from flask import Flask, jsonify
from flask_cors import CORS
from app.config import Config
from app.extensions import db, migrate
from app.routes import (
    health_bp,
    destinations_bp,
    operators_bp,
    themes_bp,
    packages_bp,
    discover_bp,
    recommendations_bp,
    providers_bp,
)


import os
from werkzeug.exceptions import HTTPException


def create_app(config_class=Config):
    """Application factory for the Flask backend."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Enable Cross-Origin Resource Sharing with configurable origins for production safety
    cors_origins_env = os.environ.get('CORS_ORIGINS', '*')
    if cors_origins_env == '*':
        cors_origins = '*'
    else:
        cors_origins = [o.strip() for o in cors_origins_env.split(',') if o.strip()]

    CORS(app, resources={r"/api/*": {"origins": cors_origins}})

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to ensure metadata is registered with SQLAlchemy
    from app import models  # noqa: F401

    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(destinations_bp)
    app.register_blueprint(operators_bp)
    app.register_blueprint(themes_bp)
    app.register_blueprint(packages_bp)
    app.register_blueprint(discover_bp)
    app.register_blueprint(recommendations_bp)
    app.register_blueprint(providers_bp)

    # Consistent JSON error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
            "success": False,
            "error": {
                "message": "Resource not found"
            }
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": {
                "message": "Internal server error"
            }
        }), 500

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return jsonify({
            "success": False,
            "error": {
                "message": error.description or "Request failed"
            }
        }), error.code

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        # Do not expose internal stack trace or credentials in responses
        return jsonify({
            "success": False,
            "error": {
                "message": "Internal server error"
            }
        }), 500

    return app
