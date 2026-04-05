-- Relational schema for AI-powered Inventory Management System.
CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    category VARCHAR(80) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    type ENUM('IN', 'OUT') NOT NULL,
    quantity INT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_transactions_product FOREIGN KEY (product_id)
        REFERENCES products(id) ON DELETE CASCADE
);

-- Sample default user: admin / admin123 (bcrypt hash)
INSERT INTO users(username, password_hash)
VALUES ('admin', '$2b$12$2TayN6hf9m4L4BbaNfX2NOx6pE0vE4zxi8Yo8dcbf5X8KcKvARdji')
ON DUPLICATE KEY UPDATE username=username;
