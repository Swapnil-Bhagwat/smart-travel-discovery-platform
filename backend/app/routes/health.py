from flask import Blueprint, jsonify
from sqlalchemy import text
from app.extensions import db

health_bp = Blueprint('health', __name__, url_prefix='/api/v1')


@health_bp.route('/health', methods=['GET'])
def health_check():
    """Basic health endpoint returning service status."""
    return jsonify({
        "success": True,
        "status": "ok",
        "data": {
            "status": "ok"
        }
    }), 200


@health_bp.route('/health/db', methods=['GET'])
def database_health_check():
    """Database health endpoint verifying connection to MySQL."""
    try:
        # Execute simple query to verify connection
        db.session.execute(text('SELECT 1'))
        return jsonify({
            "success": True,
            "status": "ok",
            "database": "connected",
            "data": {
                "status": "ok",
                "database": "connected"
            }
        }), 200
    except Exception:
        # Sanitize any error output to prevent exposing credentials
        return jsonify({
            "success": False,
            "status": "error",
            "database": "disconnected",
            "error": {
                "message": "Database connection failed"
            }
        }), 503
