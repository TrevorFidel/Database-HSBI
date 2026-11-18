# Module 4 — Data Definition, Manipulation and Integrity

In this module, I explored how to define database structures, manipulate data safely and enforce integrity rules directly within the database.

My main focus was understanding how constraints, generated columns, triggers and UPSERT operations help maintain reliable data, as well as how access control works in an embedded, local-first database environment.

## Learning Goals

By completing this module, I aimed to demonstrate that I could:

1. **Apply database constraints:** Create tables using `NOT NULL`, `UNIQUE`, `CHECK`, `PRIMARY KEY`, `FOREIGN KEY` and `STRICT` typing to enforce data integrity.
2. **Use generated columns:** Derive values directly within the database engine instead of relying on application code.
3. **Create database triggers:** Enforce domain rules and automatically maintain audit or rollup tables.
4. **Use DML and UPSERT correctly:** Apply `INSERT`, `UPDATE`, `DELETE` and `ON CONFLICT` to support reliable and idempotent data ingestion.
5. **Understand database access control:** Reason about read and write permissions, including how server-based `GRANT` permissions differ from access control in embedded, local-first databases.

## My Work and Evidence

Throughout this module, I completed practical exercises covering database constraints, data ingestion, triggers and access control.

| Task | What I worked on | Evidence |
|---|---|---|
| 1 — Constraints and generated columns | Used constraints and `STRICT` tables to enforce data integrity, and explored generated columns. | [Module04/integrity-notes.md] |
| 2 — UPSERT and CSV ingestion | Used Python, `executemany()` and `ON CONFLICT` to import CSV data safely and support repeatable ingestion. | [Module04/ingest.py] |
| 3 — Triggers and auditing | Created triggers to enforce rules and maintain audit records, then compared their performance. | [Module04/integrity-notes.md] |
| 4 — Access control | Explored views, file permissions and read-only connections to control database access. | [Module04/integrity-notes.md] |

## Key Takeaways

This module helped me understand that data integrity should be enforced as close to the data as possible.

I learned how constraints prevent invalid records, how generated columns reduce repeated application logic, and how triggers automate database actions.

I also gained practical experience with UPSERT for reliable data ingestion and learned how access control must be considered differently in embedded databases compared with traditional database servers.

## Navigation

**Portfolio Home:** [[Home](../README.md)]

**Module 4 — Integrity-notes.md:** [[integrity-notes.md](integrity-notes.md)]

**Module 4 — Reflection:** [[ref04](../Reflections/ref04.md)]

**Previous Module — Module 3:** [[Module03](../Module03/README.md)]

**Next Module — Module 5:** [[Module05](../Module05/README.md)]