from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import load_arxiv_source_config, load_topic_config
from .dates import parse_iso_date
from .stages.backfill import run_backfill
from .stages.ingest import run_ingest
from .stages.normalize import run_normalize
from .stages.recall import run_recall
from .stages.weekly import run_weekly_bundle


REPO_LAYOUT = """\
Repository contract:

- data/raw/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD/YYYY-MM-DD/: immutable source snapshots
- data/normalized/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD/YYYY-MM-DD/papers.jsonl: canonical per-day records after deduplication
- data/state/: run metadata and checkpoints
- data/topics/<topic-id>/daily/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD/YYYY-MM-DD.jsonl: topic daily matches
- data/topics/<topic-id>/weekly/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD.json: weekly topic bundle
- config/arxiv.toml: global source and storage contract
- topics/*.toml: topic definitions
- src/paper_daily/stages/: ingest / normalize / recall / weekly
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="paper-daily",
        description="Repository utilities for the paper-daily scaffold.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    show_topic = subparsers.add_parser(
        "show-topic",
        help="Load and print a topic config.",
    )
    show_topic.add_argument("config", help="Path to a topic TOML file.")

    show_source = subparsers.add_parser(
        "show-source",
        help="Load and print a global source config.",
    )
    show_source.add_argument("config", help="Path to a source TOML file.")

    subparsers.add_parser(
        "print-layout",
        help="Print the current repository layout contract.",
    )

    for name, help_text in [
        ("ingest-window", "Fetch raw arXiv list-page snapshots for a date window."),
        ("normalize-window", "Fetch abstracts and normalize papers for a date window."),
        ("recall-window", "Run OCR/document topic recall for a date window."),
        ("weekly-window", "Materialize a weekly bundle for a date window."),
        ("run-window", "Run ingest, normalize, recall, and weekly stages."),
        ("backfill-range", "Run ingest/normalize/recall once, then materialize weekly bundles across the date range."),
    ]:
        command = subparsers.add_parser(name, help=help_text)
        command.add_argument(
            "--source",
            default="config/arxiv.toml",
            help="Path to the global source config.",
        )
        command.add_argument("--start-date", required=True, help="Start date in YYYY-MM-DD.")
        command.add_argument("--end-date", required=True, help="End date in YYYY-MM-DD.")
        if name in {"recall-window", "weekly-window", "run-window", "backfill-range"}:
            command.add_argument(
                "--topic",
                default="topics/document_ocr.toml",
                help="Path to the topic config.",
            )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "show-topic":
        config = load_topic_config(Path(args.config))
        print(json.dumps(config.to_dict(), indent=2, ensure_ascii=False))
        return 0

    if args.command == "show-source":
        config = load_arxiv_source_config(Path(args.config))
        print(json.dumps(config.to_dict(), indent=2, ensure_ascii=False))
        return 0

    if args.command == "print-layout":
        print(REPO_LAYOUT)
        print("Current scope ends at weekly topic bundles, not report generation.")
        print("The repository now supports a full prototype pipeline for rolling week windows.")
        return 0

    if args.command in {
        "ingest-window",
        "normalize-window",
        "recall-window",
        "weekly-window",
        "run-window",
        "backfill-range",
    }:
        source_config = load_arxiv_source_config(Path(args.source))
        start_date = parse_iso_date(args.start_date)
        end_date = parse_iso_date(args.end_date)

        if args.command == "ingest-window":
            print(
                json.dumps(
                    run_ingest(source_config, start_date, end_date),
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0

        if args.command == "normalize-window":
            print(
                json.dumps(
                    run_normalize(source_config, start_date, end_date),
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0

        topic_config = load_topic_config(Path(args.topic))
        if args.command == "recall-window":
            print(
                json.dumps(
                    run_recall(source_config, topic_config, start_date, end_date),
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0

        if args.command == "weekly-window":
            print(
                json.dumps(
                    run_weekly_bundle(source_config, topic_config, start_date, end_date),
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0

        if args.command == "run-window":
            ingest = run_ingest(source_config, start_date, end_date)
            normalize = run_normalize(source_config, start_date, end_date)
            recall = run_recall(source_config, topic_config, start_date, end_date)
            weekly = run_weekly_bundle(source_config, topic_config, start_date, end_date)
            print(
                json.dumps(
                    {
                        "ingest": ingest,
                        "normalize": normalize,
                        "recall": recall,
                        "weekly": weekly,
                    },
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0

        if args.command == "backfill-range":
            print(
                json.dumps(
                    run_backfill(source_config, topic_config, start_date, end_date),
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return 0

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
