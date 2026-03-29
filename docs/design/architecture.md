# Architecture

## Goal

Build a topic-tracking research system that:

- monitors selected arXiv categories continuously
- keeps complete and replayable historical records
- recalls papers for one or more configured topics
- materializes deduplicated weekly candidate sets

This repository currently stops at the weekly candidate layer.
Human-facing report generation is intentionally out of scope for now.

## Core Design Decision

The system is split into layers so that each layer can be improved without
rewriting the rest of the repository.

1. Source ingestion
2. Normalization
3. Topic recall
4. Weekly materialization

This keeps "coverage" and "quality" separate:

- ingestion solves "do not miss papers"
- normalization solves "remove duplicates and build canonical records"
- recall solves "find candidate papers for a topic"
- weekly materialization solves "produce a stable, queryable weekly bundle"

## Layer Contracts

### 1. Source Ingestion

Input:

- arXiv category feeds or APIs
- target date
- configured source categories

Output:

- immutable daily snapshots under `data/raw/YYYY-MM-DD/`
- run metadata under `data/state/`

Rules:

- reruns for the same day must be safe
- the raw layer should preserve enough data for downstream reprocessing
- topic logic must not be embedded in this layer

### 2. Normalization

Input:

- raw daily snapshots

Output:

- canonical daily paper sets under `data/normalized/YYYY-MM-DD/`

Rules:

- deduplicate across source categories
- preserve source provenance for each paper
- keep canonical IDs stable across reruns

### 3. Topic Recall

Input:

- normalized paper records
- topic config from `topics/*.toml`

Output:

- daily topic matches under `data/topics/<topic-id>/daily/`

Rules:

- recall must be config-driven
- the first version works on title + abstract only
- a later version can add embeddings, search APIs, or full-text signals

### 4. Weekly Materialization

Input:

- topic daily matches

Output:

- deduplicated weekly bundles under `data/topics/<topic-id>/weekly/`

Rules:

- a weekly bundle is the end product of the current repository scope
- bundles must preserve paper metadata, match evidence, and first-seen dates
- rerunning a week should regenerate deterministically from stored daily data

## Storage Layout

```text
data/
  raw/
    YYYY-MM-DD/
      source-snapshot.json
  normalized/
    YYYY-MM-DD/
      papers.jsonl
  state/
    runs.jsonl
    manifests/
  topics/
    <topic-id>/
      daily/
        YYYY/
          week-YYYY-MM-DD-to-YYYY-MM-DD/
            YYYY-MM-DD.jsonl
      weekly/
        YYYY/
          week-YYYY-MM-DD-to-YYYY-MM-DD.json
```

## Config Contracts

### Global Source Config

`config/arxiv.toml` defines:

- monitored source categories
- timezone and week boundary
- storage roots
- normalization policy

### Topic Config

The first topic is `document_ocr`.

Its config defines:

- human-readable name
- strong and medium recall terms
- exclusion terms
- score threshold
- optional weekly materialization policy

This allows future topic expansion without changing code structure.

## Incremental Roadmap

### Phase 0

- finalize repository layout
- define config format
- keep only lightweight CLI validation

### Phase 1

- implement arXiv ingestion by date
- write immutable raw snapshots
- add run manifests and idempotency checks

### Phase 2

- implement canonical paper normalization
- deduplicate papers across configured source categories
- preserve provenance and first-seen metadata

### Phase 3

- implement keyword-based candidate recall
- store topic daily archives
- validate precision/recall manually on the first topic

### Phase 4

- materialize weekly bundles
- ensure deterministic weekly regeneration
- verify historical backfill behavior

## Future Extension Points

- later report generation can consume weekly bundles without changing upstream layers
- alternative retrieval strategies can be added without changing raw ingestion
- multiple topics can share the same raw snapshots and run metadata
