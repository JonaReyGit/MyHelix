from pathlib import Path
from urllib.request import urlretrieve

URL = ("https://ftp.ncbi.nih.gov/snp/latest_release/JSON/refsnp-merged.json.bz2")

OUTPUT = Path("data/dbsnp/refsnp-merged.json.bz2")

def download():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if OUTPUT.exists():
        print(f"{OUTPUT} already exists")
        return

    print(f"Downloading {URL}")
    urlretrieve(URL, OUTPUT)

    print(f"Downloaded to {OUTPUT}")



if __name__ == "__main__":
    download()