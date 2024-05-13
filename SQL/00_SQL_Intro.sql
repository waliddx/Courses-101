-- SQL Introduction :

-- SQL (Structured Query Language) is a programming language used for managing and manipulating relational databases.

-- Creating a Database
CREATE DATABASE mydatabase;

-- Using a Database
USE mydatabase;

-- Creating a Table
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);

-- Inserting Data into a Table
INSERT INTO customers (id, name, email)
VALUES (1, 'John Doe', 'john@example.com');

-- Selecting Data from a Table
SELECT * FROM customers;

-- Updating Data in a Table
UPDATE customers
SET email = 'johndoe@example.com'
WHERE id = 1;

-- Deleting Data from a Table
DELETE FROM customers
WHERE id = 1;

-- Dropping a Table
DROP TABLE customers;

-- Dropping a Database
DROP DATABASE mydatabase;