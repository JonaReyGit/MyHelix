from app.ingest.parsers.registry import detect_parser
from app.ingest.validation import validate_records
from app.schemas import RawSNPRecord


def ingest(data: bytes) -> list[RawSNPRecord]:
    text = data.decode("utf-8")
    parser = detect_parser(text)
    records = parser.parse(text)
    validate_records(records)
    return records
