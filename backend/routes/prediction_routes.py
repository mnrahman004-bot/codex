"""Prediction routes."""
from flask import Blueprint

from backend.auth import token_required
from backend.controllers.prediction_controller import PredictionController

prediction_bp = Blueprint("prediction_bp", __name__)


@prediction_bp.route("/predict/<int:product_id>", methods=["GET"])
@token_required
def predict(product_id):
    return PredictionController.predict(product_id)
