# Module 06b — Kortmann's Decision Record

| Workload | Engine | Why | Evidence | Cost accepted |
|---|---|---|---|---|
| Month-end reporting | Parquet + DuckDB | Faster analytical queries without blocking operational writes. | Module 06a: SQLite 1,927.20 ms; DuckDB 20.52 ms. | Scheduled exports and possible data staleness. |
| Sensor/job ingest | SQLite | Supports transactions, constraints and idempotent UPSERT operations. | Module 4: UPSERT and repeated-ingest test. | Local database and backup maintenance. |
| Vendor metadata | SQLite with JSON | Flexible metadata without repeated schema changes. | Module 06b Task 2: JSON validation and expression-index query plans. | Less convenient typing and joins on JSON fields. |
| Dashboard session state | Pending benchmark | Direct key-based lookups suit a key-value access pattern. | `kv_compare.py`: pending. | Pending benchmark. |
| Concurrent network users (optional) | PostgreSQL | Supports shared access from multiple network clients. | Module 06b Task 1: pending observations. | Server and network availability dependency. |

## Defence Notes

The other pod discussed my engine choices and the trade-offs involved. Their feedback helped me review my decisions.

## If Kortmann could Run Only One Engine: 

I would choose SQLite because it supports reliable operational storage, transactions, constraints and flexible JSON metadata. The two-year analytical report would be the first workload to suffer because SQLite was approximately 94 times slower than DuckDB in my Module 06a benchmark. Shared network access would also be more difficult.