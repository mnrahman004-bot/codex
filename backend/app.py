"""Flask application entrypoint for inventory system APIs."""
import os

from flask import Flask, jsonify
from flask_cors import CORS

from backend.routes.auth_routes import auth_bp
from backend.routes.prediction_routes import prediction_bp
from backend.routes.product_routes import product_bp
from backend.routes.report_routes import report_bp
from backend.routes.transaction_routes import transaction_bp


def create_app():
    """Create and configure Flask app with modular route blueprints."""
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGIN", "*")}})

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(product_bp, url_prefix="/api")
    app.register_blueprint(transaction_bp, url_prefix="/api")
    app.register_blueprint(report_bp, url_prefix="/api")
    app.register_blueprint(prediction_bp, url_prefix="/api")

    @app.route("/api/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "ok"}), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
