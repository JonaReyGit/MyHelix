import random
import zipfile
import requests
def resolve_rsid(rsid: str) -> str:
    """Map merged/retired rsIDs to their current canonical dbSNP ID."""
    raise NotImplementedError

    
def resolve_chain(
        rsid: str,
        merges: dict[str, str],
        cache: dict[str: str]
    ) -> str:

    if rsid in cache:
        return cache[rsid]

    path = []
    seen = set()
    current = rsid

    while current in merges:
        if current in cache:
            current = cache[current]
            break

        if current in seen:
            raise RuntimeError(
                f"Cycle detected in dbSNP merge chain starting at {rsid}"
            )

        seen.add(current)
        path.append(current)

        current = merges[current]

    for node in path:
        cache[node] = current

    return current