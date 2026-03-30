#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

TOPIC_CONFIG="${TOPIC_CONFIG:-topics/document_ocr.toml}"
EXPORT_ROOT="${EXPORT_ROOT:-document_ocr}"
RUN_DATE="${RUN_DATE:-$(date -u +%F)}"

if [[ -z "${DEEPSEEK_API_KEY:-}" ]]; then
  echo "DEEPSEEK_API_KEY is required" >&2
  exit 1
fi

PYTHON_BIN="${PYTHON_BIN:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  if command -v python3.13 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3.13)"
  elif command -v python3.12 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3.12)"
  elif command -v python3.11 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3.11)"
  else
    echo "Python 3.11+ is required" >&2
    exit 1
  fi
fi

if [[ ! -d .venv ]]; then
  "$PYTHON_BIN" -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel >/dev/null
pip install -e . >/dev/null
export PYTHONPATH=src

python -m paper_daily.cli run-window \
  --start-date "$RUN_DATE" \
  --end-date "$RUN_DATE" \
  --topic "$TOPIC_CONFIG"

python -m paper_daily.cli daily-export \
  --date "$RUN_DATE" \
  --topic "$TOPIC_CONFIG" \
  --export-root "$EXPORT_ROOT"
