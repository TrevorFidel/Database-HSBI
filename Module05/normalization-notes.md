
# Module 05 — Normalization vs. Denormalization

## Overview

This module explored how database normalization improves consistency and reduces data anomalies, while denormalization can simplify analytical queries. I created a 200,000-row dataset, built normalized and denormalized designs, compared query performance and storage, and tested DuckDB.

---

## Round 1 — See It: Functional Dependencies

The original relation contained:

`job_id, machine_id, site, technician, part_no, part_price`

### Functional dependencies

Based on the assumed business rules:

- `job_id → machine_id`
- `job_id → technician`
- `machine_id → site`
- `part_no → part_price`
- `(job_id, part_no)` identifies a job-part row.

The candidate key is `(job_id, part_no)`, assuming a part can appear only once per job.

These dependencies rely on business rules, not just the five sample rows.

### Proposed normalized tables

- `MACHINE(machine_id, site)`
- `JOB(job_id, machine_id, technician)`
- `PART(part_no, part_price)`
- `JOB_PART(job_id, part_no)`

The `JOB_PART` table connects jobs and parts using a composite primary key and foreign keys.

---

## Round 2 — Break It: Data Anomalies

I created a flat table called `flat5` and demonstrated three anomalies.

| Anomaly | What happened |
|---|---|
| Update | Changing the site for `cnc-01` required updating three rows. |
| Insert | I inserted part `P-0004` with price `12.00` without a job, producing an incomplete row. |
| Delete | Deleting the only row for `P-0002` also removed the only stored information that the part existed and cost `7.00`. |

### Lesson

The flat table combines job, machine and part information. Repeated data creates update, insert and delete anomalies. Separating these entities into related tables improves consistency.

---

## Round 3 — Build It: Create the 3NF Design

I generated a dataset containing 200,000 rows using a `CROSS JOIN`:

- 20,000 jobs
- 10 parts per job
- 200,000 job-part rows

The flat table was called `flat_jobpart`.

### Normalized schema

I created four tables:

- `machine`: 50 rows
- `part`: 10 rows
- `job`: 20,000 rows
- `job_part`: 200,000 rows

The normalized tables were populated using `SELECT DISTINCT` from the flat table.

### Verification

| Check | Result |
|---|---:|
| Flat table rows | 200,000 |
| Normalized job-part rows | 200,000 |
| Machine rows | 50 |
| Part rows | 10 |
| Job rows | 20,000 |

I enabled foreign-key enforcement using `PRAGMA foreign_keys=ON` and checked the relationships using `PRAGMA foreign_key_check`. No foreign-key violations were returned.

Foreign-key enforcement must be enabled for each new SQLite connection.

### Lesson

Normalization separates machine, job and part information so that each fact is stored in the appropriate table.

---

## Round 4 — Race It: Query Performance

I created a denormalized reporting table called `report_jobpart` by joining the four normalized tables.

I also created an index on `report_jobpart(machine_id)`.

### Query plans

The normalized query used several lookups:

- Scanned `job_part`
- Looked up matching jobs
- Looked up machines
- Looked up parts
- Used a temporary B-tree for grouping

The denormalized query scanned the reporting table using its machine index and also used a temporary B-tree for grouping.

### Measured dashboard query times

| Design | Time |
|---|---:|
| Normalized SQLite | 391 ms |
| Denormalized SQLite | 385 ms |

These were single measured runs after warming the cache, not repeated measurements or medians.

### Lesson

The denormalized query was slightly faster in this test, but the difference was small. The query plans showed that denormalization reduced the number of joins.

---

## Round 5 — Price It: Write Cost and Storage

I updated the site for machine `cnc-02` in both designs.

### Rows changed

| Design | Rows changed |
|---|---:|
| Normalized machine table | 1 |
| Denormalized report table | 4,000 |

The normalized design needed only one machine record to change. The denormalized design needed 4,000 repeated records to change.

### Storage measurements

I used SQLite's `dbstat` virtual table.

| Design | Storage |
|---|---:|
| Normalized tables | 4,071,424 bytes (3,976 KB) |
| Denormalized report table | 10,932,224 bytes (10,676 KB) |

These figures came from the specific `dbstat` queries used in the exercise; they should not be treated as a complete comparison of every database object and index.

The denormalized table used approximately 2.7 times as much table storage.

### Lesson

Denormalization can simplify reads, but it increases storage and write work because information is repeated.

---

## Round 6 — Decide and Defend

### Recommendation to the Operations Lead

I recommend using the denormalized `report_jobpart` table for the dashboard if read performance is the main priority. In my benchmark, the normalized query took 391 ms, while the denormalized query took 385 ms, so the improvement was small. However, the denormalized table used approximately 10,676 KB compared with 3,976 KB for the normalized tables. Updating one machine's site changed only 1 row in the normalized design but 4,000 rows in the reporting table. Therefore, the transactional tables should remain in 3NF to protect data consistency and reduce update anomalies. The reporting table should be kept current using a scheduled rebuild or carefully maintained triggers. This approach balances reliable transactions with convenient dashboard reporting.

### Decision

Keep the transactional tables normalized in 3NF. Use a denormalized reporting table only where the dashboard workload justifies its extra storage and maintenance cost.

---

## Round 7 — Harvest: Curiosities

I collected five points worth discussing:

1. **CROSS JOIN:** It multiplied 20,000 jobs by 10 parts to produce 200,000 rows.
2. **Money stored as text:** `printf('%.2f', ...)` formatted prices to two decimal places, but the flat table stored the values as text.
3. **dbstat:** The normalized tables used about 3,976 KB, compared with 10,676 KB for the report table.
4. **Report table plan:** The denormalized table reduced joins but required more storage and more rows to update.
5. **DISTINCT assumption:** It removed duplicates when creating normalized tables, relying on the assumption that each machine and part had consistent details.

The neighbour list swap was not completed.

---

## Optional Stretcher — DuckDB

I exported the 200,000 rows from SQLite into `Module05/report_jobpart.csv` and imported them into DuckDB.

The CSV required an explicit `latin-1` encoding setting when importing because it contained non-ASCII text.

### Results

- DuckDB rows loaded: 200,000
- Dashboard query time: 4.670 ms

| Database design | Dashboard query time |
|---|---:|
| SQLite normalized | 391 ms |
| SQLite denormalized | 385 ms |
| DuckDB denormalized | 4.670 ms |

The DuckDB timing was a single measured run after a warm-up query.

### Observation

DuckDB was much faster for this analytical query in this experiment. Its columnar engine may reduce the need for a separate denormalized reporting table for some analytical workloads.

However, I tested DuckDB using the denormalized CSV table. I did not benchmark an equivalent normalized DuckDB schema, so I cannot conclude that DuckDB eliminates the need for denormalization entirely.


**Main takeaway:** Keep transactional data normalized where consistency matters, and use denormalization or analytical database engines when measured reporting needs justify them.