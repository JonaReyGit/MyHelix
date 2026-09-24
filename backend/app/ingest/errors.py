class IngestError(Exception):
    """Raised for unrecognized, incomplete, or corrupted files. Never return a partial result."""
