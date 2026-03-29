# AGENTS

This repository is a working prototype for rolling-window arXiv topic tracking.

The current scope ends at:

- raw daily announcement snapshots
- normalized daily paper records
- topic daily matches
- weekly topic bundles

It does not generate final polished reports or external publications.

## Main Entry Points

- CLI: `python -m paper_daily.cli`
- wrapper script: `scripts/run_topic_week.ps1`

## Required Environment

- Python 3.11+
- install package dependencies from `pyproject.toml`
- set `DEEPSEEK_API_KEY` before running `recall-window` or `run-window`

Example:

```powershell
$env:PYTHONPATH = "src"
$env:DEEPSEEK_API_KEY = "your-key"
python -m paper_daily.cli run-window `
  --start-date 2026-03-22 `
  --end-date 2026-03-28 `
  --topic topics/document_ocr.toml
```

## Pipeline Contract

### 1. Ingest

Code:

- `src/paper_daily/stages/ingest.py`
- `src/paper_daily/arxiv_html.py`

Behavior:

- reads arXiv `list/<category>/pastweek?show=2000`
- parses announcement-page groupings
- stores raw per-category per-day snapshots under
  `data/raw/YYYY/week-<start>-to-<end>/YYYY-MM-DD/`

Important:

- day labels are **announcement dates**, not original submission dates
- this is intentional because the tracker is designed around "what appeared on arXiv that day"

### 2. Normalize

Code:

- `src/paper_daily/stages/normalize.py`

Behavior:

- merges same-day cross-category duplicates by `paper_id`
- fetches `abs/<id>` pages
- extracts title, abstract, authors, subjects, comments, submitted date
- writes canonical daily records to
  `data/normalized/YYYY/week-<start>-to-<end>/YYYY-MM-DD/papers.jsonl`

### 3. Recall

Code:

- `src/paper_daily/stages/recall.py`
- `topics/document_ocr.toml`

Behavior:

- reads normalized papers
- applies lexical prefilter first
- only sends `llm_candidate=true` papers to DeepSeek
- writes included papers to `data/topics/<topic-id>/daily/YYYY/week-<start>-to-<end>/YYYY-MM-DD.jsonl`

Current prefilter logic:

- strong lexical hits
- medium lexical hits
- contextual combinations such as `document + parsing`, `pdf + parsing`, `scientific paper + parsing`
- direct candidate fallback for `ocr`, `handwritten`, `scene text`

### 4. Weekly

Code:

- `src/paper_daily/stages/weekly.py`

Behavior:

- merges topic daily matches into one weekly bundle
- writes JSON and a human-readable Markdown inspection file

Outputs:

- `data/topics/<topic-id>/daily/YYYY/week-<start>-to-<end>/YYYY-MM-DD.jsonl`
- `data/topics/<topic-id>/weekly/YYYY/week-<start>-to-<end>.json`
- `data/topics/<topic-id>/weekly/YYYY/week-<start>-to-<end>.md`

## Current Verified Window

This repository has already been run successfully for:

- `2026-03-22` to `2026-03-28`

Produced artifacts:

- weekly JSON bundle:
  `data/topics/document_ocr/weekly/2026/week-2026-03-22-to-2026-03-28.json`
- weekly Markdown view:
  `data/topics/document_ocr/weekly/2026/week-2026-03-22-to-2026-03-28.md`

## Safe Places To Modify

- retrieval vocabulary: `topics/document_ocr.toml`
- retrieval policy and prompt: `src/paper_daily/stages/recall.py`
- source categories and runtime config: `config/arxiv.toml`

## Places To Be Careful

- `src/paper_daily/arxiv_html.py`
  arXiv list pages contain multiple `dl#articles` blocks, one per day
- `src/paper_daily/stages/recall.py`
  prefilter width strongly affects DeepSeek cost and runtime
- `data/`
  generated artifacts are useful reference outputs and should not be deleted casually

## Typical Agent Tasks

- rerun a new week window
- tighten or relax document/OCR recall
- add a second topic config under `topics/`
- add scheduled execution after the retrieval logic is stable
