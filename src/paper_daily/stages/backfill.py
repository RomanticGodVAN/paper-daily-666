from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from ..config import ArxivSourceConfig, TopicConfig
from ..dates import slug_date_range, split_week_windows
from ..storage import append_jsonl, write_json
from .ingest_api import run_ingest_api
from .normalize import run_normalize
from .recall import run_recall
from .weekly import run_weekly_bundle


def run_backfill(
    source_config: ArxivSourceConfig,
    topic_config: TopicConfig,
    start_date,
    end_date,
) -> dict[str, Any]:
    state_root = Path(source_config.state_root)

    ingest = run_ingest_api(source_config, start_date, end_date)
    normalize = run_normalize(source_config, start_date, end_date)
    recall = run_recall(source_config, topic_config, start_date, end_date)

    weekly_manifests: list[dict[str, Any]] = []
    for window_start, window_end in split_week_windows(
        start_date,
        end_date,
        source_config.week_starts_on,
    ):
        weekly_manifests.append(
            run_weekly_bundle(
                source_config,
                topic_config,
                window_start,
                window_end,
            )
        )

    summary: dict[str, Any] = {
        "stage": "backfill",
        "topic_id": topic_config.topic_id,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "week_windows": [
            {
                "start_date": item["start_date"],
                "end_date": item["end_date"],
                "paper_count": item["paper_count"],
                "json_path": item["json_path"],
                "markdown_path": item["markdown_path"],
            }
            for item in weekly_manifests
        ],
        "window_count": len(weekly_manifests),
        "ingest": {
            "total_entries": ingest["total_entries"],
        },
        "normalize": {
            "total_unique_papers": normalize["total_unique_papers"],
        },
        "recall": {
            "input_papers": recall["input_papers"],
            "llm_input_papers": recall["llm_input_papers"],
            "included_papers": recall["included_papers"],
        },
        "ingest_stage": "ingest_oai",
        "date_kind": "created_date",
    }
    manifest_path = state_root / "manifests" / (
        f"backfill-{topic_config.topic_id}-{slug_date_range(start_date, end_date)}.json"
    )
    write_json(manifest_path, summary)
    append_jsonl(
        state_root / "runs.jsonl",
        {
            "stage": "backfill",
            "topic_id": topic_config.topic_id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "manifest_path": str(manifest_path),
            "created_at": summary["created_at"],
            "window_count": summary["window_count"],
            "included_papers": summary["recall"]["included_papers"],
        },
    )
    summary["manifest_path"] = str(manifest_path)
    return summary
