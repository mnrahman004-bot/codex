"""Database configuration and helper utilities."""
import os
from contextlib import contextmanager

import mysql.connector
from mysql.connector import Error


class Database:
    """Simple database connector wrapper for MySQL operations."""

    def __init__(self):
        self.config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": int(os.getenv("DB_PORT", "3306")),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", ""),
            "database": os.getenv("DB_NAME", "inventory_db"),
        }

    @contextmanager
    def get_connection(self):
        """Yield a MySQL connection and ensure it closes properly."""
        connection = None
        try:
            connection = mysql.connector.connect(**self.config)
            yield connection
        except Error as exc:
            raise RuntimeError(f"Database connection error: {exc}") from exc
        finally:
            if connection and connection.is_connected():
                connection.close()


db = Database()
