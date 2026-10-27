## ER Models Study Log

# Reference used

Entity relation model - entities, attributes, relationships and cardinality.https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model

Enhanced ER model - inheritance and generalization. https://en.wikipedia.org/wiki/Enhanced_entity%E2%80%93relationship_model

SQlite single form - how foreign keys enforce relationships.https://sqlite.org/foreignkeys.html


# Things I looked up

Cardinality -> describes how many instances of one entity can relate to instances of another entity.

Natural keys -> uses existing meaningful data to identify a record. eg passport no. and email address.

Surrogate keys -> Artificially generated keyused to uniquely identify a record.eg automatic increment ID.

1NF(First Normal Form) -> A table is in 1NF if every cell contains a single, atomic value and there no repeating groups or multivalued attributes.

Relationship -> describes more how entities are associated.

Entities -> objects about which we store data.

Attributes -> properties of those entities.

# Aha moments

I learned that a column that looks unique may contain duplicate values.

Cardinality can be investigated by counting distinct values in the actual database.

A comma-separated list in one column can make searching and updating data more difficult.

Foreign keys help prevent records from referring to nonexistent records.

# LLM Q&A

Prompt: Explain entity–relationship models using simple examples.

Summary: An ER model describes entities, their attributes, and relationships. For example, a student can enroll in several courses, and each course can have several students.

Verification: I will compare this explanation with the ER model reference and identify the entities and relationships in my database.


Prompt: Explain the difference between a natural key and a surrogate key.

Summary: A natural key comes from meaningful real-world data, while a surrogate key is an artificial identifier. A surrogate key can remain stable when descriptive information changes.

Verification: I will inspect the table definitions in my database and identify the columns used as primary keys.

# Reflection

The most useful concept I learned was cardinality because it helps explain how records relate across database tables. I also learned that an ER diagram should be checked against the actual schema and data instead of relying only on documentation.

# Agreed Learning Pod Discussion.

Keys: A primary key uniquely identifies each record. A natural key must be unique to identify records reliably.

Cardinality: Relationships can be 1:1 (one-to-one), 1 (one-to-many), or M (many-to-many).

Foreign Keys: In a 1 relationship, the foreign key is placed on the many side.

Junction Tables: M relationships require a junction table containing foreign keys to both entities.

Entities and Attributes: Entities represent objects, while attributes describe their properties. Relationships describe how entities are connected.


We concluded that choosing appropriate keys and correctly identifying cardinality are essential for designing a reliable database. We also learned that ER diagrams helps understand the relationships before converting them into relational tables.

# Mermaid ER Diagrams

Mermaid diagrams help visualize database relationships, but they do not show every SQL constraint. Diagrams must be checked against the actual schema and data. Cardinality and inheritance should reflect real business needs, not unnecessary assumptions.

Learned that foreign keys and constraints must also be checked and not just the sample data, when converting SQL schema into Mermaid ER.