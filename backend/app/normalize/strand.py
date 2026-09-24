from app.schemas import NormalizedSNPRecord, RawSNPRecord

COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def align_strand(record: RawSNPRecord, rsid: str) -> NormalizedSNPRecord:
    """Orient the genotype to the reference strand used by the panel."""
    raise NotImplementedError
