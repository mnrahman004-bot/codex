"""Transaction controller logic."""
from flask import jsonify, request

from backend.models.product_model import ProductModel
from backend.models.transaction_model import TransactionModel


class TransactionController:
    """Controller for transaction APIs and stock adjustments."""

    @staticmethod
    def list_transactions():
        try:
            transactions = TransactionModel.list_transactions()
            return jsonify(transactions), 200
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500

    @staticmethod
    def create_transaction():
        try:
            data = request.get_json() or {}
            product_id = data.get("product_id")
            transaction_type = data.get("type")
            quantity = int(data.get("quantity", 0))

            if transaction_type not in {"IN", "OUT"}:
                return jsonify({"error": "type must be IN or OUT"}), 400
            if quantity <= 0:
                return jsonify({"error": "quantity must be positive"}), 400

            product = ProductModel.get_by_id(product_id)
            if not product:
                return jsonify({"error": "Product not found"}), 404

            current_qty = int(product["quantity"])
            if transaction_type == "IN":
                new_qty = current_qty + quantity
            else:
                if current_qty - quantity < 0:
                    return jsonify({"error": "Insufficient stock"}), 400
                new_qty = current_qty - quantity

            TransactionModel.create(product_id, transaction_type, quantity)
            ProductModel.adjust_stock(product_id, new_qty)
            return jsonify({"message": "Transaction recorded", "new_quantity": new_qty}), 201
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500
