from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path


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


def daily_topic_path(
    topics_root: str | Path,
    topic_id: str,
    day: date,
    week_starts_on: str = "monday",
) -> Path:
    week_start, week_end = week_bounds(day, week_starts_on)
    return (
        Path(topics_root)
        / topic_id
        / "daily"
        / str(day.year)
        / f"week-{slug_date_range(week_start, week_end)}"
        / f"{day.isoformat()}.jsonl"
    )
