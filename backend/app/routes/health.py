from sys import prefix
from flask import Blueprint


health_bp = Blueprint("health", __name__, url_prefix="/health")

@health_bp.route("/")
def health_check():
    return {"status": "ok"}