from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from ..arxiv_oai import ArxivOaiClient
from ..config import ArxivSourceConfig
from ..dates import parse_iso_date, raw_day_dir
from ..storage import append_jsonl, ensure_dir, write_json


def run_ingest_api(source_config: ArxivSourceConfig, start_date, end_date) -> dict[str, Any]:
    raw_root = Path(source_config.raw_root)
    state_root = Path(source_config.state_root)
    ensure_dir(raw_root)
    ensure_dir(state_root / "manifests")

    client = ArxivOaiClient(source_config)
    manifest: dict[str, Any] = {
        "stage": "ingest_oai",
        "date_kind": "created_date",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "categories": {},
        "dates": defaultdict(dict),
        "total_entries": 0,
    }

    payload = client.list_cs_records_for_created_range(start_date, end_date)
    by_category_day: dict[str, dict[str, list[dict[str, Any]]]] = {
        category: defaultdict(list) for category in source_config.categories
    }

    for entry in payload["entries"]:
        target_categories = [
            category for category in source_config.categories if category in entry["categories"]
        ]
        if not target_categories:
            continue
        for category in target_categories:
            row = dict(entry)
            row["announcement_date"] = entry["created_date"]
            row["submitted_date"] = entry["created_date"]
            row["source_category"] = category
            row["subject_categories"] = list(entry["categories"])
            by_category_day[category][row["announcement_date"]].append(row)

    for category in source_config.categories:
        by_day = by_category_day[category]
        kept_entries = sum(len(rows) for rows in by_day.values())
        manifest["categories"][category] = {
            "source": "oaipmh.arxiv.org/oai",
            "set": "cs",
            "fetched_pages": len(payload["pages"]),
            "kept_entries": kept_entries,
            "days": {day: len(rows) for day, rows in sorted(by_day.items())},
        }
        manifest["total_entries"] += kept_entries

        for day, rows in sorted(by_day.items()):
            path = (
                raw_day_dir(raw_root, parse_iso_date(day), source_config.week_starts_on)
                / f"arxiv-list.{category}.json"
            )
            write_json(
                path,
                {
                    "source": "arxiv_oai_query",
                    "date_kind": "created_date",
                    "category": category,
                    "announcement_date": day,
                    "fetched_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                    "set": "cs",
                    "count": len(rows),
                    "entries": rows,
                },
            )
            manifest["dates"][day][category] = len(rows)

    manifest["dates"] = dict(sorted(manifest["dates"].items()))
    manifest_path = state_root / "manifests" / (
        f"ingest-oai-{start_date.isoformat()}-to-{end_date.isoformat()}.json"
    )
    write_json(manifest_path, manifest)
    append_jsonl(
        state_root / "runs.jsonl",
        {
            "stage": "ingest_oai",
            "date_kind": "created_date",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "manifest_path": str(manifest_path),
            "created_at": manifest["created_at"],
            "total_entries": manifest["total_entries"],
        },
    )
    return manifest
