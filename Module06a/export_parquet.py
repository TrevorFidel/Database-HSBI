
from pathlib import Path
import sqlite3
import csv
import duckdb

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "history.db"
CSV_PATH = BASE_DIR / "report_history_utf8.csv"
PARQUET_PATH = BASE_DIR / "report_history.parquet"

# Export all 2 million rows from SQLite, decoding legacy text as CP1252.
source = sqlite3.connect(DB_PATH)
source.text_factory = lambda b: b.decode("cp1252")

try:
    cursor = source.execute("""
        SELECT job_id, machine_id, site, technician,
               part_no, part_price, done_on
        FROM report_history
    """)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "job_id", "machine_id", "site", "technician",
            "part_no", "part_price", "done_on"
        ])
        writer.writerows(cursor)

finally:
    source.close()

# Convert the clean UTF-8 CSV to Parquet.
con = duckdb.connect()

try:
    csv_path = str(CSV_PATH).replace("\\", "/").replace("'", "''")
    parquet_path = str(PARQUET_PATH).replace("\\", "/").replace("'", "''")

    con.execute(f"""
        COPY (
            SELECT * FROM read_csv(
                '{csv_path}',
                header = true,
                encoding = 'utf-8',
                auto_detect = true
            )
        )
        TO '{parquet_path}'
        (FORMAT PARQUET, COMPRESSION ZSTD)
    """)

    count = con.execute(
        f"SELECT COUNT(*) FROM read_parquet('{parquet_path}')"
    ).fetchone()[0]

    print(f"Parquet rows: {count:,}")
    print(f"Parquet file: {PARQUET_PATH}")

finally:
    con.close()
