from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.destination import Destination

destinations_bp = Blueprint('destinations', __name__, url_prefix='/api/v1/destinations')


@destinations_bp.route('', methods=['GET'])
def get_destinations():
    """
    GET /api/v1/destinations
    Returns paginated list of destinations with optional search and country filter.
    """
    # Validate and parse pagination parameters
    page_str = request.args.get('page', '1')
    per_page_str = request.args.get('per_page', '20')

    try:
        page = int(page_str)
        per_page = int(per_page_str)
        if page < 1 or per_page < 1:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameters 'page' and 'per_page' must be positive integers."
                }
            }), 400
    except ValueError:
        return jsonify({
            "success": False,
            "error": {
                "message": "Invalid 'page' or 'per_page' parameter. Must be integers."
            }
        }), 400

    # Cap per_page to reasonable limit
    if per_page > 100:
        per_page = 100

    # Build query
    query = Destination.query

    # Optional search by destination name
    search = request.args.get('search', '').strip() or request.args.get('name', '').strip()
    if search:
        query = query.filter(Destination.name.ilike(f"%{search}%"))

    # Optional country filter
    country = request.args.get('country', '').strip()
    if country:
        query = query.filter(Destination.country.ilike(f"%{country}%"))

    # Execute pagination
    pagination = query.order_by(Destination.name.asc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        "success": True,
        "data": [item.to_dict() for item in pagination.items],
        "pagination": {
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages
        }
    }), 200


@destinations_bp.route('/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    """
    GET /api/v1/destinations/<id>
    Returns single destination by ID or 404 if not found.
    """
    destination = db.session.get(Destination, destination_id)
    if not destination:
        return jsonify({
            "success": False,
            "error": {
                "message": f"Destination with id {destination_id} not found"
            }
        }), 404

    return jsonify({
        "success": True,
        "data": destination.to_dict()
    }), 200
