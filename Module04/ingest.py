
import csv
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
DB = BASE / "edge.db"
CSV_FILE = BASE / "readings.csv"

UPSERT = """
INSERT INTO reading(sensor_id, ts, value, interval_s)
VALUES (?, ?, ?, ?)
ON CONFLICT(sensor_id, ts)
DO UPDATE SET value = excluded.value
"""

with sqlite3.connect(DB) as conn:
    conn.execute("PRAGMA foreign_keys = ON")

    with CSV_FILE.open(newline="", encoding="utf-8") as file:
        rows = [
            (
                int(row["sensor_id"]),
                row["ts"],
                float(row["value"]),
                int(row["interval_s"])
            )
            for row in csv.DictReader(file)
        ]

    conn.executemany(UPSERT, rows)

    count = conn.execute(
        "SELECT COUNT(*) FROM reading"
    ).fetchone()[0]

    print(f"Processed {len(rows)} rows")
    print(f"Total readings in database: {count}")
