from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound


error_bp = Blueprint("errors", __name__)


@error_bp.app_errorhandler(Exception)
def handle_generic_errors(err:Exception):
    return jsonify({"message": "Unknow error", "error": err.__str__() }), 500


@error_bp.app_errorhandler(NotFound)
def not_found_error_handler(err):
    return jsonify({"message": "This resource isn´t available"}), 404
