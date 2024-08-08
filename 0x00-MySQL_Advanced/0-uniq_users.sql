-- Creates a table, 'users' with id, email, and name columns
-- Only creates table if not already created
CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY AUTO_INCREMENT,
email VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255))
