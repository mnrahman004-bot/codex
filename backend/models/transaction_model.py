"""Transaction data access layer."""
from backend.config.db import db


class TransactionModel:
    """Model for transaction history operations."""

    @staticmethod
    def list_transactions():
        with db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT t.id, t.product_id, p.name AS product_name, t.type, t.quantity, t.date
                FROM transactions t
                JOIN products p ON p.id = t.product_id
                ORDER BY t.date DESC
                """
            )
            return cursor.fetchall()

    @staticmethod
    def create(product_id, transaction_type, quantity):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO transactions (product_id, type, quantity)
                VALUES (%s, %s, %s)
                """,
                (product_id, transaction_type, quantity),
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_product_history(product_id):
        with db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT date, quantity, type FROM transactions WHERE product_id=%s ORDER BY date ASC",
                (product_id,),
            )
            return cursor.fetchall()
