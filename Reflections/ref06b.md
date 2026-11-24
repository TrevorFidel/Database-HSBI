# Reflection 06b — Polyglot Persistence & the Decision

## Take-away
Different database engines suit different workloads. SQLite is useful for operational data, while DuckDB and Parquet are better suited to analytical reporting. JSON also provides flexibility for changing vendor metadata.

## What was good?
Comparing Shelve and SQLite was useful. SQLite was much faster for writes, while Shelve performed faster for individual lookups.

## What was difficult?
Understanding why an expression index works with `json_extract()` but not with the alternative `->>` expression required careful comparison of the query plans.

## Exploration and show stoppers
I explored JSON storage, expression indexes, and key-value access patterns. The benchmark showed that performance depends on the operation being measured.

## How did I verify AI suggestions?
I ran the Python scripts and checked the actual query plans and benchmark timings rather than relying only on suggested results.

## Help and extra work
I used Python scripts to compare storage approaches and documented the results in my portfolio. 