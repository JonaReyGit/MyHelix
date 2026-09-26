# MyHelix backend

FastAPI service that runs the Ingest → Normalize → Look up → Report pipeline.

## Setup

```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload   # http://localhost:8000/docs
pytest
```

## Layout

| Module | Stage | Owner |
|---|---|---|
| `app/ingest/` | Parse + validate vendor files → `RawSNPRecord` | Victor |
| `app/normalize/` | rsID resolution + strand alignment → `NormalizedSNPRecord` | Victor |
| `app/panel/` | Panel schema, tier model, matching → `Finding` | Jonathan |
| `app/reporting/` | Group findings by domain, PDF export → `Report` | Neil |
| `app/schemas/contracts.py` | Shared stage contracts — change only via reviewed PR | All |

Adding a vendor: implement the `Parser` protocol in `app/ingest/parsers/` and register it in `registry.py`.

Uploads are processed in memory and never persisted. Only curated panel data belongs in the database.
