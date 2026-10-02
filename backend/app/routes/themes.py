from flask import Blueprint, jsonify
from app.extensions import db
from app.models.theme import Theme
from app.services.cache_service import metadata_cache

themes_bp = Blueprint('themes', __name__, url_prefix='/api/v1/themes')


@themes_bp.route('', methods=['GET'])
def get_themes():
    """
    GET /api/v1/themes
    Returns all available travel themes/interests with metadata caching.
    """
    def _fetch():
        themes = Theme.query.order_by(Theme.name.asc()).all()
        return [item.to_dict() for item in themes]

    data = metadata_cache.get_or_set("all_themes", _fetch, ttl_seconds=300)
    return jsonify({
        "success": True,
        "data": data
    }), 200


@themes_bp.route('/<int:theme_id>', methods=['GET'])
def get_theme(theme_id):
    """
    GET /api/v1/themes/<id>
    Returns single theme by ID or 404 if not found.
    """
    theme = db.session.get(Theme, theme_id)
    if not theme:
        return jsonify({
            "success": False,
            "error": {
                "message": f"Theme with id {theme_id} not found"
            }
        }), 404

    return jsonify({
        "success": True,
        "data": theme.to_dict()
    }), 200
