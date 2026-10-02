from decimal import Decimal
from flask import Blueprint, jsonify, request
from sqlalchemy import func, or_
from sqlalchemy.orm import selectinload

from app.models.package import Package
from app.models.theme import Theme
from app.services.recommendation_service import generate_destination_reasons

discover_bp = Blueprint('discover', __name__, url_prefix='/api/v1/discover')

VALID_TRAVEL_TYPES = {'Solo', 'Couple', 'Family', 'Group'}


@discover_bp.route('/destinations', methods=['GET'])
def discover_destinations():
    """
    GET /api/v1/discover/destinations
    Deterministic, package-backed destination discovery.
    """
    # 1. Validate starting_city (required, string)
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
    interest_clean = interest.strip().lower()

    # 6. Validate travel_type (required, string in VALID_TRAVEL_TYPES)
    travel_type_param = request.args.get('travel_type')
    if not travel_type_param or not travel_type_param.strip():
        return jsonify({
            "success": False,
            "error": {
                "message": "Missing required parameter: 'travel_type'."
            }
        }), 400
    normalized_travel_type = travel_type_param.strip().capitalize()
    if normalized_travel_type not in VALID_TRAVEL_TYPES:
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

    # 8. Validate limit (optional, integer 1–20, default 10)
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

    # -------------------------------------------------------------
    # HARD MATCHING CONSTRAINTS:
    # 1. Package.is_active = True
    # 2. starting_city matches packages.starting_city case-insensitively
    # 3. interest matches Theme.name or Theme.slug case-insensitively
    #
    # BUDGET:
    # Prefer packages within requested budget (price_per_person * travellers <= budget)
    # If at least one exists, use within-budget packages.
    # If none exist, allow packages up to 20% above budget.
    # -------------------------------------------------------------
    base_query = Package.query.filter(
        Package.is_active.is_(True),
        func.lower(Package.starting_city) == starting_city.lower(),
        Package.themes.any(
            or_(
                func.lower(Theme.name) == interest_clean,
                func.lower(Theme.slug) == interest_clean
            )
        )
    )

    within_budget_cond = (Package.price_per_person <= (budget / Decimal(travellers)))
    has_within = base_query.filter(within_budget_cond).first() is not None
    if has_within:
        candidate_query = base_query.filter(within_budget_cond)
    else:
        max_fallback_price = (budget * Decimal('1.20')) / Decimal(travellers)
        candidate_query = base_query.filter(Package.price_per_person <= max_fallback_price)

    candidate_packages = (
        candidate_query
        .distinct()
        .options(
            selectinload(Package.destination),
            selectinload(Package.themes),
            selectinload(Package.travel_types),
            selectinload(Package.availability_months)
        )
        .all()
    )

    if not candidate_packages:
        return jsonify({
            "success": True,
            "data": [],
            "message": "No destinations currently have packages matching your selected travel interest and requirements."
        }), 200

    # -------------------------------------------------------------
    # DETERMINISTIC DISCOVERY SCORING (Max = 100):
    # Starting city = +15 (Hard constraint, always awarded)
    # Interest match = +35 (Theme name or slug case-insensitively)
    # Budget fit = +20 max (+20 within budget, +10 1-10% over, +5 10-20% over)
    # Duration match = +15 max (diff 0: +15, 1: +12, 2: +9, 3: +6, >3: +3)
    # Travel type match = +10 (matching travel type)
    # Month availability = +5 (available in requested month)
    # -------------------------------------------------------------
    scored_packages = []
    for pkg in candidate_packages:
        score = 15  # Starting city hard match

        # Interest match (+35)
        has_interest_match = any(
            t.name.lower() == interest_clean or t.slug.lower() == interest_clean
            for t in pkg.themes
        )
        if has_interest_match:
            score += 35

        # Budget fit (+20 max)
        pkg_cost = round(float(pkg.price_per_person) * travellers, 2)
        if pkg_cost <= float(budget):
            score += 20
            is_budget_fit = True
        else:
            is_budget_fit = False
            over_pct = ((pkg_cost - float(budget)) / float(budget)) * 100.0
            if over_pct <= 10.0:
                score += 10
            elif over_pct <= 20.0:
                score += 5

        # Duration match (+15 max)
        duration_diff = abs(pkg.duration_days - duration_days)
        if duration_diff == 0:
            score += 15
        elif duration_diff == 1:
            score += 12
        elif duration_diff == 2:
            score += 9
        elif duration_diff == 3:
            score += 6
        else:
            score += 3

        # Travel type match (+10)
        has_travel_type_match = any(
            tt.travel_type == normalized_travel_type
            for tt in pkg.travel_types
        )
        if has_travel_type_match:
            score += 10

        # Month match (+5)
        has_month_match = any(
            m.month == month
            for m in pkg.availability_months
        )
        if has_month_match:
            score += 5

        scored_packages.append({
            'package': pkg,
            'score': score,
            'estimated_total_cost': pkg_cost,
            'is_budget_fit': is_budget_fit
        })

    # -------------------------------------------------------------
    # DESTINATION AGGREGATION:
    # Group scored packages by destination_id
    # -------------------------------------------------------------
    destinations_map = {}
    for item in scored_packages:
        pkg = item['package']
        pkg_score = item['score']
        pkg_cost = item['estimated_total_cost']
        pkg_budget_fit = item['is_budget_fit']
        dest_id = pkg.destination_id

        if dest_id not in destinations_map:
            dest = pkg.destination
            destinations_map[dest_id] = {
                'destination_id': dest.id,
                'destination_name': dest.name,
                'country': dest.country,
                'region': dest.region,
                'description': dest.description,
                'image_url': dest.image_url,
                'match_score': pkg_score,
                'matching_package_count': 1,
                'lowest_price_per_person': float(pkg.price_per_person),
                'lowest_estimated_total_cost': pkg_cost,
                'best_matching_package_id': pkg.id,
                'best_matching_package_name': pkg.name,
                '_best_package_score': pkg_score,
                '_is_budget_fit': pkg_budget_fit,
                '_packages': [pkg]
            }
        else:
            d = destinations_map[dest_id]
            d['matching_package_count'] += 1
            d['_packages'].append(pkg)

            if float(pkg.price_per_person) < d['lowest_price_per_person']:
                d['lowest_price_per_person'] = float(pkg.price_per_person)
            if pkg_cost < d['lowest_estimated_total_cost']:
                d['lowest_estimated_total_cost'] = pkg_cost
            if pkg_budget_fit:
                d['_is_budget_fit'] = True

            # Best matching package: highest score, tie-break by budget fit, then lowest cost, then lowest id
            is_better = (
                pkg_score > d['_best_package_score'] or
                (pkg_score == d['_best_package_score'] and pkg_budget_fit and not d['_is_budget_fit']) or
                (pkg_score == d['_best_package_score'] and pkg_budget_fit == d['_is_budget_fit'] and pkg_cost < d['lowest_estimated_total_cost']) or
                (pkg_score == d['_best_package_score'] and pkg_budget_fit == d['_is_budget_fit'] and pkg_cost == d['lowest_estimated_total_cost'] and pkg.id < d['best_matching_package_id'])
            )
            if is_better:
                d['_best_package_score'] = pkg_score
                d['match_score'] = max(d['match_score'], pkg_score)
                d['best_matching_package_id'] = pkg.id
                d['best_matching_package_name'] = pkg.name
            else:
                d['match_score'] = max(d['match_score'], pkg_score)

    # Generate explainable match reasons & mismatches per destination
    for d in destinations_map.values():
        reasons, mismatches = generate_destination_reasons(
            destination_name=d['destination_name'],
            matching_packages=d['_packages'],
            budget=budget,
            travellers=travellers,
            duration_days=duration_days,
            interest=interest,
            travel_type=normalized_travel_type,
            month=month
        )
        d['match_reasons'] = reasons
        d['mismatches'] = mismatches

    # -------------------------------------------------------------
    # SORTING / RANKING:
    # 1. match_score DESC
    # 2. budget-fit destinations first
    # 3. matching_package_count DESC
    # 4. lowest_estimated_total_cost ASC
    # 5. destination_name ASC (case-insensitive)
    # -------------------------------------------------------------
    results = list(destinations_map.values())
    results.sort(
        key=lambda x: (
            -x['match_score'],
            0 if x['_is_budget_fit'] else 1,
            -x['matching_package_count'],
            x['lowest_estimated_total_cost'],
            x['destination_name'].lower()
        )
    )

    for r in results:
        r.pop('_best_package_score', None)
        r.pop('_is_budget_fit', None)
        r.pop('_packages', None)

    # Apply limit
    results = results[:limit]

    return jsonify({
        "success": True,
        "data": results
    }), 200
