# Module 06b — Polyglot Persistence & the Decision

This module explores how different database engines and storage approaches support different workloads. It compares SQLite, PostgreSQL, JSON storage and key-value access patterns to make evidence-based decisions about where different types of data should live.

## Learning Goals

- Understand the differences between local and remote database access.
- Store and query semi-structured JSON data in SQLite.
- Compare key-value storage with relational database access.
- Explain ACID, BASE and CAP in practical database scenarios.
- Select database engines based on workload requirements and measured evidence.
- Defend database decisions by explaining their trade-offs.

## My Work and Evidence

| Task | Evidence | Description |
|---|---|---|
| Local vs remote database boundary | results observations | Examine shared PostgreSQL access, concurrent updates and server availability. |
| JSON metadata storage | `json_bench.py`, `polyglot-notes.md` | Explore JSON storage, JSON queries and expression-index behaviour in SQLite. |
| Database decision record | `decision-record.md` | Assign database engines to workloads and explain the reasons and trade-offs. |
| Key-value benchmark | `kv_compare.py` | Compared Shelve and SQLite using 20,000 writes and 20,000 lookups. |
| Final project ticket | `project-ticket.md` | Define the intended project problem, user, first database query and data source. |

## Key Results

- Shelve write time for 20,000 records: **35.862 seconds**.
- SQLite write time for 20,000 records: **0.058 seconds**.
- Shelve lookup time for 20,000 records: **0.267 seconds**.
- SQLite lookup time for 20,000 records: **1.625 seconds**.
- SQLite was approximately **618 times faster for writes** in this benchmark.
- Shelve was approximately **6 times faster for individual lookups** in this benchmark.

## Key Takeaways

Different database engines are suited to different workloads. SQLite provides transactional storage, relational queries and flexible JSON support. Shelve offers simple dictionary-style key-value access, while PostgreSQL supports shared access from multiple network clients. The benchmark demonstrates that performance depends on the operation being measured. Database choices should therefore consider performance, consistency, access patterns and operational requirements.

## Navigation

- [Polyglot Notes](polyglot-notes.md) — JSON storage and technical task results.
- [Decision Record](decision-record.md) — Database choices and supporting evidence.
- [Key-Value Benchmark](kv_compare.py) — Shelve and SQLite performance comparison.
- [JSON Benchmark](json_bench.py) — JSON queries and expression-index comparison.
- [Project Ticket](project-ticket.md) — Final project problem and initial requirements.

**Module 06b Reflection:** [Reflection 06b](../Reflections/ref06b.md)

**Previous Module:** [Module 06a](../Module06a/README.md)

**Next Module:** [To be continued](../README.md)