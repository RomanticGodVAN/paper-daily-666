from __future__ import annotations

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime
from html import unescape
import re
from threading import local
import time
from typing import Any

from bs4 import BeautifulSoup
import requests

from .config import ArxivSourceConfig


MONTHS = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}

DATE_HEADER_RE = re.compile(r"([A-Z][a-z]{2}), (\d{1,2}) ([A-Z][a-z]{2}) (\d{4})")
CATEGORY_RE = re.compile(r"\b[a-z-]+\.[A-Z0-9-]+\b")
THREAD_LOCAL = local()


def _get_session(user_agent: str) -> requests.Session:
    session = getattr(THREAD_LOCAL, "session", None)
    if session is None:
        session = requests.Session()
        session.headers.update({"User-Agent": user_agent})
        THREAD_LOCAL.session = session
    return session


def _fetch_text(url: str, config: ArxivSourceConfig, retries: int = 5) -> str:
    session = _get_session(config.user_agent)
    backoff = 1.5
    for attempt in range(retries):
        try:
            response = session.get(url, timeout=config.request_timeout_seconds)
            if response.status_code in {429, 500, 502, 503, 504}:
                if attempt == retries - 1:
                    response.raise_for_status()
                time.sleep(backoff)
                backoff *= 2
                continue
            response.raise_for_status()
            response.encoding = "utf-8"
            return response.text
        except requests.RequestException:
            if attempt == retries - 1:
                raise
            time.sleep(backoff)
            backoff *= 2
    raise RuntimeError(f"Failed to fetch URL after retries: {url}")


def fetch_category_list_page(category: str, config: ArxivSourceConfig) -> str:
    url = f"https://arxiv.org/list/{category}/pastweek?show={config.list_page_show}"
    return _fetch_text(url, config)


def parse_category_list_page(html: str, category: str) -> list[dict[str, Any]]:
    soup = BeautifulSoup(html, "html.parser")
    article_blocks = soup.select("dl#articles")
    if not article_blocks:
        raise ValueError(f"Could not find article list for category {category}")
    entries: list[dict[str, Any]] = []

    for articles in article_blocks:
        current_date: date | None = None
        pending_id: str | None = None
        for child in articles.children:
            if getattr(child, "name", None) == "h3":
                current_date = _parse_heading_date(child.get_text(" ", strip=True))
                continue
            if getattr(child, "name", None) == "dt":
                abs_link = child.find("a", href=re.compile(r"^/abs/"))
                if abs_link is None:
                    pending_id = None
                    continue
                pending_id = abs_link.get_text(strip=True).replace("arXiv:", "")
                continue
            if getattr(child, "name", None) == "dd" and current_date and pending_id:
                entries.append(_parse_list_item(child, category, current_date, pending_id))
                pending_id = None

    return entries


def fetch_abs_records(
    stubs: list[dict[str, Any]],
    config: ArxivSourceConfig,
) -> list[dict[str, Any]]:
    results: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=max(1, config.abs_fetch_workers)) as executor:
        future_map = {
            executor.submit(fetch_abs_record, stub, config): stub["paper_id"]
            for stub in stubs
        }
        for future in as_completed(future_map):
            record = future.result()
            results[record["paper_id"]] = record
    return [results[stub["paper_id"]] for stub in stubs]


def fetch_abs_record(stub: dict[str, Any], config: ArxivSourceConfig) -> dict[str, Any]:
    html = _fetch_text(stub["abs_url"], config)
    soup = BeautifulSoup(html, "html.parser")
    meta = _collect_meta(soup)

    abstract = meta.get("citation_abstract") or _extract_abstract(soup)
    title = meta.get("citation_title") or stub["title"]
    authors = meta.get("citation_author", []) or stub["authors"]

    subjects_cell = soup.select_one("td.tablecell.subjects")
    subjects_text = subjects_cell.get_text(" ", strip=True) if subjects_cell else ""
    categories = sorted(set(CATEGORY_RE.findall(subjects_text))) or stub["subject_categories"]
    primary_node = subjects_cell.select_one(".primary-subject") if subjects_cell else None
    primary_subject = (
        primary_node.get_text(" ", strip=True) if primary_node is not None else stub["primary_subject"]
    )

    comments = ""
    comments_label = soup.find("td", class_="tablecell label", string=re.compile(r"Comments:"))
    if comments_label is not None:
        comments_value = comments_label.find_next_sibling("td")
        if comments_value is not None:
            comments = _collapse_ws(comments_value.get_text(" ", strip=True))

    dateline = soup.select_one(".dateline")
    submitted_date = _parse_submitted_date(dateline.get_text(" ", strip=True) if dateline else "")

    paper_id = meta.get("citation_arxiv_id") or stub["paper_id"]
    base_paper_id = paper_id.split("v", 1)[0]
    version_match = re.search(r"v(\d+)$", paper_id)
    version = int(version_match.group(1)) if version_match else None

    return {
        "paper_id": paper_id,
        "base_paper_id": base_paper_id,
        "version": version,
        "title": _collapse_ws(title),
        "abstract": _collapse_ws(abstract),
        "authors": authors,
        "comments": comments,
        "categories": categories,
        "primary_subject": primary_subject,
        "abs_url": stub["abs_url"],
        "announcement_date": stub["announcement_date"],
        "submitted_date": submitted_date,
        "source_categories": sorted(set(stub["source_categories"])),
        "fetched_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }


def _parse_heading_date(text: str) -> date:
    match = DATE_HEADER_RE.search(text)
    if match is None:
        raise ValueError(f"Could not parse date from heading: {text}")
    _, day, month_abbr, year = match.groups()
    return date(int(year), MONTHS[month_abbr], int(day))


def _parse_list_item(node: Any, category: str, announcement_date: date, paper_id: str) -> dict[str, Any]:
    title_node = node.select_one(".list-title")
    title = ""
    if title_node is not None:
        title = title_node.get_text(" ", strip=True).replace("Title:", "", 1).strip()
    authors = [anchor.get_text(" ", strip=True) for anchor in node.select(".list-authors a")]
    subjects_text = node.select_one(".list-subjects").get_text(" ", strip=True) if node.select_one(".list-subjects") else ""
    primary_node = node.select_one(".list-subjects .primary-subject")
    primary_subject = primary_node.get_text(" ", strip=True) if primary_node else ""
    categories = sorted(set(CATEGORY_RE.findall(subjects_text)))
    return {
        "paper_id": paper_id,
        "abs_url": f"https://arxiv.org/abs/{paper_id}",
        "source_category": category,
        "title": _collapse_ws(title),
        "authors": authors,
        "primary_subject": primary_subject,
        "subject_categories": categories,
        "announcement_date": announcement_date.isoformat(),
    }


def _collect_meta(soup: BeautifulSoup) -> dict[str, Any]:
    meta: dict[str, Any] = defaultdict(list)
    for node in soup.find_all("meta"):
        name = node.get("name")
        content = node.get("content")
        if not name or content is None:
            continue
        if name == "citation_author":
            meta[name].append(unescape(content))
        else:
            meta[name] = unescape(content)
    return dict(meta)


def _extract_abstract(soup: BeautifulSoup) -> str:
    abstract_node = soup.select_one("blockquote.abstract")
    if abstract_node is None:
        return ""
    return abstract_node.get_text(" ", strip=True).replace("Abstract:", "", 1).strip()


def _parse_submitted_date(text: str) -> str:
    match = re.search(r"Submitted on (\d{1,2}) ([A-Z][a-z]{2}) (\d{4})", text)
    if match is None:
        return ""
    day, month_abbr, year = match.groups()
    return date(int(year), MONTHS[month_abbr], int(day)).isoformat()


def _collapse_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
