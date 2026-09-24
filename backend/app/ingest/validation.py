import re

from app.ingest.errors import IngestError
from app.schemas import RawSNPRecord

VALID_CHROMOSOMES = {str(n) for n in range(1, 23)} | {"X", "Y", "MT"}
# A/C/G/T bases, D/I for deletion/insertion calls, "-" for no-call; 1 char on haploid X/Y/MT.
GENOTYPE_PATTERN = re.compile(r"^[ACGTDI-]{1,2}$")


def validate_records(records: list[RawSNPRecord]) -> None:
    """Raise IngestError if the parsed file looks incomplete or corrupted."""
    if not records:
        raise IngestError("File contains no genotype records")

    seen: set[str] = set()
    for r in records:
        if r.chromosome not in VALID_CHROMOSOMES:
            raise IngestError(f"{r.rsid}: invalid chromosome '{r.chromosome}'")
        if not GENOTYPE_PATTERN.match(r.genotype):
            raise IngestError(f"{r.rsid}: invalid genotype '{r.genotype}'")
        if r.rsid in seen:
            raise IngestError(f"{r.rsid}: duplicate marker")
        seen.add(r.rsid)
