## Notes for Module06b

# Task 2 — The Shape

- Created a SQLite `device` table with JSON metadata and `CHECK (json_valid(meta))`.
- Used `json_extract()` and `json_each()` to query vendor metadata.
- Created an expression index on `json_extract(meta, '$.vendor')`.
- Compared two query plans: `json_extract()` used the index, while `->>` caused a table scan.
- **Takeaway:** JSON supports flexible vendor metadata, but queries must match the indexed expression to benefit from the index.

**Evidence:** `json_bench.py` and its two `EXPLAIN QUERY PLAN` outputs.

### Key-Value Benchmark

Tested 20,000 writes and 20,000 lookups using Shelve and SQLite.

- Shelve: write 35.862 s; lookup 0.267 s.
- SQLite: write 0.058 s; lookup 1.625 s.

**Takeaway:** SQLite performed much better for writes, while Shelve was faster for direct lookups. SQLite also supports SQL queries across sessions, which Shelve does not provide directly.