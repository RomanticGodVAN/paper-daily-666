from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path
import re


MODERN_ARXIV_ID_RE = re.compile(r"^(?P<prefix>\d{4})\.\d{4,5}(?:v\d+)?$")


def parse_iso_date(value: str) -> date:
    return date.fromisoformat(value)


def daterange(start: date, end: date) -> list[date]:
    if end < start:
        raise ValueError("end date must be on or after start date")
    current = start
    result: list[date] = []
    while current <= end:
        result.append(current)
        current += timedelta(days=1)
    return result


def slug_date_range(start: date, end: date) -> str:
    return f"{start.isoformat()}-to-{end.isoformat()}"


def week_bounds(day: date, week_starts_on: str = "monday") -> tuple[date, date]:
    normalized = week_starts_on.strip().lower()
    week_start_map = {
        "monday": 0,
        "sunday": 6,
    }
    if normalized not in week_start_map:
        raise ValueError(f"Unsupported week_starts_on value: {week_starts_on}")
    start_weekday = week_start_map[normalized]
    delta = (day.weekday() - start_weekday) % 7
    start = day - timedelta(days=delta)
    end = start + timedelta(days=6)
    return start, end


def split_week_windows(start: date, end: date, week_starts_on: str = "monday") -> list[tuple[date, date]]:
    if end < start:
        raise ValueError("end date must be on or after start date")
    windows: list[tuple[date, date]] = []
    current = start
    while current <= end:
        _, week_end = week_bounds(current, week_starts_on)
        window_end = min(week_end, end)
        windows.append((current, window_end))
        current = window_end + timedelta(days=1)
    return windows


def month_prefixes_for_range(start: date, end: date) -> set[str]:
    if end < start:
        raise ValueError("end date must be on or after start date")
    prefixes: set[str] = set()
    current = date(start.year, start.month, 1)
    last = date(end.year, end.month, 1)
    while current <= last:
        prefixes.add(current.strftime("%y%m"))
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)
    return prefixes


def paper_id_matches_month_window(paper_id: str, start: date, end: date) -> bool:
    match = MODERN_ARXIV_ID_RE.match((paper_id or "").strip())
    if match is None:
        return True
    return match.group("prefix") in month_prefixes_for_range(start, end)


def week_bucket_dir(root: str | Path, day: date, week_starts_on: str = "monday") -> Path:
    week_start, week_end = week_bounds(day, week_starts_on)
    return Path(root) / str(day.year) / f"week-{slug_date_range(week_start, week_end)}"


def day_bucket_dir(root: str | Path, day: date, week_starts_on: str = "monday") -> Path:
    return week_bucket_dir(root, day, week_starts_on) / day.isoformat()


def raw_day_dir(raw_root: str | Path, day: date, week_starts_on: str = "monday") -> Path:
    return day_bucket_dir(raw_root, day, week_starts_on)


def normalized_day_path(
    normalized_root: str | Path,
    day: date,
    week_starts_on: str = "monday",
) -> Path:
    return day_bucket_dir(normalized_root, day, week_starts_on) / "papers.jsonl"


def daily_topic_path(
    topics_root: str | Path,
    topic_id: str,
    day: date,
    week_starts_on: str = "monday",
) -> Path:
    return (
        week_bucket_dir(
            Path(topics_root) / topic_id / "daily",
            day,
            week_starts_on,
        )
        / f"{day.isoformat()}.jsonl"
    )
