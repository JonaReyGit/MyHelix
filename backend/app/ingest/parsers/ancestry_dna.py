from app.schemas import RawSNPRecord, Vendor


class AncestryDNAParser:
    vendor = Vendor.ANCESTRY_DNA

    def can_parse(self, text: str) -> bool:
        raise NotImplementedError

    def parse(self, text: str) -> list[RawSNPRecord]:
        raise NotImplementedError
