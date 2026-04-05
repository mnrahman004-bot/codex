"""Product data access layer."""
from backend.config.db import db


class ProductModel:
    """Model for CRUD operations on products."""

    @staticmethod
    def list_products(search=None, category=None):
        query = "SELECT * FROM products WHERE 1=1"
        params = []
        if search:
            query += " AND name LIKE %s"
            params.append(f"%{search}%")
        if category:
            query += " AND category = %s"
            params.append(category)
        query += " ORDER BY created_at DESC"

        with db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, tuple(params))
            return cursor.fetchall()

    @staticmethod
    def get_by_id(product_id):
        with db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
            return cursor.fetchone()

    @staticmethod
    def create(name, category, price, quantity):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO products (name, category, price, quantity)
                VALUES (%s, %s, %s, %s)
                """,
                (name, category, price, quantity),
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def update(product_id, name, category, price, quantity):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE products
                SET name=%s, category=%s, price=%s, quantity=%s
                WHERE id=%s
                """,
                (name, category, price, quantity, product_id),
            )
            conn.commit()
            return cursor.rowcount

    @staticmethod
    def delete(product_id):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
            conn.commit()
            return cursor.rowcount

    @staticmethod
    def adjust_stock(product_id, new_quantity):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET quantity=%s WHERE id=%s", (new_quantity, product_id))
            conn.commit()
