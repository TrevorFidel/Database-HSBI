# Module 2 — Database Modelling, Integrity and Schema Auditing

In this module, I explored how to understand an existing database schema, reconstruct its data model and identify problems that could affect data integrity.

My main focus was learning how to interpret database structures, distinguish relationships and keys, investigate integrity defects and translate database designs into application-level data contracts.

## Learning Goals

By completing this module, I aimed to demonstrate that I could:

1. **Reconstruct ER/EER models:** Identify entities, attributes, keys, relationships and cardinalities from an undocumented SQL schema.
2. **Audit database integrity:** Use SQL queries to identify missing foreign keys, orphan records, redundant data and normalization problems.
3. **Understand database modelling concepts:** Distinguish entities from attributes and surrogate keys from natural keys, and justify appropriate design choices.
4. **Create code-first data contracts:** Represent database structures using Pydantic and SQLAlchemy so applications can enforce data requirements.
5. **Identify missing business rules:** Document requirements and constraints that are important to the business but are not enforced by the existing schema.

## My Work and Evidence

Throughout this module, I completed five practical tasks involving database modelling, schema auditing, integrity checks and application-level data contracts.

| Task | What I worked on | Evidence |
|---|---|---|
| 1 — Schema investigation | Studied the existing database structure and documented my findings. | [study-log.md] |
| 2 — ER/EER modelling and audit | Reconstructed relationships and investigated schema integrity defects. | [er-audit.md] |
| 3 — Keys and relationships | Explored modelling examples, entity relationships and key design choices. | [er-examples.md] |
| 4 — Schema visualisation | Practised representing database structures and relationships using Mermaid diagrams. | [mermaid-lab.md] |
| 5 — Data contracts and business rules | Documented application-level requirements and business rules that the schema should enforce. | [Module02/study-log.md] |

## Key Takeaways

This module helped me understand that an existing database schema does not always tell the whole story.

I learned to reconstruct relationships, identify integrity problems using SQL and distinguish between different types of keys and database objects.

I also gained an appreciation for documenting business rules and expressing database requirements in a way that both the database and application can enforce.

## Navigation

**Portfolio Home:** [[Home](../README.md)]

**Module 2 — Mermaid-lab.md:** [[mermaid-lab.md](mermaid-lab.md)]

**Module 2 — Study Log:** [[study-log.md](study-log.md)]

**Module 2 — Reflection:** [[ref02](../Reflections/ref02.md)]

**Next Module — Module 3:** [[Module03](../Module03/README.md)]