from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from ..arxiv_html import fetch_abs_records
from ..config import ArxivSourceConfig
from ..dates import daterange, normalized_day_path, raw_day_dir
from ..storage import append_jsonl, read_json, write_json, write_jsonl


def run_normalize(source_config: ArxivSourceConfig, start_date, end_date) -> dict[str, Any]:
    raw_root = Path(source_config.raw_root)
    normalized_root = Path(source_config.normalized_root)
    state_root = Path(source_config.state_root)

    manifest: dict[str, Any] = {
        "stage": "normalize",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "days": {},
        "total_unique_papers": 0,
    }

    for day in daterange(start_date, end_date):
        day_str = day.isoformat()
        day_dir = raw_day_dir(raw_root, day, source_config.week_starts_on)
        files = sorted(day_dir.glob("arxiv-list.*.json"))
        if not files:
            manifest["days"][day_str] = {"raw_files": 0, "unique_papers": 0}
            continue

        merged: dict[str, dict[str, Any]] = {}
        for file in files:
            payload = read_json(file)
            for entry in payload["entries"]:
                paper_id = entry["paper_id"]
                if paper_id not in merged:
                    merged[paper_id] = dict(entry)
                    merged[paper_id]["source_categories"] = [entry["source_category"]]
                else:
                    current = merged[paper_id]
                    current["source_categories"] = sorted(
                        set(current["source_categories"] + [entry["source_category"]])
                    )
                    current["subject_categories"] = sorted(
                        set(current["subject_categories"] + entry["subject_categories"])
                    )

        stubs = [merged[key] for key in sorted(merged)]
        records = fetch_abs_records(stubs, source_config)

        out_path = normalized_day_path(
            normalized_root,
            day,
            source_config.week_starts_on,
        )
        write_jsonl(out_path, records)
        manifest["days"][day_str] = {
            "raw_files": len(files),
            "unique_papers": len(records),
            "output_path": str(out_path),
        }
        manifest["total_unique_papers"] += len(records)

    manifest_path = state_root / "manifests" / (
        f"normalize-{start_date.isoformat()}-to-{end_date.isoformat()}.json"
    )
    write_json(manifest_path, manifest)
    append_jsonl(
        state_root / "runs.jsonl",
        {
            "stage": "normalize",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "manifest_path": str(manifest_path),
            "created_at": manifest["created_at"],
            "total_unique_papers": manifest["total_unique_papers"],
        },
    )
    return manifest
