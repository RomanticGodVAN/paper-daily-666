from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from ..config import ArxivSourceConfig, TopicConfig
from ..dates import daily_topic_path, daterange, slug_date_range
from ..storage import append_jsonl, read_jsonl, write_json


def run_weekly_bundle(
    source_config: ArxivSourceConfig,
    topic_config: TopicConfig,
    start_date,
    end_date,
) -> dict[str, Any]:
    topics_root = Path(source_config.topics_root)
    state_root = Path(source_config.state_root)

    records: list[dict[str, Any]] = []
    for day in daterange(start_date, end_date):
        records.extend(
            read_jsonl(
                daily_topic_path(
                    topics_root,
                    topic_config.topic_id,
                    day,
                    source_config.week_starts_on,
                )
            )
        )

    merged: dict[str, dict[str, Any]] = {}
    for record in records:
        key = record["base_paper_id"]
        if key not in merged:
            merged[key] = dict(record)
            continue
        current = merged[key]
        current["source_categories"] = sorted(
            set(current["source_categories"] + record["source_categories"])
        )
        current["categories"] = sorted(set(current["categories"] + record["categories"]))

    papers = sorted(
        merged.values(),
        key=lambda item: (item["announcement_date"], item["paper_id"]),
        reverse=True,
    )

    date_slug = slug_date_range(start_date, end_date)
    weekly_dir = topics_root / topic_config.topic_id / "weekly" / str(start_date.year)
    json_path = weekly_dir / f"week-{date_slug}.json"
    md_path = weekly_dir / f"week-{date_slug}.md"

    payload: dict[str, Any] = {
        "topic_id": topic_config.topic_id,
        "topic_name": topic_config.name,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "paper_count": len(papers),
        "papers": papers,
    }
    write_json(json_path, payload)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(_render_markdown(payload), encoding="utf-8")

    manifest = {
        "stage": "weekly",
        "topic_id": topic_config.topic_id,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "created_at": payload["created_at"],
        "paper_count": len(papers),
        "json_path": str(json_path),
        "markdown_path": str(md_path),
    }
    manifest_path = state_root / "manifests" / (
        f"weekly-{topic_config.topic_id}-{date_slug}.json"
    )
    write_json(manifest_path, manifest)
    append_jsonl(
        state_root / "runs.jsonl",
        {
            "stage": "weekly",
            "topic_id": topic_config.topic_id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "manifest_path": str(manifest_path),
            "created_at": payload["created_at"],
            "paper_count": len(papers),
        },
    )
    return manifest


def _render_markdown(payload: dict[str, Any]) -> str:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in payload["papers"]:
        groups[paper["announcement_date"]].append(paper)

    lines = [
        f"# {payload['topic_name']}",
        "",
        f"- Window: {payload['start_date']} to {payload['end_date']}",
        f"- Papers: {payload['paper_count']}",
        "",
    ]

    for day in sorted(groups, reverse=True):
        lines.append(f"## {day}")
        lines.append("")
        for paper in groups[day]:
            lines.append(
                f"- [{paper['title']}]({paper['abs_url']}) "
                f"(`{paper['paper_id']}`; categories: {', '.join(paper['categories'])})"
            )
            lines.append(
                f"  submitted: {paper['submitted_date'] or 'unknown'}; "
                f"keyword_score: {paper['keyword_score']}; "
                f"tags: {', '.join(paper['llm_tags']) or 'none'}"
            )
            lines.append(f"  reason: {paper['llm_reason'] or 'n/a'}")
            lines.append("")
    return "\n".join(lines).strip() + "\n"
