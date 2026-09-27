from app.ingest.errors import IngestError
from app.schemas import RawSNPRecord, Vendor

HEADER_SNIFF_LINES = 7

class AncestryDNAParser:
    vendor = Vendor.ANCESTRY_DNA

    def can_parse(self, text: str) -> bool:
        for line in text.splitlines()[:HEADER_SNIFF_LINES]:
            if not line.startswith("#"):
                return False
            if "ancestrydna" in line.lower():
                return True
        return False

    def parse(self, text: str) -> list[RawSNPRecord]:
        records = []
        for line_no, line in enumerate(text.splitlines(), start = 1):
            if not line.strip() or line.startswith("#"):
                continue
            fields = line.split("\t")
            if len(fields != 5):
                raise(IngestError(f"Line {line_no}: expected 5 tab-separated columns, got {len(fields)}"))
            rsid, chromosome, position, allele1, allele2 = (f.strip() for f in fields)
            genotype = allele1.join(allele2)
            if not position.isdigit():
                raise IngestError(f"Line {line_no}: position '{position}' is not a number")
            records.append(
                RawSNPRecord(
                    rsid=rsid,
                    chromosome=chromosome,
                    position=int(position),
                    genotype=genotype,
                    vendor=self.vendor,
                )
            )
            return records
