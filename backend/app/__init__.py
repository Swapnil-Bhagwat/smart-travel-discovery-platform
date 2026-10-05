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
import logging
import traceback
from werkzeug.exceptions import HTTPException


def create_app(config_class=Config):
    """Application factory for the Flask backend."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # In production (e.g. Render / Gunicorn), bridge Gunicorn error handlers so logs appear in console
    gunicorn_logger = logging.getLogger('gunicorn.error')
    if gunicorn_logger.handlers:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    # Enable Cross-Origin Resource Sharing with configurable origins for production safety
    cors_origins_env = os.environ.get('CORS_ORIGINS', '*')
    if cors_origins_env == '*':
        cors_origins = '*'
    else:
        cors_origins = [o.strip() for o in cors_origins_env.split(',') if o.strip()]

    CORS(app, resources={r"/api/*": {"origins": cors_origins}})

    # Strip MySQL/TiDB-specific connect_args if testing with SQLite
    db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', '')
    if db_uri.startswith('sqlite') and 'SQLALCHEMY_ENGINE_OPTIONS' in app.config:
        engine_opts = app.config['SQLALCHEMY_ENGINE_OPTIONS']
        if isinstance(engine_opts, dict) and 'connect_args' in engine_opts:
            engine_opts = dict(engine_opts)
            engine_opts.pop('connect_args', None)
            app.config['SQLALCHEMY_ENGINE_OPTIONS'] = engine_opts

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
        app.logger.error("Internal Server Error (500): %s\n%s", error, traceback.format_exc())
        return jsonify({
            "success": False,
            "error": {
                "message": "Internal server error"
            }
        }), 500

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        if error.code and error.code >= 500:
            app.logger.error("HTTPException (%s): %s\n%s", error.code, error, traceback.format_exc())
            return jsonify({
                "success": False,
                "error": {
                    "message": "Internal server error"
                }
            }), 500
        return jsonify({
            "success": False,
            "error": {
                "message": error.description or "Request failed"
            }
        }), error.code

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        if isinstance(error, HTTPException):
            if error.code and error.code >= 500:
                app.logger.error("HTTPException (%s): %s\n%s", error.code, error, traceback.format_exc())
                return jsonify({
                    "success": False,
                    "error": {
                        "message": "Internal server error"
                    }
                }), 500
            return jsonify({
                "success": False,
                "error": {
                    "message": error.description or "Request failed"
                }
            }), error.code

        # Log full Python traceback to stderr/stdout for production debugging
        app.logger.error("Unhandled Exception: %s\n%s", error, traceback.format_exc())
        return jsonify({
            "success": False,
            "error": {
                "message": "Internal server error"
            }
        }), 500

    return app
