from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from ..config import ArxivSourceConfig, TopicConfig
from ..dates import daily_topic_path
from ..storage import append_jsonl, read_json, read_jsonl, write_json


def run_daily_bundle(
    source_config: ArxivSourceConfig,
    topic_config: TopicConfig,
    day,
    export_root: str | Path | None = None,
) -> dict[str, Any]:
    topics_root = Path(source_config.topics_root)
    state_root = Path(source_config.state_root)

    source_path = daily_topic_path(
        topics_root,
        topic_config.topic_id,
        day,
        source_config.week_starts_on,
    )
    records = read_jsonl(source_path)

    dedupe_index_path = state_root / "dedupe" / f"{topic_config.topic_id}.json"
    dedupe_index = _load_dedupe_index(dedupe_index_path)

    selected: list[dict[str, Any]] = []
    skipped_duplicates: list[dict[str, Any]] = []
    for record in sorted(records, key=lambda item: item["paper_id"]):
        key = record["base_paper_id"]
        first_included_on = dedupe_index.get(key)
        if first_included_on:
            skipped_duplicates.append(
                {
                    "paper_id": record["paper_id"],
                    "base_paper_id": key,
                    "first_included_on": first_included_on,
                }
            )
            continue
        dedupe_index[key] = day.isoformat()
        selected.append(record)

    write_json(
        dedupe_index_path,
        {
            "topic_id": topic_config.topic_id,
            "updated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "papers": dict(sorted(dedupe_index.items())),
        },
    )

    export_base = Path(export_root) if export_root else Path(topic_config.topic_id)
    output_dir = export_base / day.isoformat()
    json_path = output_dir / "papers.json"
    md_path = output_dir / "README.md"

    payload: dict[str, Any] = {
        "topic_id": topic_config.topic_id,
        "topic_name": topic_config.name,
        "date": day.isoformat(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "source_daily_path": str(source_path),
        "paper_count": len(selected),
        "duplicate_skipped_count": len(skipped_duplicates),
        "papers": selected,
        "skipped_duplicates": skipped_duplicates,
    }
    write_json(json_path, payload)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(_render_markdown(payload), encoding="utf-8")

    manifest = {
        "stage": "daily",
        "topic_id": topic_config.topic_id,
        "date": day.isoformat(),
        "created_at": payload["created_at"],
        "paper_count": len(selected),
        "duplicate_skipped_count": len(skipped_duplicates),
        "json_path": str(json_path),
        "markdown_path": str(md_path),
        "dedupe_index_path": str(dedupe_index_path),
    }
    manifest_path = state_root / "manifests" / (
        f"daily-{topic_config.topic_id}-{day.isoformat()}.json"
    )
    write_json(manifest_path, manifest)
    append_jsonl(
        state_root / "runs.jsonl",
        {
            "stage": "daily",
            "topic_id": topic_config.topic_id,
            "date": day.isoformat(),
            "manifest_path": str(manifest_path),
            "created_at": payload["created_at"],
            "paper_count": len(selected),
            "duplicate_skipped_count": len(skipped_duplicates),
        },
    )
    return manifest


def _load_dedupe_index(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    payload = read_json(path)
    if not isinstance(payload, dict):
        return {}
    papers = payload.get("papers")
    if not isinstance(papers, dict):
        return {}
    result: dict[str, str] = {}
    for key, value in papers.items():
        if isinstance(key, str) and isinstance(value, str):
            result[key] = value
    return result


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# {payload['topic_name']} — {payload['date']}",
        "",
        f"- Papers: {payload['paper_count']}",
        f"- Skipped as duplicates: {payload['duplicate_skipped_count']}",
        "",
    ]

    if not payload["papers"]:
        lines.append("今天没有新增推荐论文。")
        lines.append("")
        return "\n".join(lines).strip() + "\n"

    for index, paper in enumerate(payload["papers"], start=1):
        lines.append(f"## {index}. {paper['title']}")
        lines.append("")
        lines.append(f"- arXiv: `{paper['paper_id']}`")
        lines.append(f"- Link: {paper['abs_url']}")
        lines.append(f"- Announcement date: {paper['announcement_date']}")
        lines.append(f"- Categories: {', '.join(paper['categories'])}")
        lines.append(f"- Tags: {', '.join(paper['llm_tags']) or 'none'}")
        lines.append(f"- Reason: {paper['llm_reason'] or 'n/a'}")
        lines.append("")
        lines.append("### Abstract")
        lines.append("")
        lines.append(paper.get("abstract", ""))
        lines.append("")

    return "\n".join(lines).strip() + "\n"
