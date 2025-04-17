CREATE TABLE Product (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  price DECIMAL(12,2)
);

INSERT INTO Product (name, price) VALUES ('Mobile', 100);
INSERT INTO Product (name, price) VALUES ('Tablet', 200);
INSERT INTO Product (name, price) VALUES ('Laptop', 300.00);
INSERT INTO Product (name, price) VALUES ('Desktop', 400);
INSERT INTO Product (name, price) VALUES ('Server', 500);