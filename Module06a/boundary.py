
import sqlite3
import duckdb
import time

N = 1000
rows = [(i, f"key_{i}", float(i)) for i in range(N)]


def measure_individual_inserts(connection, engine):
    start = time.perf_counter()

    for row in rows:
        connection.execute(
            "INSERT INTO s VALUES (?, ?, ?)",
            row
        )

    elapsed = (time.perf_counter() - start) * 1000
    print(f"{engine} individual inserts: {elapsed:.2f} ms")


def measure_lookups(connection, engine):
    start = time.perf_counter()

    for i in range(N):
        connection.execute(
            "SELECT * FROM s WHERE id = ?",
            (i,)
        ).fetchone()

    elapsed = (time.perf_counter() - start) * 1000
    print(f"{engine} individual lookups: {elapsed:.2f} ms")


def measure_batch_inserts(connection):
    start = time.perf_counter()

    connection.executemany(
        "INSERT INTO s VALUES (?, ?, ?)",
        rows
    )

    elapsed = (time.perf_counter() - start) * 1000
    print(f"SQLite executemany inserts: {elapsed:.2f} ms")


# SQLite in-memory database
sqlite_conn = sqlite3.connect(":memory:")
sqlite_conn.execute(
    "CREATE TABLE s (id INTEGER PRIMARY KEY, k TEXT, v REAL)"
)

measure_individual_inserts(sqlite_conn, "SQLite")
measure_lookups(sqlite_conn, "SQLite")

# DuckDB in-memory database
duck_conn = duckdb.connect(":memory:")
duck_conn.execute(
    "CREATE TABLE s (id INTEGER PRIMARY KEY, k TEXT, v DOUBLE)"
)

measure_individual_inserts(duck_conn, "DuckDB")
measure_lookups(duck_conn, "DuckDB")

# SQLite batch insert comparison
batch_conn = sqlite3.connect(":memory:")
batch_conn.execute(
    "CREATE TABLE s (id INTEGER PRIMARY KEY, k TEXT, v REAL)"
)

measure_batch_inserts(batch_conn)

sqlite_conn.close()
duck_conn.close()
batch_conn.close()
