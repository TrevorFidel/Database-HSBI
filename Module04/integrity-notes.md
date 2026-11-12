## Module04 Notes

## Data Integrity, Constraints and Edge Triggers

# Integrity and Constraints 

SQLite handles invalid data in tables with and without constraints. Tested how PRIMARY KEY, NOT NULL, CHECK, and STRICT protect data integrity.


PRIMARY KEY: Uniquely identifies each row and prevents duplicate IDs.

NOT NULL: Prevents required columns from being left empty.

CHECK: Restricts values to specified conditions, such as allowed metrics or numeric ranges.

STRICT: Enforces declared data types and rejects incompatible values.

NULL and CHECK: A CHECK constraint alone does not reject NULL; use NOT NULL when a value is required.

Constraint limitations: Values can still be incorrect even when they satisfy the defined rules. For example, a temperature of 4500 was accepted because it was within the permitted range.

# Key Takeaway

Constraints help the database reject invalid data automatically, but the rules must be carefully designed to reflect realistic requirements. Database integrity depends on both the constraints used and the quality of the rules behind them.


### Task B — Pod Discussion

- **Most surprising finding:** An unconstrained SQLite table accepted text in a REAL column, an invalid metric, and an unrealistic temperature.
- **Hardest concept:** `CHECK` with `NULL`. A CHECK constraint does not reject NULL automatically; `NOT NULL` is needed for mandatory values.
- **Agreed takeaway:** Database constraints protect data integrity, but they must reflect realistic business rules. Different constraints protect against different types of invalid data.

# Test Evidence and Results

Valid sensor and reading -> Accepted.

Temperature 9000 -> Rejected — CHECK constraint failed.

Text 'hot' in REAL column -> Rejected — STRICT type enforcement.

Non-existing sensor ID 99 -> Rejected — FOREIGN KEY constraint failed.

Duplicate (machine_id, metric) -> Rejected — UNIQUE constraint failed

Generated energy_j -> Successfully calculated as 41.5

# Task 3 — Triggers for Alarms and Audit

Created two SQLite triggers to automate alarm generation and maintain an audit trail whenever reading values change.


AFTER INSERT trigger: Creates an alarm when vibration exceeds 2.0 mm/s.

AFTER UPDATE trigger: Records the reading ID, old value, new value and timestamp.

OLD and NEW: Allow triggers to access values before and after an update.

Audit trail: Automatically records changes without relying on application code.

Trigger performance: Triggers add processing overhead to database operations.

 In conclusion, Triggers automate database actions and help maintain reliable audit records. However, they introduce additional processing, so their performance impact should be measured.

 ### Task 4 — Access Control Without a Server

**Overview**

Demonstrated SQLite access control using a database view, file permissions and read-only connections.

**Important Notes**
- **Views:** `machine_health` exposes summarized machine data without requiring report readers to query the underlying tables directly.
- **chmod 444:** Removes write permissions from the database file.
- **mode=ro / -readonly:** Allows reading but prevents database modifications.
- **chmod 644:** Restores write access for the file owner.

**PostgreSQL Comparison**

PostgreSQL provides server-based access control through users, roles and `GRANT`/`REVOKE` permissions. SQLite has no equivalent built-in user management, so access is generally controlled through file permissions and connection settings. File-level permissions are acceptable for a local database with trusted users, but they are insufficient for a multi-tenant web application because different users need separate permissions enforced by the database server or application. Otherwise, users who can access the database file may bypass application-level restrictions.

**Key Takeaway**

SQLite uses file and connection permissions rather than server-based user roles. This is practical for local applications but less suitable for systems requiring fine-grained access control between multiple users.