from decimal import Decimal
from flask import Blueprint, jsonify, request
from sqlalchemy import func, or_
from sqlalchemy.orm import selectinload

from app.extensions import db
from app.models.destination import Destination
from app.models.operator import Operator
from app.models.package import (
    Package,
    PackageAvailabilityMonth,
    PackageTravelType,
    package_themes,
)
from app.models.theme import Theme
from app.services.recommendation_service import MONTH_NAMES

packages_bp = Blueprint('packages', __name__, url_prefix='/api/v1/packages')

VALID_TRAVEL_TYPES = {'Solo', 'Couple', 'Family', 'Group'}


@packages_bp.route('', methods=['GET'])
def get_packages():
    """
    GET /api/v1/packages
    Search and filter travel packages with pagination.
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

    # 7. Validate & Parse Operator ID
    operator_id_param = request.args.get('operator_id')
    operator_id = None
    if operator_id_param is not None and operator_id_param.strip() != '':
        try:
            operator_id = int(operator_id_param.strip())
            if operator_id < 1:
                return jsonify({
                    "success": False,
                    "error": {
                        "message": "Parameter 'operator_id' must be a positive integer."
                    }
                }), 400
        except ValueError:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'operator_id' must be a positive integer."
                }
            }), 400

    # 8. Validate & Parse Pagination
    page_str = request.args.get('page', '1')
    per_page_str = request.args.get('per_page', '20')
    try:
        page = int(page_str)
        if page < 1:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'page' must be a positive integer."
                }
            }), 400
    except ValueError:
        return jsonify({
            "success": False,
            "error": {
                "message": "Parameter 'page' must be a positive integer."
            }
        }), 400

    try:
        per_page = int(per_page_str)
        if per_page < 1 or per_page > 100:
            return jsonify({
                "success": False,
                "error": {
                    "message": "Parameter 'per_page' must be an integer between 1 and 100."
                }
            }), 400
    except ValueError:
        return jsonify({
            "success": False,
            "error": {
                "message": "Parameter 'per_page' must be an integer between 1 and 100."
            }
        }), 400

    # Base query: Only return active packages
    query = Package.query.filter(Package.is_active.is_(True))

    # Optional Destination filter (Hard constraint when supplied)
    if destination_id is not None:
        query = query.filter(Package.destination_id == destination_id)

    # Optional Operator filter (Hard constraint when supplied)
    if operator_id is not None:
        query = query.filter(Package.operator_id == operator_id)

    # Optional Starting City filter (Hard constraint when supplied, case-insensitive)
    starting_city = request.args.get('starting_city')
    if starting_city is not None and starting_city.strip() != '':
        query = query.filter(func.lower(Package.starting_city) == starting_city.strip().lower())

    # Optional Interest filter (Hard constraint when supplied, case-insensitive matching on Theme.name or Theme.slug)
    interest = request.args.get('interest')
    interest_clean = interest.strip().lower() if interest is not None and interest.strip() != '' else None
    if interest_clean is not None:
        query = query.filter(
            Package.themes.any(
                or_(
                    func.lower(Theme.name) == interest_clean,
                    func.lower(Theme.slug) == interest_clean
                )
            )
        )

    # Budget handling & fallback:
    # 1. Prefer packages within requested budget (price_per_person * travellers <= budget)
    # 2. If at least one package is within budget, return within-budget packages
    # 3. If NO package is within budget, return closest packages up to 20% over budget
    if budget is not None:
        within_budget_cond = (Package.price_per_person <= (budget / Decimal(travellers)))
        has_within = query.filter(within_budget_cond).first() is not None
        if has_within:
            query = query.filter(within_budget_cond)
        else:
            max_fallback_price = (budget * Decimal('1.20')) / Decimal(travellers)
            query = query.filter(Package.price_per_person <= max_fallback_price)

    # Prevent duplicate rows and eagerly load relationships to avoid N+1 queries
    query = query.distinct().options(
        selectinload(Package.operator),
        selectinload(Package.destination),
        selectinload(Package.themes),
        selectinload(Package.travel_types),
        selectinload(Package.availability_months)
    )

    candidate_packages = query.all()

    # Deterministic scoring for package search:
    # Duration: max 25
    # Interest: max 25
    # Travel type: max 20
    # Month: max 15
    # Budget fit: max 15
    # Maximum = 100
    scored_packages = []
    for pkg in candidate_packages:
        score = 0
        pkg_cost = round(float(pkg.price_per_person) * travellers, 2)

        # 1. Duration (max 25)
        if duration_days is not None:
            diff = abs(pkg.duration_days - duration_days)
            if diff == 0:
                score += 25
            elif diff == 1:
                score += 20
            elif diff == 2:
                score += 15
            elif diff == 3:
                score += 10
            else:
                score += 5
        else:
            score += 25

        # 2. Interest (max 25)
        if interest_clean is not None:
            has_theme_match = any(
                t.name.lower() == interest_clean or t.slug.lower() == interest_clean
                for t in pkg.themes
            )
            if has_theme_match:
                score += 25
        else:
            score += 25

        # 3. Travel type (max 20)
        if travel_type is not None:
            has_type_match = any(
                tt.travel_type == travel_type
                for tt in pkg.travel_types
            )
            if has_type_match:
                score += 20
        else:
            score += 20

        # 4. Month (max 15)
        if month is not None:
            has_month_match = any(
                m.month == month
                for m in pkg.availability_months
            )
            if has_month_match:
                score += 15
        else:
            score += 15

        # 5. Budget fit (max 15)
        if budget is not None:
            if pkg_cost <= float(budget):
                score += 15
                b_status = "within_budget"
                b_diff = 0.0
            else:
                b_status = "over_budget"
                b_diff = round(pkg_cost - float(budget), 2)
                over_pct = ((pkg_cost - float(budget)) / float(budget)) * 100.0
                if over_pct <= 10.0:
                    score += 10
                elif over_pct <= 20.0:
                    score += 5
                else:
                    score += 0
        else:
            score += 15
            b_status = "within_budget"
            b_diff = 0.0

        # Build match reasons & mismatches if search criteria were provided
        match_reasons = []
        mismatches = []

        if starting_city:
            match_reasons.append(f"Departs from your starting city ({starting_city.strip()})")

        if interest_clean is not None:
            matched_theme = next(
                (t.name for t in pkg.themes if t.name.lower() == interest_clean or t.slug.lower() == interest_clean),
                interest.strip()
            )
            match_reasons.append(f"Matches your {matched_theme} interest")

        if budget is not None:
            if b_status == "within_budget":
                match_reasons.append(f"Fits your ₹{int(float(budget)):,} total budget")
            else:
                mismatches.append(f"₹{int(b_diff):,} above your selected budget")

        if duration_days is not None:
            diff = abs(pkg.duration_days - duration_days)
            if diff == 0:
                match_reasons.append(f"Matches your {duration_days}-day duration preference")
            elif diff == 1:
                if pkg.duration_days > duration_days:
                    match_reasons.append("Only 1 day longer than your preferred duration")
                else:
                    match_reasons.append("Only 1 day shorter than your preferred duration")
                mismatches.append(f"Package is {pkg.duration_days} days instead of your preferred {duration_days} days")
            else:
                mismatches.append(f"Package is {pkg.duration_days} days instead of your preferred {duration_days} days")

        if travel_type is not None:
            if has_type_match:
                match_reasons.append(f"Suitable for {travel_type} travel")
            else:
                avail_types = [tt.travel_type for tt in pkg.travel_types]
                types_str = ", ".join(avail_types) if avail_types else "other"
                mismatches.append(f"Designed for {types_str} travel")

        if month is not None:
            month_name = MONTH_NAMES.get(month, f"Month {month}")
            if has_month_match:
                match_reasons.append(f"Available in {month_name}")
            else:
                mismatches.append(f"Not listed for {month_name}")

        scored_packages.append({
            'package': pkg,
            'match_score': score,
            'budget_status': b_status,
            'budget_difference': b_diff,
            'estimated_total_cost': pkg_cost,
            'match_reasons': match_reasons if (match_reasons or mismatches) else None,
            'mismatches': mismatches if (match_reasons or mismatches) else None
        })

    # Sort package results:
    # 1. match_score DESC
    # 2. budget_status = within_budget before over_budget
    # 3. estimated_total_cost ASC
    # 4. package name ASC
    scored_packages.sort(
        key=lambda x: (
            -x['match_score'],
            0 if x['budget_status'] == 'within_budget' else 1,
            x['estimated_total_cost'],
            x['package'].name.lower()
        )
    )

    # Paginate results
    total = len(scored_packages)
    pages = (total + per_page - 1) // per_page if total > 0 else 0
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_items = scored_packages[start_idx:end_idx]

    response_payload = {
        "success": True,
        "data": [
            item['package'].to_summary_dict(
                requested_travellers=travellers,
                match_score=item['match_score'],
                budget_status=item['budget_status'],
                budget_difference=item['budget_difference'],
                match_reasons=item['match_reasons'],
                mismatches=item['mismatches']
            )
            for item in paginated_items
        ],
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total,
            "pages": pages
        }
    }
    if total == 0:
        response_payload["message"] = (
            "No packages match the selected travel interest and other requirements. "
            "Try another interest or adjust your other preferences."
        )

    return jsonify(response_payload), 200


@packages_bp.route('/<int:package_id>', methods=['GET'])
def get_package(package_id):
    """
    GET /api/v1/packages/<id>
    Returns complete package details including itinerary, inclusions, exclusions, and attributes.
    """
    # Optional travellers parameter for estimated total cost calculation
    travellers = 1
    travellers_param = request.args.get('travellers')
    if travellers_param is not None and travellers_param.strip() != '':
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

    # Query with eager loading for all details
    stmt = (
        db.select(Package)
        .options(
            selectinload(Package.operator),
            selectinload(Package.destination),
            selectinload(Package.themes),
            selectinload(Package.travel_types),
            selectinload(Package.availability_months),
            selectinload(Package.itineraries),
            selectinload(Package.inclusions),
            selectinload(Package.exclusions)
        )
        .filter(Package.id == package_id, Package.is_active.is_(True))
    )
    package = db.session.execute(stmt).scalar_one_or_none()

    if not package:
        return jsonify({
            "success": False,
            "error": {
                "message": f"Package with id {package_id} not found"
            }
        }), 404

    return jsonify({
        "success": True,
        "data": package.to_detail_dict(requested_travellers=travellers)
    }), 200
