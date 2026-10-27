## Legacy Schema Audit

This audit is aimed at examining a flawed legacy database, identify it's entities and relationships, while using SQL queries to prove its integrity defects.

# Key Findings

1. Entities: The intended model contains Machine, Part, MaintenanceJob, and Technician, with a junction table called JobPart to connect maintenance jobs and parts.

2. Primary Keys:The table lacks properly defined keys hence allowing duplicate records eg part number P-1003.

3. Relationship: Machine–MaintenanceJob and Technician–MaintenanceJob are intended to be one-to-many (1) relationships. MaintenanceJob–Part is a many-to-many (M) relationship that should be implemented using a junction table.

4. Foreign Keys: The maintenance job referencing cnc-05 is an orphan record because that machine does not exist in the Machine table.

5. Data Quality: Prices are stored as text, and one machine has an invalid installation date recorded as unknown.

6. First Normal Form(1NF):  Prices are stored as text, and one machine has an invalid installation date recorded as unknown.

# Conclusion

The audit shows why a database needs appropriate keys, foreign keys, data types and normalized relationships. the proposed solutions enforces data integrity constraints, store prices numerically, validate dates and replaces the comma separated parts list with a junctiion table. SQL queries provides evidence of the defects rather than relying on assumptions.

# Er audit results and production impacts.

1. Orphan maintenance jobs: A job referencing a nonexistent machine cannot be reliably linked to the machine’s maintenance history or site.

2. Duplicate part numbers: Duplicate P-1003 records can lead to inaccurate inventory counts and double-counted maintenance costs.

3. Price stored as text: Text-based price comparisons can exclude cheaper parts, resulting in incorrect purchasing decisions or invoices.

4. Invalid installation date: The value unknown prevents reliable machine-age calculations and can disrupt warranty checks and maintenance scheduling.

5. Comma-separated parts list: Multi-part jobs can be omitted from reports, while duplicate part records can cause parts and costs to be counted more than once.

# EER Inheritance and Disjointness

Objective: Model two machine subtypes—CNC mills and injection molders—using two database designs and choose the preferred design.

1. Alternative A: Single-table inheritance
- Stores all machines in one machine table.
- Uses a machine_type discriminator to identify CNC mills and injection molders.
- Uses a CHECK constraint to enforce disjointness and require the correct subtype attributes.
- Advantage: Simple structure with fewer tables.
- Disadvantage: Contains nullable columns for attributes that do not apply to each machine type.

2. Alternative B: Separate subtype tables
- Stores common attributes in the machine table.
- Stores CNC-specific attributes in cnc_mill.
- Stores injection-molder-specific attributes in injection_molder.
- Uses primary keys, foreign keys, and triggers to enforce relationships and disjointness.
- Advantage: Better organization and easier extension.
- Disadvantage: Requires joins to retrieve all machine details.

3. Decision
I would choose Alternative B (separate subtype tables) because it separates subtype-specific attributes, reduces unnecessary nullable columns, and makes the database easier to maintain and extend.