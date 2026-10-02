from app.schemas import Finding, NormalizedSNPRecord


def match_panel(records: list[NormalizedSNPRecord]) -> list[Finding]:
    """Match normalized genotypes against the curated panel and attach evidence tiers."""
    raise NotImplementedError
