"""
Provider Routes for Health and Unified Multi-Provider Search.
Step 9 - Provider-Ready Architecture.
"""

from decimal import Decimal
from flask import Blueprint, jsonify, request

from app.providers import provider_registry
from app.services.provider_search_service import provider_search_service
from app.services.cache_service import metadata_cache

providers_bp = Blueprint('providers', __name__, url_prefix='/api/v1/providers')

VALID_TRAVEL_TYPES = {'Solo', 'Couple', 'Family', 'Group'}


@providers_bp.route('', methods=['GET'])
def get_providers_health():
    """
    GET /api/v1/providers
    Returns status, source_type, and health of all registered inventory providers.
    Uses short-term metadata caching to avoid repeated pinging.
    """
    def _fetch_health():
        return provider_registry.get_health_status()

    # Cache provider health for 60 seconds
    health_data = metadata_cache.get_or_set("provider_health_status", _fetch_health, ttl_seconds=60)

    return jsonify({
        "success": True,
        "data": health_data
    }), 200


@providers_bp.route('/search', methods=['GET'])
def search_providers():
    """
    GET /api/v1/providers/search
    Unified search endpoint querying enabled providers and returning normalized packages.
    """
    # 1. Validate & Parse Travellers
    travellers_param = request.args.get('travellers', '1')
    try:
        travellers = int(travellers_param)
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

    # 2. Validate & Parse Budget
    budget_param = request.args.get('budget')
    budget = None
    if budget_param is not None and budget_param.strip() != '':
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

    # 3. Validate & Parse Duration Days
    duration_param = request.args.get('duration_days')
    duration_days = None
    if duration_param is not None and duration_param.strip() != '':
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

    # 4. Validate & Parse Month
    month_param = request.args.get('month')
    month = None
    if month_param is not None and month_param.strip() != '':
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

    # 5. Validate & Parse Travel Type
    travel_type_param = request.args.get('travel_type')
    travel_type = None
    if travel_type_param is not None and travel_type_param.strip() != '':
        normalized_type = travel_type_param.strip().capitalize()
        if normalized_type not in VALID_TRAVEL_TYPES:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'travel_type' must be one of: Solo, Couple, Family, Group."
                }
            }), 400
        travel_type = normalized_type

    # 6. Validate & Parse Destination ID
    destination_id_param = request.args.get('destination_id')
    destination_id = None
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

    # 7. Validate & Parse Limit
    limit_param = request.args.get('limit')
    limit = None
    if limit_param is not None and limit_param.strip() != '':
        try:
            limit = int(limit_param.strip())
            if limit < 1 or limit > 100:
                return jsonify({
                    "success": False,
                    "error": {
                        "message": "Parameter 'limit' must be an integer between 1 and 100."
                    }
                }), 400
        except ValueError:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'limit' must be an integer between 1 and 100."
                }
            }), 400

    # 8. Optional provider filter
    provider_name = request.args.get('provider')
    if provider_name and provider_name.strip():
        provider_name = provider_name.strip().lower()
        if not provider_registry.get(provider_name):
            return jsonify({
                "success": False,
                "error": {
                    "message": f"Provider '{provider_name}' is not recognized."
                }
            }), 400

    starting_city = request.args.get('starting_city')
    interest = request.args.get('interest')

    criteria = {
        'starting_city': starting_city.strip() if starting_city and starting_city.strip() else None,
        'budget': budget,
        'travellers': travellers,
        'duration_days': duration_days,
        'interest': interest.strip() if interest and interest.strip() else None,
        'travel_type': travel_type,
        'month': month,
        'destination_id': destination_id,
        'limit': limit
    }

    normalized_results = provider_search_service.search(criteria=criteria, provider_name=provider_name)

    data_payload = [p.to_dict() for p in normalized_results]

    response_payload = {
        "success": True,
        "data": data_payload,
        "pagination": {
            "total": len(data_payload),
            "limit": limit
        }
    }

    if not data_payload:
        response_payload["message"] = (
            "No packages match the selected criteria across available providers."
        )

    return jsonify(response_payload), 200
