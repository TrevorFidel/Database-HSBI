
"""Stretch Module 5's report table to ten quarters (2,000,000 rows)."""

import csv
import sqlite3
from pathlib import Path

# Define file locations
here = Path(__file__).parent
src = here.parent / "Module05" / "normalize.db"
db = here / "history.db"
csv_path = here / "report_jobpart.csv"

QUARTERS = 10

# Check that the Module 5 database exists
if not src.exists():
    raise SystemExit(
        "Module05/normalize.db is missing. "
        "Rebuild it using the Module 5 setup first."
    )

# Remove the previous generated database, if it exists
db.unlink(missing_ok=True)

# Connect to the new database
conn = sqlite3.connect(db)

# Decode existing Windows-1252 text correctly
conn.text_factory = lambda b: b.decode("cp1252")

# Attach the Module 5 database
conn.execute(
    "ATTACH DATABASE ? AS m5",
    (str(src),)
)

# Create the expanded history table
conn.execute("""
    CREATE TABLE report_history (
        job_id INTEGER,
        machine_id TEXT,
        site TEXT,
        technician TEXT,
        part_no TEXT,
        part_price REAL,
        done_on TEXT
    )
""")

# Create ten copies, each shifted forward by 91 days
conn.execute(f"""
    INSERT INTO report_history
    SELECT
        r.job_id + k * 1000000,
        r.machine_id,
        r.site,
        r.technician,
        r.part_no,
        r.part_price,
        date(r.done_on, '+' || (k * 91) || ' days')
    FROM m5.report_jobpart AS r,
         (
             WITH RECURSIVE n(k) AS (
                 SELECT 0
                 UNION ALL
                 SELECT k + 1
                 FROM n
                 WHERE k < {QUARTERS - 1}
             )
             SELECT k FROM n
         )
""")

conn.commit()

# Export the original Module 5 report table as UTF-8 CSV
with csv_path.open(
    "w",
    encoding="utf-8",
    newline=""
) as f:
    writer = csv.writer(f)

    writer.writerow([
        "job_id",
        "machine_id",
        "site",
        "technician",
        "part_no",
        "part_price",
        "done_on"
    ])

    writer.writerows(
        conn.execute("SELECT * FROM m5.report_jobpart")
    )

# Display results
row_count = conn.execute(
    "SELECT COUNT(*) FROM report_history"
).fetchone()[0]

print("history rows:", row_count)
print("csv bytes   :", csv_path.stat().st_size)

conn.close()
