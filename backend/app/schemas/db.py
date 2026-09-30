import psycopg2 
from psycopg2.extras import execute_values
import os

def insert_rsid_aliases(aliases: list[tuple[str, str]]):
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    try:
        with conn.cursor as cur:
            execute_values(
                cur,
                 """
                INSERT INTO rsid_alias (
                    alias_rsid,
                    canonical_rsid
                )
                VALUES %s
                ON CONFLICT (alias_rsid)
                DO UPDATE SET
                    canonical_rsid = EXCLUDED.canonical_rsid
                """,
                aliases,
                page_size=10_000,
            )
        conn.commit()
    finally:
        conn.close()