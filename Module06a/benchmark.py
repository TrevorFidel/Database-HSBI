
from pathlib import Path
import sqlite3
import statistics
import time
import duckdb

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DB = BASE_DIR / "history.db"
PARQUET_FILE = BASE_DIR / "report_history.parquet"

QUERY = """
SELECT
    site,
    COUNT(*) AS job_parts,
    ROUND(SUM(part_price), 2) AS total_value
FROM report_history
GROUP BY site
ORDER BY site
"""

RUNS = 7

sqlite_conn = sqlite3.connect(SQLITE_DB)
sqlite_conn.text_factory = lambda b: b.decode("cp1252")
duck_conn = duckdb.connect()

# Use a safely quoted, locally generated file path.
parquet_path = str(PARQUET_FILE).replace("\\", "/").replace("'", "''")

duck_conn.execute(
    f"""
    CREATE VIEW report_history AS
    SELECT * FROM read_parquet('{parquet_path}')
    """
)

def timed_query(connection):
    start = time.perf_counter()
    rows = connection.execute(QUERY).fetchall()
    elapsed_ms = (time.perf_counter() - start) * 1000
    return elapsed_ms, rows

sqlite_times = []
duck_times = []

try:
    for run in range(RUNS):
        if run % 2 == 0:
            sqlite_ms, sqlite_rows = timed_query(sqlite_conn)
            duck_ms, duck_rows = timed_query(duck_conn)
        else:
            duck_ms, duck_rows = timed_query(duck_conn)
            sqlite_ms, sqlite_rows = timed_query(sqlite_conn)

        if sqlite_rows != duck_rows:
            raise ValueError("SQLite and DuckDB results do not match!")

        sqlite_times.append(sqlite_ms)
        duck_times.append(duck_ms)

        print(
            f"Run {run + 1}: "
            f"SQLite {sqlite_ms:.2f} ms | "
            f"DuckDB {duck_ms:.2f} ms"
        )

    print("\nMEDIAN RESULTS")
    print(f"SQLite median: {statistics.median(sqlite_times):.2f} ms")
    print(f"DuckDB median: {statistics.median(duck_times):.2f} ms")
    print(f"Result groups: {len(sqlite_rows)}")
    print("Result check: SQLite and DuckDB match")

finally:
    sqlite_conn.close()
    duck_conn.close()
