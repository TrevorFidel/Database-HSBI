
from pathlib import Path
import duckdb

BASE_DIR = Path(__file__).resolve().parent
PARQUET_FILE = BASE_DIR / "report_history.parquet"
OUTPUT_FILE = BASE_DIR / "explain-output.txt"

parquet_path = str(PARQUET_FILE).replace("\\", "/").replace("'", "''")

con = duckdb.connect()

try:
    query = f"""
        EXPLAIN ANALYZE
        SELECT
            site,
            COUNT(*) AS job_parts,
            ROUND(SUM(part_price), 2) AS total_value
        FROM read_parquet('{parquet_path}')
        GROUP BY site
        ORDER BY site
    """

    result = con.execute(query).fetchall()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("DUCKDB EXPLAIN ANALYZE\n")
        f.write("======================\n\n")

        for row in result:
            f.write(str(row[1]))
            f.write("\n\n")

    print(f"Complete query plan saved to: {OUTPUT_FILE}")

finally:
    con.close()
