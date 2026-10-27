# Task 5: Mermaid ER Diagram Lab

### Diagram 1: Good Design — Online Store

This diagram represents a simple online store. Customers place orders, and orders contain products. The associative entity `ORDER_ITEM` resolves the many-to-many relationship between orders and products.

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        int customer_id PK
        string name
    }

    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : appears_in

    ORDER {
        int order_id PK
        date order_date
        int customer_id FK
    }

    ORDER_ITEM {
        int order_id PK, FK
        int product_id PK, FK
        int quantity
    }

    PRODUCT {
        int product_id PK
        string product_name
        decimal price
    }
```

**Critique:** This is a good design because it uses clear entities, primary keys, foreign keys, and an associative entity. It avoids storing multiple product IDs in one order column.

### Diagram 2: Strange Design — Recursive Employee Relationship

This diagram models employees who supervise other employees. The relationship connects the `EMPLOYEE` entity to itself.

```mermaid
erDiagram
    EMPLOYEE o|--o{ EMPLOYEE : supervises

    EMPLOYEE {
        int employee_id PK
        string employee_name
        int supervisor_id FK
    }
```

**Critique:** This design is unusual because an entity relates to itself. It is useful for organizational hierarchies, but queries must handle multiple levels of supervision. The optional side allows an employee to have no supervisor, such as a company director.

### Diagram 3: Wrong or Confusing Design — Products Stored as Text

This diagram represents a poorly designed order system where several products are stored in one text field.

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places

    CUSTOMER {
        int customer_id PK
        string name
    }

    ORDER {
        int order_id PK
        int customer_id FK
        string products
    }
```

**Critique:** This design is confusing because the `products` field may contain several product names separated by commas. Individual products cannot be reliably referenced, searched, or constrained using ordinary foreign keys. A separate `PRODUCT` table and `ORDER_ITEM` junction table would be better.