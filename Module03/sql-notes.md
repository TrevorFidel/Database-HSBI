## Six Clauses and the plan
to be continued.....

# Sqlite Query Prediction before running

# Query	                        Prediction
WHERE technician = 'Beier'	    SEARCH — an index might be used, if one exists

WHERE machine_name = 'cnc-02'	SEARCH — an index might be used, if one exists

WHERE technician LIKE '%ei%'	SCAN — the leading wildcard usually prevents an ordinary index lookup


# Results after running
Query 1: technician = 'Bier'. Predicted (SEARCH)resulted into 'SEARCH maint_job USING INDEX ix_job_tech (technician=?). SQlite used the existing technician index, which I was suppposed to add the index on the next step.
(see picture)

Query 2: machine_name = 'cnc-02'. Prediction: (SEARCH) resulted into SCAN machine. SQlite scanned the table because no suitable index was used. Continued directly to part 3 discovered that indexes speed up matching queries when suitable but queries with a leading wildcard like LIKE'%ei%' still require a table scan.

Query 3: technician LIKE '%ei%'. Prediction: (SCAN) resulted  into SCAN maint_job. A leading wildcard prevents a normal B-tree index from efficiently searching for a substring.

Generally, EXPLAIN QUERY PLAN reveals whether SQlite scans table or uses an index to find matching rows.

Couldn't continue with the task A 2 since I already had index before running the program mst likely from the previous modules hence my findings are after the index is in place and not before the index.


# My wrong prediction

Query 2- I predicted SEARCH but SQlite returned SCAN machine because it didn't use a suitable index for machine_name.

Findings -> A WHERE condition doesn't guarantee an index lookup. Without a suitable index,SQlite may scan the table.

# Algebra Check

| Symbol |       | Meaning |            |SQL equivalent |

| **σ** (sigma) | Select rows that match a condition | `WHERE` |

| **π** (pi)    | Select specific columns | `SELECT column_name` |

| **⋈** (join)  | Combine related tables | `JOIN` |

Choose the 1st Query which turned into: \[
\sigma_{\text{technician}='Beier'}(\text{maint\_job})
\]

# SQlite query plan comparison

SQLite version: 3.46.1 (64-bit).

Biggest surprise: The equality query can use an index, but LIKE '%ei%' scans the whole table.

Lesson: Index usage depends on the query conditions and available indexes.


# Warehouse/ oder dataset

Before: SCAN orders — SQLite scanned the table.

After: SEARCH orders USING INDEX ix_orders_status (status=?) — SQLite uses the index to find matching rows.

Index creation time: about 0.066 seconds.

Query plan time shown: about 0.001 seconds.

Query: SELECT * FROM orders WHERE status = 'late';

Before index: SCAN orders.

After index: SEARCH orders USING INDEX ix_orders_status (status=?).

Matching rows: 12,000.

Oders: 6000||
Oderlines: 240000

Lesson: An index lets SQLite search for matching status values instead of scanning the entire table. The displayed timings are very small, so repeated measurements would be needed for a reliable performance comparison.

## Asking LLM then checking the plan

# Prediction

customer → likely SCAN

orders → likely SCAN to filter by date

order_line → likely SCAN

product → likely SEARCH using its primary key

USE TEMP B-TREE → possible for COUNT(DISTINCT ...) and ORDER BY

# Findings of the planed query

- **Prediction vs. actual:** SQLite scanned `order_line` and searched `orders`, `customer`, and `product` using their integer primary keys.
- **Temporary B-trees:** Used for `GROUP BY`, `COUNT(DISTINCT)`, and `ORDER BY`.
- **Lesson:** Joins can use primary-key lookups, while grouping, distinct counting, and sorting may require temporary structures.

# Findings of the actual query

All 4 cities each with 500 distinct customers.
- **Results:** Bielefeld: 11,242,176; Gütersloh: 8,422,344; Münster: 5,493,504; Paderborn: 2,815,656.
- **Correctness:** The query counts distinct customers and sums `qty * price` for order lines belonging to orders dated in 2025. The date filter is correctly applied before grouping.
- **Observation:** The query took about 0.800 seconds. All four cities have 500 distinct customers represented in the results.

# Index Benchmark

Dashboard baseline: Median runtime = 0.307s.

Indexes tested: ix_orders_ordered_on, ix_orderline_order, and ix_orderline_product.

Dashboard result: The query plan stayed unchanged after each index was added. SQLite continued to scan order_line and use primary-key lookups for the other tables.

Single-day lookup with date index: SQLite used SEARCH o USING INDEX ix_orders_ordered_on (ordered_on=?).

Runtime with date index: 0.066 s, 0.055 s, 0.039 s. Median = 0.055 s.

Single-day lookup without date index: After dropping ix_orders_ordered_on, SQLite changed to SCAN o.

Without the date index, SQLite should scan the orders table. The median runtime is higher than the indexed median of 0.055s.

Conclusion: Indexes do not automatically improve every query. Their usefulness depends on the query and the execution plan chosen by SQLite.

## SQL Injection

Payload used: ' OR '1'='1

Vulnerable query: Builds SQL by inserting user input directly into the query string. The payload changes the condition so it matches all rows.

Safe query: Uses a bound parameter (?) and passes the value separately with (name,). SQLite treats the payload as data, not executable SQL.

Why manual escaping or filtering is not a real fix:
Removing or escaping apostrophes by hand is error-prone and depends on SQL syntax and context. SQL values, identifiers, numeric contexts, and character encodings can require different handling. A homemade filter can miss cases or change legitimate input. Bound parameters let the database driver handle values correctly, keeping data separate from SQL code.

Conclusion: Use bound parameters for values instead of building SQL queries through string concatenation or interpolation.

# One Query from algebra to plan

The algebra and SQL match logically. The query plan is SQLite's chosen execution strategy, which may differ from the order in which the SQL is written. *more will be added.

# Stretcher - Window Functions and Subquery Rewrite

Objective: Rewrite the late-orders-per-customer report using a correlated subquery and a window function, then compare the query plans and readability.

Original query: Joins orders and customer, filters for status = 'late', groups by customer, and counts late orders.

Correlated subquery: Counts late orders separately for each customer. An EXISTS condition excludes customers with no late orders.

Window function: Uses COUNT(*) OVER (PARTITION BY customer_id) to calculate each customer's late-order count while retaining individual order rows.

Readability: The original grouped query is the most direct. The correlated subquery makes the per-customer count explicit. The window version demonstrates partitioned counting but may require an additional query layer to produce one row per customer.

Query plans: Compare the actual SQLite plans to see how each version accesses orders and customer and whether sorting or temporary structures are needed.

Conclusion: Different SQL formulations can express the same report. Comparing their results, query plans, and readability helps determine which is most suitable.

NB: The window-function query above uses GROUP BY to remove repeated rows. We should verify that its results match the original query before treating it as complete.