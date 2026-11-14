# Reflection 04 — Data Integrity, Constraints, and Edge Triggers

## Take-away

Module 4 helped me understand the importance of maintaining data integrity and controlling how information is stored and modified in a database. I learned that constraints, generated columns, triggers, and UPSERT operations help ensure that data remains accurate and consistent. My main takeaway was that a reliable database should not simply store information but should also enforce rules, prevent invalid data, and automate important operations.

## What was good?

I found it useful to explore how SQLite constraints protect data from incorrect entries. Testing `NOT NULL`, `UNIQUE`, `CHECK`, foreign keys, and `STRICT` tables helped me understand how different rules improve data quality. I also enjoyed working with triggers because they demonstrated how a database can automatically generate alarms and maintain an audit trail when data changes. Using Python with `executemany()` and UPSERT was another useful exercise because it showed how repeated data imports can be handled without creating duplicate records.

## What was difficult?

One challenge was understanding how different constraints behave, especially how `CHECK` constraints interact with `NULL` values. I also encountered difficulties when working with the command line and creating the CSV file for the Python ingestion script. Another challenge was understanding SQLite access control and how read-only permissions work. With step-by-step guidance and testing, I was able to resolve these issues and complete the exercises.

## Exploration and show stoppers

Exploring triggers and measuring their performance helped me understand that database automation has both benefits and costs. I compared inserting 10,000 records with and without the alarm trigger. The insertion took 0.069 seconds without the trigger and 0.086 seconds with it, showing a small performance difference. I also explored SQLite access control by creating a view, changing file permissions, and testing read-only connections. This helped me understand the limitations of SQLite compared with a server-based database such as PostgreSQL.

## Interaction with peers and instructors

During this module, I used the available learning resources and an LLM to help me understand the exercises and troubleshoot technical problems. The step-by-step guidance helped me work through SQL commands, Python ingestion, triggers, and file permissions. This experience reinforced the importance of asking questions and using additional resources when I encounter unfamiliar database concepts.

## How did you verify AI suggestions?

I used an LLM to help explain SQL constraints, write triggers, develop the Python ingestion script, and troubleshoot command-line errors. However, I verified the suggestions by executing the commands and checking the actual database results. For example, I confirmed that UPSERT did not increase the row count when the same CSV was processed twice. I also checked that the alarm and audit triggers produced the expected records and that read-only connections allowed SELECT statements but rejected DELETE operations.

## Help and extra work

My main focus was understanding how to build databases that maintain data integrity and automate important operations. I used an LLM for guidance when creating SQL statements, writing Python code, and resolving command-line issues. I also completed additional testing by measuring trigger performance and comparing SQLite access control with PostgreSQL. This module improved my confidence in working with database constraints, automation, data ingestion, and basic database security.