# Module 6a — The Analytical Engine (DuckDB)

This module explores the difference between operational and analytical database workloads by moving historical reporting data from SQLite into Parquet and querying it with DuckDB.

## Learning Goals

- Export historical SQLite data into Parquet reproducibly.
- Compare SQLite and DuckDB analytical query performance.
- Interpret DuckDB `EXPLAIN ANALYZE` output.
- Identify when DuckDB is not the appropriate database engine.
- Recommend a strategy for analytical data refresh and validation.

## My Work and Evidence

| Task | Evidence | Description |
|---|---|---|
| Build historical dataset | `prepare.py` | Created a SQLite history database containing 2 million rows. |
| Export to Parquet | `export_parquet.py` | Exported the historical dataset and verified the row count. |
| Performance comparison | `benchmark.py` | Compared SQLite and DuckDB using seven interleaved runs. |
| Query plan analysis | `explain_plan.py`, `explain-output.txt` | Examined DuckDB operators and their execution times. |
| OLTP vs OLAP boundary | `boundary.py` | Compared individual inserts and lookups, including SQLite batch inserts. |
| Decision memo | `memo-to-lea-and-yasmin.md` | Recommended which workloads should remain in SQLite and move to DuckDB. |
| Compression comparison | `report_zstd.parquet`, `duckdb-notes.md` | Compared original and Zstandard Parquet file sizes. |

## Key Results

- The analytical query returned matching results in SQLite and DuckDB.
- SQLite median query time: 1,927.20 ms.
- DuckDB median query time: 20.52 ms.
- DuckDB was approximately 93.9 times faster for the tested analytical query.
- The original Parquet file was 1,441,430 bytes; the Zstandard copy was 1,438,857 bytes.
- Individual inserts and point lookups were substantially faster in SQLite than DuckDB in the boundary test.

## Key Takeaways

SQLite is suitable for operational workloads involving frequent individual transactions and point lookups. DuckDB is better suited to analytical workloads involving large scans, aggregations and historical reporting. Parquet provides a compact analytical copy, but its freshness must be managed through a reliable refresh and validation process.

## Navigation

- [Duckdb-notes](duckdb-notes.md) — Technical notes and task results.
- [memo-to-lea-and-Yasmin](memo-to-lea-and-yasmin.md) — Analytical database recommendation.
- [explain-output.txt](explain-output.txt) — Query execution plan evidence.
- [prepare.py](prepare.py) — Historical dataset preparation.
- [export_parquet.py](export_parquet.py) — Parquet export.
- [benchmark.py](benchmark.py) — SQLite and DuckDB performance comparison.
- [boundary.py](boundary.py) — OLTP versus OLAP boundary test.
  
**Module06a — Reflection:** [[ref06a](../Reflections/ref06a.md)]

**Previous Module — Module 05:** [[Module05](../Module05/README.md)]

**Next Module — Module 6b:** [[Module06](README.md)]
