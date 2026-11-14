# Reflection 05 — Normalization vs. Denormalization

## Take-away

I learned how normalization reduces data duplication and prevents update, insert and delete anomalies. I also learned that denormalization can improve reporting queries, but it increases storage and write costs. DuckDB showed how a columnar database can perform analytical queries very quickly.

## What was good?

Building the normalized tables and comparing them with the denormalized reporting table helped me understand the differences in practice. I also enjoyed testing the same dashboard query in DuckDB and comparing the results.

## What was difficult?

Understanding functional dependencies and choosing the candidate key was challenging at first. I also had some difficulty exporting and importing the CSV because of its character encoding. Comparing query times was another challenge because the measurements were only single runs.

## Exploration and show stoppers

I explored SQLite query plans, indexes, storage measurements with `dbstat`, and DuckDB performance. The CSV import initially failed because of its encoding, but specifying Latin-1 allowed the import to complete successfully. The DuckDB dashboard query took 4.670 ms in my measured run.

## Interaction with peers and instructors

I collected five curiosities from the module, including the `CROSS JOIN`, text-based price storage, `dbstat` measurements, the reporting-table query plan, and the use of `DISTINCT`. I also helped Felix get back on track when he was stuck with the module. This gave me an opportunity to support a fellow student and share what I had learned.

## How did you verify AI suggestions?

I ran the SQL statements in SQLite and checked the row counts, foreign-key constraints, query plans and storage figures. I also ran the dashboard query in DuckDB and checked that all 200,000 rows were loaded. I used the actual command outputs to verify the results rather than relying only on AI explanations.

## Help and extra work

AI helped me work through the SQL commands, understand the anomalies, troubleshoot the CSV encoding problem and organize my results. I also completed the optional DuckDB experiment, which helped me explore the performance of a columnar database for analytical queries.