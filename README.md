# Paper Daily

`paper-daily` is a working prototype for one core task:

- ingest broad arXiv computer-science announcements
- normalize and deduplicate paper metadata
- use an LLM to recall topic-relevant papers from title + abstract
- materialize a weekly bundle of relevant papers

The current repository stops at **weekly relevant paper bundles**.
It does not attempt final report writing, GitHub Pages publishing, or WeChat posting.

## Current Prototype

The current implementation is built around four stages:

1. `ingest`
   Reads arXiv `list/<category>/pastweek` pages for rolling current-week runs.
   Historical backfill uses arXiv OAI-PMH over `set=cs`, then filters locally.
2. `normalize`
   Fetches per-paper `abs/<id>` pages, extracts abstract-level metadata, and deduplicates across categories.
3. `recall`
   Uses a high-recall lexical prefilter plus DeepSeek-based abstract screening for the target topic.
4. `weekly`
   Merges daily matches into a rolling 7-day bundle and exports both JSON and Markdown.

Important:

- the current ingestion source is based on **arXiv announcement pages**
- day labels in `data/raw/`, `data/normalized/`, and `data/topics/.../daily/` are therefore **announcement dates**
- this matches "what appeared on arXiv that day" better than original submission timestamps
- `backfill-range` is the exception: it uses arXiv OAI-PMH and groups by **created date**
- weekly backfill bundles also apply a modern arXiv ID/month guard to drop papers whose numeric ID prefix does not match the requested month window

## Repository Layout

```text
config/                    Global source config
data/raw/                  Raw per-day announcement snapshots
data/normalized/           Canonical per-day papers with abstracts
data/state/                Run logs and manifests
data/topics/               Topic daily matches and weekly bundles
docs/design/               Design notes
src/paper_daily/           Python package
src/paper_daily/stages/    ingest / normalize / recall / weekly
topics/                    Topic configs
```

## Configs

- global source config: [`config/arxiv.toml`](config/arxiv.toml)
- first topic config: [`topics/document_ocr.toml`](topics/document_ocr.toml)

The first topic is `Document AI and OCR`.

## Commands

Agent handoff notes are in [`AGENTS.md`](AGENTS.md).

Show configs:

```powershell
$env:PYTHONPATH = "src"
python -m paper_daily.cli show-source config/arxiv.toml
python -m paper_daily.cli show-topic topics/document_ocr.toml
```

Run one rolling week window:

```powershell
$env:PYTHONPATH = "src"
$env:DEEPSEEK_API_KEY = "your-key"
python -m paper_daily.cli run-window `
  --start-date 2026-03-22 `
  --end-date 2026-03-28 `
  --topic topics/document_ocr.toml
```

Or use the wrapper script:

```powershell
$env:DEEPSEEK_API_KEY = "your-key"
.\scripts\run_topic_week.ps1 -StartDate 2026-03-22 -EndDate 2026-03-28
```

Backfill a longer range and emit one weekly bundle per calendar week slice:

```powershell
$env:DEEPSEEK_API_KEY = "your-key"
.\scripts\run_topic_backfill.ps1 -StartDate 2026-01-01 -EndDate 2026-03-29
```

Backfill notes:

- source: arXiv OAI-PMH (`oaipmh.arxiv.org/oai`)
- harvest scope: `set=cs`, then local filtering to configured categories
- date semantics: created-date based, not announcement-page based
- weekly outputs apply an additional modern arXiv ID/month consistency guard

You can also run stages separately:

```powershell
$env:PYTHONPATH = "src"
python -m paper_daily.cli ingest-window --start-date 2026-03-22 --end-date 2026-03-28
python -m paper_daily.cli normalize-window --start-date 2026-03-22 --end-date 2026-03-28
$env:DEEPSEEK_API_KEY = "your-key"
python -m paper_daily.cli recall-window --start-date 2026-03-22 --end-date 2026-03-28 --topic topics/document_ocr.toml
python -m paper_daily.cli weekly-window --start-date 2026-03-22 --end-date 2026-03-28 --topic topics/document_ocr.toml
```

Or use the range backfill command directly:

```powershell
$env:PYTHONPATH = "src"
$env:DEEPSEEK_API_KEY = "your-key"
python -m paper_daily.cli backfill-range `
  --start-date 2026-01-01 `
  --end-date 2026-03-29 `
  --topic topics/document_ocr.toml
```

## Output Contract

The current prototype materializes these artifacts:

- `data/raw/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD/YYYY-MM-DD/arxiv-list.<category>.json`
- `data/normalized/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD/YYYY-MM-DD/papers.jsonl`
- `data/topics/<topic-id>/daily/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD/YYYY-MM-DD.jsonl`
- `data/topics/<topic-id>/weekly/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD.json`
- `data/topics/<topic-id>/weekly/YYYY/week-YYYY-MM-DD-to-YYYY-MM-DD.md`

The weekly JSON bundle is the machine-readable output.
The weekly Markdown file is only a convenient inspection view.

## Verified Example

The repository has been run on the rolling window:

- `2026-03-22` to `2026-03-28`

For topic `document_ocr`, the prototype produced:

- raw entries: `3445`
- normalized unique papers: `2480`
- LLM-screened candidates: `111`
- final included weekly papers: `28`
