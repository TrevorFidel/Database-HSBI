## ER Diagrams examples

# 1. Machine and Nameplate(1:1)

Each machine has exactly one nameplate, and each nameplate belongs to exactly one machine. 

# Machine and Sensor(One to many)

One machine can have many sensors, but each sensor belongs to exactly one machine. The foreign key is stored in the Sensor table.

# Work Oders and Parts(Many to Many)

A work order can contain many parts, and a part can be used in many work orders. A junction table resolves this relationship.

# Machine, Technician and Maintenance Job(One to Many)

Each maintenance job concerns one machine and is performed by one technician. Each machine and technician can be associated with multiple jobs.