"""JWT authentication decorator for protected routes."""
import os
from functools import wraps

import jwt
from flask import jsonify, request


def token_required(func):
    """Validate bearer token and gate API endpoints."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing bearer token"}), 401

        token = auth_header.split(" ", 1)[1]
        try:
            jwt.decode(token, os.getenv("JWT_SECRET", "dev-secret"), algorithms=["HS256"])
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 401
        return func(*args, **kwargs)

    return wrapper
