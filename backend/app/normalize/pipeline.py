from app.normalize.rsid_resolver import resolve_rsid
from app.normalize.strand import align_strand
from app.schemas import NormalizedSNPRecord, RawSNPRecord


def normalize(records: list[RawSNPRecord]) -> list[NormalizedSNPRecord]:
    normalized = [align_strand(r, resolve_rsid(r.rsid)) for r in records]
    return sorted(normalized, key=lambda r: r.rsid)
