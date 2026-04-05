"""Prediction controller logic."""
from flask import jsonify

from backend.ml.prediction import predict_demand
from backend.models.transaction_model import TransactionModel


class PredictionController:
    """Controller for stock demand predictions."""

    @staticmethod
    def predict(product_id):
        try:
            history = TransactionModel.get_product_history(product_id)
            result = predict_demand(history)
            return jsonify({"product_id": product_id, **result}), 200
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500
