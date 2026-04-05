"""Authentication controller logic."""
import os
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from flask import jsonify, request

from backend.models.user_model import UserModel


class AuthController:
    """Controller for login and token issuance."""

    @staticmethod
    def login():
        try:
            data = request.get_json() or {}
            username = data.get("username", "").strip()
            password = data.get("password", "")

            if not username or not password:
                return jsonify({"error": "Username and password are required."}), 400

            user = UserModel.get_by_username(username)
            if not user:
                return jsonify({"error": "Invalid credentials."}), 401

            if not bcrypt.checkpw(password.encode("utf-8"), user["password_hash"].encode("utf-8")):
                return jsonify({"error": "Invalid credentials."}), 401

            payload = {
                "sub": str(user["id"]),
                "username": user["username"],
                "exp": datetime.now(timezone.utc) + timedelta(hours=12),
            }
            token = jwt.encode(payload, os.getenv("JWT_SECRET", "dev-secret"), algorithm="HS256")
            return jsonify({"token": token, "username": user["username"]}), 200
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500
