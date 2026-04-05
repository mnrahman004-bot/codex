"""Product routes."""
from flask import Blueprint

from backend.auth import token_required
from backend.controllers.product_controller import ProductController

product_bp = Blueprint("product_bp", __name__)


@product_bp.route("/products", methods=["GET"])
@token_required
def list_products():
    return ProductController.list_products()


@product_bp.route("/products", methods=["POST"])
@token_required
def create_product():
    return ProductController.create_product()


@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@token_required
def update_product(product_id):
    return ProductController.update_product(product_id)


@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
@token_required
def delete_product(product_id):
    return ProductController.delete_product(product_id)
