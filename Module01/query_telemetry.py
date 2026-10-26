"""Run the shop manager's telemetry queries."""

import sqlite3
import time
from pathlib import Path

db_path = Path(__file__).with_name("telemetry.db")

queries = [
    (
        "1. Readings per machine",
        """
        SELECT machine, COUNT(*) AS n
        FROM readings
        GROUP BY machine
        ORDER BY machine;
        """,
    ),
    (
        "2. Peak vibration per machine",
        """
        SELECT machine, MAX(vib_rms) AS peak_vib
        FROM readings
        GROUP BY machine
        ORDER BY machine;
        """,
    ),
    (
        "3. Readings exceeding the 2.0 mm/s alarm",
        """
        SELECT COUNT(*) AS alarm_readings
        FROM readings
        WHERE vib_rms > 2.0;
        """,
    ),
]

with sqlite3.connect(db_path) as conn:
    for title, sql in queries:
        start = time.perf_counter()
        rows = conn.execute(sql).fetchall()
        elapsed = time.perf_counter() - start

        print(f"\n{title}")
        print("-" * len(title))

        for row in rows:
            print(*row, sep=" | ")

        print(f"Elapsed time: {elapsed:.6f} seconds")