from fastapi import APIRouter, HTTPException, UploadFile

from app.core.config import settings
from app.ingest import IngestError, ingest
from app.normalize import normalize
from app.panel import match_panel
from app.reporting import build_report
from app.schemas import Report

router = APIRouter()

PANEL_VERSION = "0.0.0"


@router.post("/upload", response_model=Report)
async def upload(file: UploadFile) -> Report:
    data = await file.read(settings.max_upload_bytes + 1)
    if len(data) > settings.max_upload_bytes:
        raise HTTPException(status_code=413, detail="File too large")

    # Processed in memory and returned directly; nothing about the upload is persisted.
    try:
        raw = ingest(data)
    except (IngestError, UnicodeDecodeError) as e:
        raise HTTPException(status_code=422, detail=str(e)) from e

    findings = match_panel(normalize(raw))
    return build_report(raw[0].vendor, findings, PANEL_VERSION)
