"""
Recommendation routes for travel packages.
Step 7 - Smart Travel Discovery and Comparison Platform.
"""
from decimal import Decimal
from flask import Blueprint, jsonify, request

from app.services.recommendation_service import get_package_recommendations

recommendations_bp = Blueprint('recommendations', __name__, url_prefix='/api/v1/recommendations')

VALID_TRAVEL_TYPES = {'Solo', 'Couple', 'Family', 'Group'}


@recommendations_bp.route('/packages', methods=['GET'])
def recommend_packages():
    """
    GET /api/v1/recommendations/packages
    Deterministic, explainable package recommendations with ground-truth reasons and mismatches.
    """
    # 1. Validate starting_city (required, non-empty string)
    starting_city = request.args.get('starting_city')
    if not starting_city or not starting_city.strip():
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'starting_city'."
            }
        }), 400
    starting_city = starting_city.strip()

    # 2. Validate budget (required, number >= 0)
    budget_param = request.args.get('budget')
    if budget_param is None or budget_param.strip() == '':
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'budget'."
            }
        }), 400
    try:
        budget = Decimal(budget_param.strip())
        if budget < 0:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'budget' must be a non-negative number."
                }
            }), 400
    except Exception:
        return jsonify({
            "success": False,
            "error": {
                "message": "Parameter 'budget' must be a non-negative number."
            }
        }), 400

    # 3. Validate travellers (required, integer >= 1)
    travellers_param = request.args.get('travellers')
    if travellers_param is None or travellers_param.strip() == '':
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'travellers'."
            }
        }), 400
    try:
        travellers = int(travellers_param.strip())
        if travellers < 1:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'travellers' must be an integer greater than or equal to 1."
                }
            }), 400
    except ValueError:
        return jsonify({
            "success": False,
            "error": {
                "message": "Parameter 'travellers' must be an integer greater than or equal to 1."
            }
        }), 400

    # 4. Validate duration_days (required, integer > 0)
    duration_param = request.args.get('duration_days')
    if duration_param is None or duration_param.strip() == '':
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'duration_days'."
            }
        }), 400
    try:
        duration_days = int(duration_param.strip())
        if duration_days <= 0:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'duration_days' must be a positive integer."
                }
            }), 400
    except ValueError:
        return jsonify({
            "success": False,
            "error": {
                "message": "Parameter 'duration_days' must be a positive integer."
            }
        }), 400

    # 5. Validate interest (required, string)
    interest = request.args.get('interest')
    if not interest or not interest.strip():
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'interest'."
            }
        }), 400
    interest = interest.strip()

    # 6. Validate travel_type (required, string in VALID_TRAVEL_TYPES)
    travel_type_param = request.args.get('travel_type')
    if not travel_type_param or not travel_type_param.strip():
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'travel_type'."
            }
        }), 400
    travel_type_clean = travel_type_param.strip().capitalize()
    if travel_type_clean not in VALID_TRAVEL_TYPES:
        return jsonify({
            "success": False,
            "error": {
                "message": "Parameter 'travel_type' must be one of: Solo, Couple, Family, Group."
            }
        }), 400

    # 7. Validate month (required, integer 1–12)
    month_param = request.args.get('month')
    if month_param is None or month_param.strip() == '':
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'month'."
            }
        }), 400
    try:
        month = int(month_param.strip())
        if month < 1 or month > 12:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'month' must be an integer between 1 and 12."
                }
            }), 400
    except ValueError:
        return jsonify({
            "success": False,
            "error": {
                "message": "Parameter 'month' must be an integer between 1 and 12."
            }
        }), 400

    # 8. Validate destination_id (optional, integer >= 1)
    destination_id = None
    destination_id_param = request.args.get('destination_id')
    if destination_id_param is not None and destination_id_param.strip() != '':
        try:
            destination_id = int(destination_id_param.strip())
            if destination_id < 1:
                return jsonify({
                    "success": False,
                    "error": {
                        "message": "Parameter 'destination_id' must be a positive integer."
                    }
                }), 400
        except ValueError:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'destination_id' must be a positive integer."
                }
            }), 400

    # 9. Validate limit (optional, integer 1–20, default 10)
    limit = 10
    limit_param = request.args.get('limit')
    if limit_param is not None and limit_param.strip() != '':
        try:
            limit = int(limit_param.strip())
            if limit < 1 or limit > 20:
                return jsonify({
                    "success": False,
                    "error": {
                        "message": "Parameter 'limit' must be an integer between 1 and 20."
                    }
                }), 400
        except ValueError:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'limit' must be an integer between 1 and 20."
                }
            }), 400

    # Execute recommendation service
    recommended_packages = get_package_recommendations(
        starting_city=starting_city,
        budget=budget,
        travellers=travellers,
        duration_days=duration_days,
        interest=interest,
        travel_type=travel_type_clean,
        month=month,
        destination_id=destination_id,
        limit=limit
    )

    response_payload = {
        "success": True,
        "data": recommended_packages,
        "pagination": {
            "total": len(recommended_packages),
            "limit": limit
        }
    }

    if not recommended_packages:
        response_payload["message"] = (
            "No recommended packages match your selected travel interest and requirements. "
            "Try another interest or adjust your other preferences."
        )

    return jsonify(response_payload), 200
