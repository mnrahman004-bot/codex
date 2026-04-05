"""Transaction routes."""
from flask import Blueprint

from backend.auth import token_required
from backend.controllers.transaction_controller import TransactionController

transaction_bp = Blueprint("transaction_bp", __name__)


@transaction_bp.route("/transactions", methods=["GET"])
@token_required
def list_transactions():
    return TransactionController.list_transactions()


@transaction_bp.route("/transactions", methods=["POST"])
@token_required
def create_transaction():
    return TransactionController.create_transaction()
