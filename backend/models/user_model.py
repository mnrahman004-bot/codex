"""User data access layer."""
from backend.config.db import db


class UserModel:
    """Model for user authentication queries."""

    @staticmethod
    def get_by_username(username):
        with db.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cursor.fetchone()
