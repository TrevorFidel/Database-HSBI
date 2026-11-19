### Task 3 — Benchmark: SQLite vs DuckDB

I compared the same aggregate query against the 2,000,000-row history dataset using seven interleaved runs.

| Measurement | SQLite | DuckDB |
|---|---:|---:|
| Median query time | 1,927.20 ms | 20.52 ms |
| Result groups | 2 | 2 |

**Result:** DuckDB was approximately 93.9 times faster in this benchmark. Both engines returned matching query results.

This supports using DuckDB for large analytical aggregations while keeping SQLite for operational workloads. The result applies to this specific query and test environment; it should not be generalized to every workload.


### Task 4 — Query Plan Analysis

I used DuckDB's `EXPLAIN ANALYZE` to inspect the aggregate query over the 2-million-row Parquet dataset.

**Execution plan findings:**

| Operator | Rows | Reported time |
|---|---:|---:|
| Table Scan (`READ_PARQUET`) | 2,000,000 | 40 ms |
| Hash Group By | 2 | 70 ms |
| Projection | 2,000,000 | 0 µs |
| Projection | 2 | 0 µs |
| Order By | 2 | 0 µs |

The `HASH_GROUP_BY` operator was the most expensive reported operator at 70 ms. It grouped two million records by `site` and calculated the row count and total part price.

The Parquet scan read all 17 of 17 row groups, processing two million rows. This shows that the query required a full scan rather than reading only a small subset of the dataset.

DuckDB reported a total execution time of 0.0290 seconds. Operator timings are not additive, so they should not be summed to calculate total query time.

**Interpretation:** The aggregation and full dataset scan account for the main work in this analytical query. DuckDB handles this workload efficiently through columnar Parquet reading and vectorized aggregation.

### Task 5 — Boundary Test: OLTP vs OLAP

I compared SQLite and DuckDB using 1,000 individual inserts and 1,000 individual point lookups in in-memory databases.

| Operation | SQLite | DuckDB |
|---|---:|---:|
| Individual inserts | 2.93 ms | 2673.83 ms |
| Individual lookups | 4.04 ms | 2333.90 ms |
| SQLite `executemany` inserts | 1.80 ms | — |

SQLite performed substantially better for individual transactions. DuckDB took approximately 912 times longer for individual inserts and 578 times longer for individual lookups in this test. Using SQLite's `executemany` reduced insert time from 2.93 ms to 1.80 ms.

The results illustrate the difference between OLTP and OLAP workloads. SQLite is better suited to frequent individual writes and point lookups, while DuckDB is designed for analytical queries that process large volumes of data in batches.

**Engine boundary:** For Kortmann, DuckDB is the wrong engine when an application needs frequent individual inserts and point lookups, as demonstrated by its 2673.83 ms insert time and 2333.90 ms lookup time compared with SQLite's 2.93 ms and 4.04 ms.

### Task 6 — Decision: What belongs in SQLite and DuckDB?

The benchmark results support separating operational and analytical workloads.

**Keep in SQLite (OLTP):**
- Frequent individual inserts and updates.
- Point lookups of individual operational records.
- Transactions that need to update the operational database immediately.

**Move to DuckDB and Parquet (OLAP):**
- Historical reporting across large datasets.
- Monthly aggregations and summary reports.
- Analytical queries that scan and aggregate many rows.

The seven-run benchmark on 2 million rows returned matching results. SQLite had a median query time of 1,927.20 ms, while DuckDB had a median of 20.52 ms. DuckDB was approximately 93.9 times faster for this analytical query.

**Storage comparison:**

| File | Size |
|---|---:|
| `history.db` | 106 MB |
| `report_history.parquet` | 1,441,430 bytes (approximately 1.4 MB) |

These figures compare the complete SQLite database with the exported analytical table, not identical contents.

**Refresh recommendation:**

I recommend an automated nightly refresh after the operational shift. The refresh process should verify the Parquet row count and the sum of `part_price` against SQLite, record the last successful refresh timestamp, and alert the responsible database or IT operations team if validation fails.

If the refresh silently stops, the report may still run quickly but display incomplete or outdated information. Therefore, freshness monitoring is as important as query performance.

### Task 7 — Zstandard compression

I created a second Parquet file using Zstandard compression.

| File | Exact size |
|---|---:|
| `report_history.parquet` | 1,441,430 bytes |
| `report_zstd.parquet` | 1,438,857 bytes |
| Difference | 2,573 bytes |

Zstandard reduced the file size by approximately 0.18%. The improvement was small for this dataset, but the compressed copy was successfully created.

**Refresh and failure considerations:**

The analytical copy should be refreshed automatically after the operational shift or on a scheduled nightly basis. The refresh process should compare row counts and financial totals with SQLite, record its completion time, and alert the responsible team if it fails. If the process stops without detection, users may receive outdated month-end figures even though the analytical query runs successfully. A freshness check and visible last-refresh timestamp help prevent this silent failure.