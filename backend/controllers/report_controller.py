"""Reporting controller logic."""
import csv
import io

from flask import Response, jsonify

from backend.config.db import db


class ReportController:
    """Controller for dashboard analytics and report export."""

    @staticmethod
    def dashboard():
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor(dictionary=True)

                cursor.execute("SELECT COUNT(*) AS total_products FROM products")
                total_products = cursor.fetchone()["total_products"]

                cursor.execute("SELECT COALESCE(SUM(price * quantity), 0) AS total_stock_value FROM products")
                total_stock_value = float(cursor.fetchone()["total_stock_value"])

                cursor.execute("SELECT COUNT(*) AS low_stock FROM products WHERE quantity < 10")
                low_stock = cursor.fetchone()["low_stock"]

                cursor.execute(
                    "SELECT category, SUM(quantity) AS total FROM products GROUP BY category ORDER BY total DESC"
                )
                category_distribution = cursor.fetchall()

                cursor.execute(
                    """
                    SELECT DATE(date) AS day,
                           SUM(CASE WHEN type='OUT' THEN quantity ELSE 0 END) AS sales,
                           SUM(CASE WHEN type='IN' THEN quantity ELSE 0 END) AS purchases
                    FROM transactions
                    GROUP BY DATE(date)
                    ORDER BY day ASC
                    """
                )
                trend = cursor.fetchall()

            return (
                jsonify(
                    {
                        "total_products": total_products,
                        "total_stock_value": total_stock_value,
                        "low_stock": low_stock,
                        "category_distribution": category_distribution,
                        "trend": trend,
                    }
                ),
                200,
            )
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500

    @staticmethod
    def export_csv():
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(
                    """
                    SELECT t.id, p.name AS product_name, t.type, t.quantity, t.date
                    FROM transactions t
                    JOIN products p ON p.id = t.product_id
                    ORDER BY t.date DESC
                    """
                )
                rows = cursor.fetchall()

            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=["id", "product_name", "type", "quantity", "date"])
            writer.writeheader()
            writer.writerows(rows)

            return Response(
                output.getvalue(),
                mimetype="text/csv",
                headers={"Content-Disposition": "attachment; filename=transactions_report.csv"},
            )
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500
