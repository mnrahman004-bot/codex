"""Authentication routes."""
from flask import Blueprint

from backend.controllers.auth_controller import AuthController

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    return AuthController.login()
