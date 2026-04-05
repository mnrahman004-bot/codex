"""Product controller logic."""
from flask import jsonify, request

from backend.models.product_model import ProductModel


class ProductController:
    """Controller for product CRUD endpoints."""

    @staticmethod
    def list_products():
        try:
            search = request.args.get("search")
            category = request.args.get("category")
            products = ProductModel.list_products(search=search, category=category)
            return jsonify(products), 200
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500

    @staticmethod
    def create_product():
        try:
            data = request.get_json() or {}
            required = ["name", "category", "price", "quantity"]
            if any(field not in data for field in required):
                return jsonify({"error": "name, category, price, quantity are required."}), 400

            product_id = ProductModel.create(data["name"], data["category"], data["price"], data["quantity"])
            return jsonify({"message": "Product created", "id": product_id}), 201
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500

    @staticmethod
    def update_product(product_id):
        try:
            data = request.get_json() or {}
            updated = ProductModel.update(
                product_id,
                data.get("name"),
                data.get("category"),
                data.get("price"),
                data.get("quantity"),
            )
            if updated == 0:
                return jsonify({"error": "Product not found."}), 404
            return jsonify({"message": "Product updated"}), 200
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500

    @staticmethod
    def delete_product(product_id):
        try:
            deleted = ProductModel.delete(product_id)
            if deleted == 0:
                return jsonify({"error": "Product not found."}), 404
            return jsonify({"message": "Product deleted"}), 200
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500
