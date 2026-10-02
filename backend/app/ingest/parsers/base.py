from typing import Protocol

from app.schemas import RawSNPRecord, Vendor


class Parser(Protocol):
    vendor: Vendor

    def can_parse(self, text: str) -> bool:
        """Cheap header sniff — must not parse the whole file."""
        ...

    def parse(self, text: str) -> list[RawSNPRecord]: ...
