from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.operator import Operator

operators_bp = Blueprint('operators', __name__, url_prefix='/api/v1/operators')


@operators_bp.route('', methods=['GET'])
def get_operators():
    """
    GET /api/v1/operators
    Returns paginated list of travel operators with optional search by name.
    """
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

    if per_page > 100:
        per_page = 100

    query = Operator.query

    # Optional search by operator name
    search = request.args.get('search', '').strip() or request.args.get('name', '').strip()
    if search:
        query = query.filter(Operator.name.ilike(f"%{search}%"))

    pagination = query.order_by(Operator.name.asc()).paginate(
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


@operators_bp.route('/<int:operator_id>', methods=['GET'])
def get_operator(operator_id):
    """
    GET /api/v1/operators/<id>
    Returns single operator by ID or 404 if not found.
    """
    operator = db.session.get(Operator, operator_id)
    if not operator:
        return jsonify({
            "success": False,
            "error": {
                "message": f"Operator with id {operator_id} not found"
            }
        }), 404

    return jsonify({
        "success": True,
        "data": operator.to_dict()
    }), 200
