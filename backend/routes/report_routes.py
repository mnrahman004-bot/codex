"""Dashboard and reporting routes."""
from flask import Blueprint

from backend.auth import token_required
from backend.controllers.report_controller import ReportController

report_bp = Blueprint("report_bp", __name__)


@report_bp.route("/dashboard", methods=["GET"])
@token_required
def dashboard():
    return ReportController.dashboard()


@report_bp.route("/reports/export", methods=["GET"])
@token_required
def export_csv():
    return ReportController.export_csv()
