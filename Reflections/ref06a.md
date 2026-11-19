# Reflection 06a — The Analytical Engine (DuckDB)

## Take-away

I learned that SQLite and DuckDB are designed for different workloads. SQLite performed much better for individual inserts and point lookups, while DuckDB was substantially faster for analytical queries over 2 million rows. I also learned how Parquet provides a compact format for storing analytical data separately from an operational database, and why keeping that copy fresh is important.

## What was good?

Building the 2-million-row history database and exporting it to Parquet helped me understand the analytical data workflow in practice. I enjoyed comparing the same aggregate query in SQLite and DuckDB. DuckDB achieved a median execution time of 20.52 ms compared with SQLite's 1,927.20 ms, and both engines returned matching results. The boundary test was also useful because it demonstrated the opposite performance result for individual transactions.

## What was difficult?

The CSV character encoding caused some difficulties during the export process. The original SQLite data contained CP1252 text, which caused UTF-8 decoding errors when working with DuckDB and Parquet. I addressed this by decoding the source text as CP1252 and exporting it as UTF-8. I also had to troubleshoot DuckDB's prepared parameter limitation when creating a view over the Parquet file. Understanding the differences between analytical and operational workloads required comparing several measurements rather than relying on one benchmark.

## Exploration and show stoppers

I explored SQLite-to-Parquet export, DuckDB analytical queries, query execution plans and Zstandard compression. The `EXPLAIN ANALYZE` output identified the `HASH_GROUP_BY` operator as the largest reported time contributor, at 110 ms in the recorded plan. The Parquet file contained 2 million rows and occupied 1,441,430 bytes. The Zstandard version occupied 1,438,857 bytes, a reduction of approximately 0.18%. The boundary test also showed that SQLite handled individual inserts and lookups much faster than DuckDB.

## Interaction with peers and instructors

I have not recorded specific peer or instructor interactions for this module in my evidence. My main focus was completing the practical database experiments, troubleshooting the export process and documenting the results.

## How did you verify AI suggestions?

I ran the Python scripts and SQL queries locally and checked the actual command outputs. I verified that the SQLite history database and Parquet file both contained 2 million rows. I compared the analytical query results from SQLite and DuckDB to confirm that they matched, and used seven interleaved runs to calculate median execution times. I also inspected the DuckDB execution plan and measured the exact file sizes of the original and Zstandard Parquet files. For the boundary test, I recorded the actual insert and lookup timings rather than relying on expected performance figures.

## Help and extra work

AI helped me write and troubleshoot the Python scripts, understand the differences between SQLite and DuckDB, interpret the query plan and organize the benchmark evidence. I also explored Zstandard compression and compared its actual file size with the original Parquet file. The refresh strategy was documented as a recommendation; I did not implement the optional automated refresh process in this core work.