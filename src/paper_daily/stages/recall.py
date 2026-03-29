from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from ..config import ArxivSourceConfig, TopicConfig
from ..dates import daterange
from ..llm import DeepSeekClient
from ..storage import append_jsonl, read_jsonl, write_json, write_jsonl


def run_recall(
    source_config: ArxivSourceConfig,
    topic_config: TopicConfig,
    start_date,
    end_date,
) -> dict[str, Any]:
    normalized_root = Path(source_config.normalized_root)
    topics_root = Path(source_config.topics_root)
    state_root = Path(source_config.state_root)

    all_records: list[dict[str, Any]] = []
    for day in daterange(start_date, end_date):
        all_records.extend(read_jsonl(normalized_root / day.isoformat() / "papers.jsonl"))

    enriched = [_attach_keyword_features(record, topic_config) for record in all_records]
    llm_candidates = [record for record in enriched if record["llm_candidate"]]
    decisions: dict[str, dict[str, Any]] = {
        record["paper_id"]: {
            "decision": "exclude",
            "confidence": 0.0,
            "tags": ["prefilter_no_document_signal"],
            "reason": "No document/OCR lexical signal before LLM screening.",
        }
        for record in enriched
        if not record["llm_candidate"]
    }
    if llm_candidates:
        client = DeepSeekClient()
        decisions.update(_classify_records(client, topic_config, llm_candidates))

    included_records: list[dict[str, Any]] = []
    for record in enriched:
        decision = decisions[record["paper_id"]]
        merged = dict(record)
        merged.update(
            {
                "topic_id": topic_config.topic_id,
                "llm_decision": decision["decision"],
                "llm_confidence": decision["confidence"],
                "llm_tags": decision["tags"],
                "llm_reason": decision["reason"],
                "included": decision["decision"] == "include",
            }
        )
        if merged["included"]:
            included_records.append(merged)

    by_day: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in included_records:
        by_day[record["announcement_date"]].append(record)

    for day, rows in by_day.items():
        rows.sort(key=lambda item: item["paper_id"])
        write_jsonl(topics_root / topic_config.topic_id / "daily" / f"{day}.jsonl", rows)

    manifest: dict[str, Any] = {
        "stage": "recall",
        "topic_id": topic_config.topic_id,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "input_papers": len(enriched),
        "llm_input_papers": len(llm_candidates),
        "included_papers": len(included_records),
        "days": {day: len(rows) for day, rows in sorted(by_day.items())},
    }
    manifest_path = state_root / "manifests" / (
        f"recall-{topic_config.topic_id}-{start_date.isoformat()}-to-{end_date.isoformat()}.json"
    )
    write_json(manifest_path, manifest)
    append_jsonl(
        state_root / "runs.jsonl",
        {
            "stage": "recall",
            "topic_id": topic_config.topic_id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "manifest_path": str(manifest_path),
            "created_at": manifest["created_at"],
            "input_papers": manifest["input_papers"],
            "llm_input_papers": manifest["llm_input_papers"],
            "included_papers": manifest["included_papers"],
        },
    )
    return manifest


def _attach_keyword_features(
    record: dict[str, Any],
    topic_config: TopicConfig,
) -> dict[str, Any]:
    text = f"{record['title']} {record['abstract']}".lower()
    strong_hits = [term for term in topic_config.strong_terms if term.lower() in text]
    medium_hits = [term for term in topic_config.medium_terms if term.lower() in text]
    candidate_hits = [term for term in topic_config.candidate_terms if term.lower() in text]
    exclude_hits = [term for term in topic_config.exclude_terms if term.lower() in text]
    score = len(strong_hits) * 3 + len(medium_hits) - len(exclude_hits) * 2
    contextual_hits = _contextual_candidate_hits(text)
    enriched = dict(record)
    enriched["keyword_score"] = score
    enriched["keyword_strong_hits"] = strong_hits
    enriched["keyword_medium_hits"] = medium_hits
    enriched["keyword_candidate_hits"] = candidate_hits
    enriched["keyword_contextual_hits"] = contextual_hits
    enriched["keyword_exclude_hits"] = exclude_hits
    enriched["llm_candidate"] = bool(
        strong_hits
        or medium_hits
        or contextual_hits
        or "ocr" in candidate_hits
        or "handwritten" in candidate_hits
        or "scene text" in candidate_hits
    )
    return enriched


def _classify_records(
    client: DeepSeekClient,
    topic_config: TopicConfig,
    records: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    pending_batches = _chunk(records, topic_config.llm_batch_size)
    results: dict[str, dict[str, Any]] = {}

    while pending_batches:
        batch = pending_batches.pop(0)
        try:
            response = _classify_batch(client, topic_config, batch)
            _validate_batch_response(batch, response)
            for item in response["results"]:
                results[item["paper_id"]] = {
                    "decision": item["decision"],
                    "confidence": float(item["confidence"]),
                    "tags": item.get("tags", []),
                    "reason": item.get("reason", ""),
                }
        except Exception:
            if len(batch) == 1:
                record = batch[0]
                results[record["paper_id"]] = {
                    "decision": "exclude",
                    "confidence": 0.0,
                    "tags": ["llm_error"],
                    "reason": "LLM batch parsing failed.",
                }
            else:
                midpoint = max(1, len(batch) // 2)
                pending_batches.insert(0, batch[midpoint:])
                pending_batches.insert(0, batch[:midpoint])

    return results


def _classify_batch(
    client: DeepSeekClient,
    topic_config: TopicConfig,
    batch: list[dict[str, Any]],
) -> dict[str, Any]:
    system_prompt = (
        "You are screening arXiv papers for a high-recall OCR and Document AI tracker. "
        "Return JSON only."
    )
    blocks = []
    for record in batch:
        blocks.append(
            "\n".join(
                [
                    f"paper_id: {record['paper_id']}",
                    f"title: {record['title']}",
                    f"categories: {', '.join(record['categories'])}",
                    f"keyword_score: {record['keyword_score']}",
                    f"keyword_strong_hits: {', '.join(record['keyword_strong_hits']) or 'none'}",
                    f"keyword_medium_hits: {', '.join(record['keyword_medium_hits']) or 'none'}",
                    f"keyword_candidate_hits: {', '.join(record['keyword_candidate_hits']) or 'none'}",
                    f"keyword_contextual_hits: {', '.join(record['keyword_contextual_hits']) or 'none'}",
                    f"keyword_exclude_hits: {', '.join(record['keyword_exclude_hits']) or 'none'}",
                    f"abstract: {record['abstract']}",
                ]
            )
        )

    user_prompt = (
        f"Topic name: {topic_config.name}\n"
        f"Topic description: {topic_config.description}\n\n"
        "Inclusion rules:\n"
        "- Include only when the paper's central task materially targets OCR or document AI.\n"
        "- Positive examples: OCR, text recognition/detection in images, scene text, handwritten text recognition, layout analysis, document parsing, PDF/citation parsing, form/table/receipt/invoice understanding, document VQA, document generation/derendering, scientific paper parsing, and extracting structured content from document-like images.\n"
        "- Include multimodal or agent papers only if document/PDF/page/diagram parsing is a core contribution rather than an incidental application.\n"
        "- Exclude generic multimodal LLM papers, generic tokenization papers, generic benchmarks, generic graphic design or image generation papers, clinical documentation or transcription papers, generic RAG/document chunking papers, scientific fraud forensics, generic agents where OCR is just one supported tool, and engineering-diagram workflows whose real target is downstream simulation rather than document parsing itself.\n"
        "- Use a strict standard for centrality: an OCR/document researcher should plausibly file the paper under OCR, document understanding, page parsing, layout, or structured document generation.\n"
        "- When uncertain, prefer exclude unless the document/OCR contribution is explicit and central.\n\n"
        "Return a JSON object with this schema:\n"
        '{"results": [{"paper_id": "...", "decision": "include|exclude", "confidence": 0.0, "tags": ["..."], "reason": "short reason"}]}\n'
        "Return exactly one result per input paper_id.\n\n"
        "Papers:\n\n"
        + "\n\n---\n\n".join(blocks)
    )
    return client.chat_json(
        model=topic_config.llm_model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=4000,
        temperature=topic_config.llm_temperature,
    )


def _validate_batch_response(batch: list[dict[str, Any]], response: dict[str, Any]) -> None:
    if "results" not in response or not isinstance(response["results"], list):
        raise ValueError("Response missing results list.")
    expected = {record["paper_id"] for record in batch}
    actual = {item.get("paper_id") for item in response["results"]}
    if expected != actual:
        raise ValueError("LLM response did not return a matching paper_id set.")
    for item in response["results"]:
        if item.get("decision") not in {"include", "exclude"}:
            raise ValueError("Invalid decision.")


def _chunk(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def _contextual_candidate_hits(text: str) -> list[str]:
    rules = [
        ("document+parse", ["document", "documents"], ["parse", "parsing", "parser"]),
        (
            "document+understand",
            ["document", "documents"],
            ["understanding", "layout", "derendering", "generation", "intelligence", "grounded"],
        ),
        ("pdf+parse", ["pdf", "pdfs"], ["parse", "parsing", "citation", "extract", "extraction"]),
        (
            "scientific-paper+parse",
            ["scientific paper", "scientific papers"],
            ["parse", "parsing", "citation", "grounded", "figure"],
        ),
        ("diagram+parse", ["diagram", "diagrams"], ["parse", "parsing", "interpret", "interpretation", "extract"]),
        (
            "receipt+invoice",
            ["receipt", "receipts", "invoice", "invoices"],
            ["understanding", "recognition", "parse", "parsing", "extract"],
        ),
        (
            "visual-doc-generation",
            ["chart", "webpage", "poster", "slide", "slides"],
            ["layout", "text rendering", "generation", "document"],
        ),
    ]
    hits: list[str] = []
    for label, lhs_terms, rhs_terms in rules:
        if any(term in text for term in lhs_terms) and any(term in text for term in rhs_terms):
            hits.append(label)
    return hits
