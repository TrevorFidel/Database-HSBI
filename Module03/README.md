# Module 3 — SQL Query Design, Security and Performance

In this module, I explored how to write complex SQL queries, understand database query execution, improve performance and protect databases against security vulnerabilities.

My main focus was learning not only how to write SQL queries, but also how to understand what happens when they run, evaluate their efficiency and make them more secure.

## Learning Goals

By completing this module, I aimed to demonstrate that I could:

1. **Build complex DQL queries:** Use joins, aggregations with `GROUP BY` and `HAVING`, subqueries and window functions.
2. **Understand query execution plans:** Use `EXPLAIN QUERY PLAN` to distinguish between `SCAN` and `SEARCH`, and understand table lookups and covering indexes.
3. **Evaluate index performance:** Compare queries with and without indexes and explain why the query planner may decide not to use an index.
4. **Verify AI-generated SQL:** Use an LLM to generate SQL queries and independently check their correctness, performance and behaviour with edge cases.
5. **Prevent SQL injection:** Use bound parameters and demonstrate the risks of building SQL queries through string concatenation.

## My Work and Evidence

Throughout this module, I completed practical exercises that helped me develop my SQL querying, performance analysis and database security skills.

| Task | What I worked on | Evidence |
|---|---|---|
| 1 — Complex SQL queries | Practised joins, aggregations, subqueries, filtering and window functions. | [Module03/sql-notes.md] |
| 2 — Query execution plans | Investigated how SQLite executes queries using `EXPLAIN QUERY PLAN`. | [Module03/pictures/query-plan-run-results.png] |
| 3 — Index performance | Compared query performance with and without indexes and examined index selection by the query planner. | [Module03/pictures/index-benchmark-sqlnotes.png] |
| 4 — AI-generated SQL | Used AI-generated queries and checked their correctness, performance and edge cases. | [Module03/sql-notes.md] |
| 5 — SQL injection | Explored SQL injection through string concatenation and applied bound parameters as a safer approach. | [Module03/sql-notes.md] |

## Key Takeaways

This module helped me understand that writing a working SQL query is only part of database development.

I also learned the importance of examining query execution plans, measuring performance, choosing appropriate indexes and protecting queries against malicious input.

I now understand why SQL queries should be tested and verified rather than accepted simply because they produce a result.

## Navigation

**Portfolio Home:** [[Home](../README.md)]

**Module 3 — SQL-notes.md:** [[sql_notes.md](sql-notes.md)]

**Module 3 — Reflection:** [[ref03](../Reflections/ref03.md)]

**Next Module — Module 4:** [[Module04](../Module04)]