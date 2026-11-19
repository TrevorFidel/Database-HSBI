# Module 5 — Database Normalization and Performance

In this module, I explored how database schema design affects data integrity, query performance, write operations and storage requirements.

My main focus was understanding when normalization is beneficial, when deliberate denormalization can improve performance, and how to use measurements to justify schema design decisions.

## Learning Goals

By completing this module, I aimed to demonstrate that I could:

1. **Identify functional dependencies:** Derive functional dependencies from a relation and identify its candidate keys.
2. **Normalize database relations:** Apply 1NF, 2NF and 3NF, explaining the data anomalies addressed at each stage.
3. **Denormalize deliberately:** Design a denormalized structure to improve a frequently used read path while understanding the additional write and storage costs.
4. **Measure performance trade-offs:** Compare query latency, write costs and database size before and after normalization or denormalization.
5. **Justify schema design decisions:** Evaluate the workload and defend an appropriate balance between normalization and denormalization.

## My Work and Evidence

Throughout this module, I worked through practical exercises involving functional dependencies, normalization, denormalization and performance measurement.

| Task | What I worked on | Evidence |
|---|---|---|
| 1 — Functional dependencies | Identified functional dependencies and the candidate key for the original relation. | [Module05/normalization-notes.md] |
| 2 — Normalization | Investigated data anomalies and transformed the original relation into a normalized design. | [Module05/normalization-notes.md] |
| 3 — Database implementation | Built normalized and denormalized tables and checked their data integrity. | [Module05/normalization.db] |
| 4 — Query performance | Compared report query performance across the normalized and denormalized designs. | [Module05/normalize.db] |
| 5 — Write cost and storage | Measured the impact of updates and compared database storage requirements. | [Module05/normalization-notes.md] |
| 6 — Design recommendation | Prepared a recommendation explaining which schema design best suited the workload. | [Module05/normalization-notes.md] |
| 7 — Further exploration | Recorded additional questions and ideas for further investigation. | [Module05/normalization-notes.md] |
| Optional — DuckDB | Loaded the CSV data into DuckDB and explored query execution in another database engine. | [Module05/dashboard.duckdb] |

## Key Takeaways

This module helped me understand that database normalization is not simply about reducing duplication. It is also about improving consistency and preventing data anomalies.

I learned that denormalization can improve particular read operations, but it introduces additional costs when updating data and maintaining storage.

By measuring query latency, write costs and database size, I could make a more informed decision about which schema design best suited a particular workload.

## Navigation

**Portfolio Home:** [[Home](../README.md)]

**Module 5 — Normalization Notes:** [[normalization_notes.md](normalization-notes.md)]

**Module 5 — Reflection:** [[ref05](../Reflections/ref05.md)]

**Previous Module — Module 4:** [[Module04](../Module04/README.md)]

**Next Module — Module 6a:** [[Module06a](../Module06a/README.md)]