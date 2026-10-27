PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS order_item;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price NUMERIC NOT NULL CHECK (price >= 0)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE order_item (
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

INSERT INTO customer VALUES
    (1, 'Amina'),
    (2, 'Jonas');

INSERT INTO product VALUES
    (1, 'Bearing', 12.50),
    (2, 'Coolant filter', 8.00),
    (3, 'Drive belt', 15.00);

INSERT INTO orders VALUES
    (101, 1, '2026-10-01'),
    (102, 1, '2026-10-02'),
    (103, 2, '2026-10-03');

INSERT INTO order_item VALUES
    (101, 1, 2),
    (101, 2, 1),
    (102, 3, 1),
    (103, 1, 4);

-- Check the number of orders per customer.
SELECT c.customer_id, c.name, COUNT(o.order_id) AS order_count
FROM customer AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id;

-- Check the number of order items per order.
SELECT o.order_id, COUNT(oi.product_id) AS product_count
FROM orders AS o
LEFT JOIN order_item AS oi ON oi.order_id = o.order_id
GROUP BY o.order_id
ORDER BY o.order_id;

-- Display the schema for round-trip comparison.
.schema
erDiagram
    CUSTOMER ||--o{ ORDERS : places
    ORDERS ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : appears_in

    CUSTOMER {
        int customer_id PK
        string name
    }

    ORDERS {
        int order_id PK
        int customer_id FK
        string order_date
    }

    PRODUCT {
        int product_id PK
        string product_name
        decimal price
    }

    ORDER_ITEM {
        int order_id PK, FK
        int product_id PK, FK
        int quantity
    }