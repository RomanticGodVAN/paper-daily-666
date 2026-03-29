from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import tomllib


@dataclass(slots=True)
class ArxivSourceConfig:
    provider: str
    timezone: str
    week_starts_on: str
    categories: list[str]
    user_agent: str
    list_page_show: int
    request_timeout_seconds: int
    abs_fetch_workers: int
    raw_root: str
    normalized_root: str
    state_root: str
    topics_root: str
    canonical_id: str
    track_versions: bool
    deduplicate_across_categories: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class TopicConfig:
    topic_id: str
    name: str
    description: str
    enabled: bool
    minimum_score: int
    strong_terms: list[str]
    medium_terms: list[str]
    candidate_terms: list[str]
    exclude_terms: list[str]
    llm_model: str
    llm_batch_size: int
    llm_temperature: float
    weekly_enabled: bool
    include_match_explanations: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def _read_table(data: dict[str, object], key: str) -> dict[str, object]:
    table = data.get(key)
    if not isinstance(table, dict):
        raise ValueError(f"Missing or invalid [{key}] table.")
    return table


def _read_string_list(table: dict[str, object], key: str) -> list[str]:
    value = table.get(key)
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"Expected '{key}' to be a list of strings.")
    return value


def load_arxiv_source_config(path: str | Path) -> ArxivSourceConfig:
    config_path = Path(path)
    raw = tomllib.loads(config_path.read_text(encoding="utf-8"))

    source = _read_table(raw, "source")
    storage = _read_table(raw, "storage")
    normalization = _read_table(raw, "normalization")

    return ArxivSourceConfig(
        provider=_require_string(source, "provider"),
        timezone=_require_string(source, "timezone"),
        week_starts_on=_require_string(source, "week_starts_on"),
        categories=_read_string_list(source, "categories"),
        user_agent=_require_string(source, "user_agent"),
        list_page_show=_require_int(source, "list_page_show"),
        request_timeout_seconds=_require_int(source, "request_timeout_seconds"),
        abs_fetch_workers=_require_int(source, "abs_fetch_workers"),
        raw_root=_require_string(storage, "raw_root"),
        normalized_root=_require_string(storage, "normalized_root"),
        state_root=_require_string(storage, "state_root"),
        topics_root=_require_string(storage, "topics_root"),
        canonical_id=_require_string(normalization, "canonical_id"),
        track_versions=_require_bool(normalization, "track_versions"),
        deduplicate_across_categories=_require_bool(
            normalization,
            "deduplicate_across_categories",
        ),
    )


def load_topic_config(path: str | Path) -> TopicConfig:
    config_path = Path(path)
    raw = tomllib.loads(config_path.read_text(encoding="utf-8"))

    topic = _read_table(raw, "topic")
    retrieval = _read_table(raw, "retrieval")
    weekly = _read_table(raw, "weekly")

    return TopicConfig(
        topic_id=_require_string(topic, "id"),
        name=_require_string(topic, "name"),
        description=_require_string(topic, "description"),
        enabled=_require_bool(topic, "enabled"),
        minimum_score=_require_int(retrieval, "minimum_score"),
        strong_terms=_read_string_list(retrieval, "strong_terms"),
        medium_terms=_read_string_list(retrieval, "medium_terms"),
        candidate_terms=_read_string_list(retrieval, "candidate_terms"),
        exclude_terms=_read_string_list(retrieval, "exclude_terms"),
        llm_model=_require_string(retrieval, "llm_model"),
        llm_batch_size=_require_int(retrieval, "llm_batch_size"),
        llm_temperature=_require_float(retrieval, "llm_temperature"),
        weekly_enabled=_require_bool(weekly, "enabled"),
        include_match_explanations=_require_bool(
            weekly,
            "include_match_explanations",
        ),
    )


def _require_string(table: dict[str, object], key: str) -> str:
    value = table.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Expected '{key}' to be a non-empty string.")
    return value


def _require_bool(table: dict[str, object], key: str) -> bool:
    value = table.get(key)
    if not isinstance(value, bool):
        raise ValueError(f"Expected '{key}' to be a boolean.")
    return value


def _require_int(table: dict[str, object], key: str) -> int:
    value = table.get(key)
    if not isinstance(value, int):
        raise ValueError(f"Expected '{key}' to be an integer.")
    return value


def _require_float(table: dict[str, object], key: str) -> float:
    value = table.get(key)
    if not isinstance(value, (int, float)):
        raise ValueError(f"Expected '{key}' to be a float.")
    return float(value)
