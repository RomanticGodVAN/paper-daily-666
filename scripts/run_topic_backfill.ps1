param(
  [Parameter(Mandatory = $true)]
  [string]$StartDate,

  [Parameter(Mandatory = $true)]
  [string]$EndDate,

  [string]$Topic = "topics/document_ocr.toml",
  [string]$Source = "config/arxiv.toml"
)

if (-not $env:DEEPSEEK_API_KEY) {
  Write-Error "DEEPSEEK_API_KEY is not set."
  exit 1
}

$env:PYTHONPATH = "src"
python -m paper_daily.cli backfill-range --start-date $StartDate --end-date $EndDate --topic $Topic --source $Source
