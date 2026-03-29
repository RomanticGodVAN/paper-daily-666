from __future__ import annotations

from datetime import date, datetime
from html import unescape
import re
import time
from typing import Any
import xml.etree.ElementTree as ET

import requests

from .config import ArxivSourceConfig


OAI_NS = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "arxiv": "http://arxiv.org/OAI/arXiv/",
}
CATEGORY_RE = re.compile(r"\b[a-z-]+\.[A-Z0-9-]+\b")


class ArxivOaiClient:
    def __init__(self, config: ArxivSourceConfig) -> None:
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": config.user_agent})
        self._last_request_monotonic: float | None = None

    def list_cs_records_for_created_range(
        self,
        start_date: date,
        end_date: date,
    ) -> dict[str, Any]:
        params: dict[str, str] | None = {
            "verb": "ListRecords",
            "metadataPrefix": "arXiv",
            "from": start_date.isoformat(),
            "until": end_date.isoformat(),
            "set": "cs",
        }
        entries: list[dict[str, Any]] = []
        pages: list[dict[str, Any]] = []
        while True:
            payload = self._request(params)
            entries.extend(payload["entries"])
            pages.append(
                {
                    "record_count": len(payload["entries"]),
                    "resumption_token_present": bool(payload["resumption_token"]),
                }
            )
            if not payload["resumption_token"]:
                break
            params = {
                "verb": "ListRecords",
                "resumptionToken": payload["resumption_token"],
            }
        return {
            "entries": [
                entry
                for entry in entries
                if start_date <= date.fromisoformat(entry["created_date"]) <= end_date
            ],
            "pages": pages,
        }

    def _request(self, params: dict[str, str], retries: int = 5) -> dict[str, Any]:
        backoff = 2.0
        for attempt in range(retries):
            self._respect_rate_limit()
            response = self.session.get(
                "https://oaipmh.arxiv.org/oai",
                params=params,
                timeout=self.config.request_timeout_seconds,
            )
            self._last_request_monotonic = time.monotonic()
            if response.status_code in {429, 500, 502, 503, 504}:
                if attempt == retries - 1:
                    response.raise_for_status()
                time.sleep(backoff)
                backoff *= 2
                continue
            response.raise_for_status()
            response.encoding = "utf-8"
            return _parse_oai_page(response.text)
        raise RuntimeError("arXiv OAI-PMH request failed after retries.")

    def _respect_rate_limit(self) -> None:
        if self._last_request_monotonic is None:
            return
        elapsed = time.monotonic() - self._last_request_monotonic
        wait_seconds = 1.1 - elapsed
        if wait_seconds > 0:
            time.sleep(wait_seconds)


def _parse_oai_page(xml_text: str) -> dict[str, Any]:
    root = ET.fromstring(xml_text)
    token_node = root.find(".//oai:resumptionToken", OAI_NS)
    resumption_token = token_node.text.strip() if token_node is not None and token_node.text else ""
    entries: list[dict[str, Any]] = []

    for record in root.findall(".//oai:record", OAI_NS):
        header = record.find("oai:header", OAI_NS)
        if header is None or header.attrib.get("status") == "deleted":
            continue
        metadata = record.find("oai:metadata/arxiv:arXiv", OAI_NS)
        if metadata is None:
            continue
        parsed = _parse_record(metadata)
        if parsed is not None:
            entries.append(parsed)

    return {
        "entries": entries,
        "resumption_token": resumption_token,
    }


def _parse_record(node: ET.Element) -> dict[str, Any] | None:
    paper_id = (node.findtext("arxiv:id", default="", namespaces=OAI_NS) or "").strip()
    created_date = (node.findtext("arxiv:created", default="", namespaces=OAI_NS) or "").strip()
    if not paper_id or not created_date:
        return None

    categories_text = node.findtext("arxiv:categories", default="", namespaces=OAI_NS) or ""
    categories = [term for term in categories_text.split() if CATEGORY_RE.fullmatch(term)]
    authors_node = node.find("arxiv:authors", OAI_NS)
    authors: list[str] = []
    if authors_node is not None:
        for author in authors_node.findall("arxiv:author", OAI_NS):
            keyname = author.findtext("arxiv:keyname", default="", namespaces=OAI_NS).strip()
            forenames = author.findtext("arxiv:forenames", default="", namespaces=OAI_NS).strip()
            if forenames and keyname:
                authors.append(f"{forenames} {keyname}")
            elif keyname:
                authors.append(keyname)

    primary_subject = categories[0] if categories else ""
    updated_date = (node.findtext("arxiv:updated", default="", namespaces=OAI_NS) or "").strip()

    return {
        "paper_id": paper_id,
        "base_paper_id": paper_id.split("v", 1)[0],
        "version": None,
        "abs_url": f"https://arxiv.org/abs/{paper_id}",
        "title": _collapse_ws(unescape(node.findtext("arxiv:title", default="", namespaces=OAI_NS) or "")),
        "abstract": _collapse_ws(unescape(node.findtext("arxiv:abstract", default="", namespaces=OAI_NS) or "")),
        "authors": authors,
        "comments": _collapse_ws(unescape(node.findtext("arxiv:comments", default="", namespaces=OAI_NS) or "")),
        "categories": sorted(set(categories)),
        "primary_subject": primary_subject,
        "created_date": created_date,
        "updated_date": updated_date,
    }


def _collapse_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
