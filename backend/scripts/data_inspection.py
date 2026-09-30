import bz2
import json


PATH = "data/dbsnp/refsnp-merged.json.bz2"


with bz2.open(PATH, "rt") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        record = json.loads(line)

        print(json.dumps(record, indent=2))
        break