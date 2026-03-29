from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from ..arxiv_html import fetch_category_list_page, parse_category_list_page
from ..config import ArxivSourceConfig
from ..dates import daterange, parse_iso_date, raw_day_dir
from ..storage import append_jsonl, ensure_dir, write_json


def run_ingest(source_config: ArxivSourceConfig, start_date, end_date) -> dict[str, Any]:
    raw_root = Path(source_config.raw_root)
    state_root = Path(source_config.state_root)
    ensure_dir(raw_root)
    ensure_dir(state_root / "manifests")

    allowed_dates = {item.isoformat() for item in daterange(start_date, end_date)}
    manifest: dict[str, Any] = {
        "stage": "ingest",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "categories": {},
        "dates": defaultdict(dict),
        "total_entries": 0,
    }

    for category in source_config.categories:
        html = fetch_category_list_page(category, source_config)
        entries = parse_category_list_page(html, category)
        filtered = [entry for entry in entries if entry["announcement_date"] in allowed_dates]
        by_day: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for entry in filtered:
            by_day[entry["announcement_date"]].append(entry)

        manifest["categories"][category] = {
            "fetched_entries": len(entries),
            "kept_entries": len(filtered),
            "days": {day: len(rows) for day, rows in sorted(by_day.items())},
        }
        manifest["total_entries"] += len(filtered)

        for day, rows in sorted(by_day.items()):
            path = (
                raw_day_dir(raw_root, parse_iso_date(day), source_config.week_starts_on)
                / f"arxiv-list.{category}.json"
            )
            write_json(
                path,
                {
                    "source": "arxiv_list_pastweek_html",
                    "category": category,
                    "announcement_date": day,
                    "fetched_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                    "count": len(rows),
                    "entries": rows,
                },
            )
            manifest["dates"][day][category] = len(rows)

    manifest["dates"] = dict(sorted(manifest["dates"].items()))
    manifest_path = state_root / "manifests" / (
        f"ingest-{start_date.isoformat()}-to-{end_date.isoformat()}.json"
    )
    write_json(manifest_path, manifest)
    append_jsonl(
        state_root / "runs.jsonl",
        {
            "stage": "ingest",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "manifest_path": str(manifest_path),
            "created_at": manifest["created_at"],
            "total_entries": manifest["total_entries"],
        },
    )
    return manifest
