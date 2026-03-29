from __future__ import annotations

from datetime import date, timedelta


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
