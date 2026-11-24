
"""Compare key-value access using shelve and SQLite."""

import shelve
import sqlite3
import time
from pathlib import Path

here = Path(__file__).parent
N = 20_000

# Test shelve
with shelve.open(str(here / "sessions")) as db:
    t0 = time.perf_counter()
    for i in range(N):
        db[f"session-{i}"] = f"user-{i % 100}:filter=city:{i % 4}"
    t_set = time.perf_counter() - t0

    t0 = time.perf_counter()
    for i in range(N):
        _ = db[f"session-{i}"]
    t_get = time.perf_counter() - t0

# Test SQLite
conn = sqlite3.connect(here / "sessions.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS session (k TEXT PRIMARY KEY, v TEXT)"
)
conn.execute("DELETE FROM session")

t0 = time.perf_counter()
conn.executemany(
    "INSERT OR REPLACE INTO session(k, v) VALUES (?, ?)",
    (
        (f"session-{i}", f"user-{i % 100}:filter=city:{i % 4}")
        for i in range(N)
    ),
)
conn.commit()
sq_set = time.perf_counter() - t0

t0 = time.perf_counter()
for i in range(N):
    conn.execute(
        "SELECT v FROM session WHERE k = ?",
        (f"session-{i}",),
    ).fetchone()
sq_get = time.perf_counter() - t0

print(f"shelve  set={t_set:8.3f}s get={t_get:8.3f}s")
print(f"sqlite  set={sq_set:8.3f}s get={sq_get:8.3f}s")

conn.close()

