"""
Deterministic, explainable recommendation engine for travel packages and destinations.
Step 7 - Smart Travel Discovery and Comparison Platform.
"""
from decimal import Decimal
from typing import Any, Dict, List, Optional, Tuple, Union
from sqlalchemy import func, or_
from sqlalchemy.orm import selectinload

from app.extensions import db
from app.models.package import Package
from app.models.theme import Theme

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

PROHIBITED_UNSUPPORTED_CLAIMS = [
    "most popular", "best choice", "highly recommended",
    "loved by travellers", "trending", "perfect for you"
]


def _get_pkg_themes(pkg: Any) -> List[Tuple[str, str]]:
    """Helper to extract (name, slug) tuples from themes."""
    if hasattr(pkg, 'themes'):
        themes = pkg.themes
    elif isinstance(pkg, dict) and 'themes' in pkg:
        themes = pkg['themes']
    else:
        return []

    result = []
    for t in themes:
        if hasattr(t, 'name') and hasattr(t, 'slug'):
            result.append((t.name, t.slug))
        elif isinstance(t, dict):
            result.append((t.get('name', ''), t.get('slug', '')))
    return result


def _get_pkg_travel_types(pkg: Any) -> List[str]:
    """Helper to extract travel types."""
    if hasattr(pkg, 'travel_types'):
        tts = pkg.travel_types
    elif isinstance(pkg, dict) and 'travel_types' in pkg:
        tts = pkg['travel_types']
    else:
        return []

    result = []
    for tt in tts:
        if hasattr(tt, 'travel_type'):
            result.append(str(tt.travel_type))
        elif isinstance(tt, dict) and 'travel_type' in tt:
            result.append(str(tt['travel_type']))
        else:
            result.append(str(tt))
    return result


def _get_pkg_months(pkg: Any) -> List[int]:
    """Helper to extract availability months."""
    if hasattr(pkg, 'availability_months'):
        months = pkg.availability_months
    elif isinstance(pkg, dict) and 'available_months' in pkg:
        months = pkg['available_months']
    elif isinstance(pkg, dict) and 'availability_months' in pkg:
        months = pkg['availability_months']
    else:
        return []

    result = []
    for m in months:
        if hasattr(m, 'month'):
            result.append(int(m.month))
        elif isinstance(m, dict) and 'month' in m:
            result.append(int(m['month']))
        else:
            try:
                result.append(int(m))
            except (ValueError, TypeError):
                pass
    return sorted(result)


def score_and_explain_package(
    pkg: Any,
    starting_city: str,
    budget: Union[Decimal, float, int],
    travellers: int,
    duration_days: int,
    interest: str,
    travel_type: str,
    month: int,
    destination_id: Optional[int] = None
) -> Optional[Dict[str, Any]]:
    """
    Score a package using the 100-point recommendation model and generate factual explanations.

    Returns None if any hard constraint fails or budget > 20% fallback.
    Returns dict with:
        match_score: int (0-100)
        match_reasons: List[str]
        mismatches: List[str]
        budget_status: str ('within_budget' | 'over_budget')
        budget_difference: float
        estimated_total_cost: float
    """
    # 1. HARD FILTER: Active status
    is_active = getattr(pkg, 'is_active', True)
    if isinstance(pkg, dict):
        is_active = pkg.get('is_active', True)
    if not is_active:
        return None

    # 2. HARD FILTER: Starting City (case-insensitive)
    pkg_city = getattr(pkg, 'starting_city', None)
    if isinstance(pkg, dict):
        pkg_city = pkg.get('starting_city')
    if not pkg_city or pkg_city.strip().lower() != starting_city.strip().lower():
        return None

    # 3. HARD FILTER: Interest (case-insensitive on name or slug)
    interest_clean = interest.strip().lower()
    pkg_themes = _get_pkg_themes(pkg)
    has_theme_match = any(
        t_name.lower() == interest_clean or t_slug.lower() == interest_clean
        for t_name, t_slug in pkg_themes
    )
    if not has_theme_match:
        return None

    # 4. HARD FILTER: Explicit Destination (if provided)
    if destination_id is not None:
        pkg_dest_id = getattr(pkg, 'destination_id', None)
        if pkg_dest_id is None and hasattr(pkg, 'destination') and pkg.destination:
            pkg_dest_id = getattr(pkg.destination, 'id', None)
        elif isinstance(pkg, dict):
            pkg_dest_id = pkg.get('destination_id')
            if pkg_dest_id is None and isinstance(pkg.get('destination'), dict):
                pkg_dest_id = pkg['destination'].get('id')
        if pkg_dest_id != destination_id:
            return None

    # Cost calculation
    price_per_person = getattr(pkg, 'price_per_person', None)
    if isinstance(pkg, dict):
        price_per_person = pkg.get('price_per_person')
    price_per_person = float(price_per_person)
    estimated_total_cost = round(price_per_person * travellers, 2)
    budget_float = float(budget)

    # 5. HARD FILTER: Budget fallback boundary (>20% over budget is excluded)
    if estimated_total_cost > round(budget_float * 1.20, 2):
        return None

    # -------------------------------------------------------------
    # SOFT SCORING (Max = 100 points)
    # -------------------------------------------------------------
    score = 0
    match_reasons: List[str] = []
    mismatches: List[str] = []

    # F. Starting City: +5 pts (hard matched above)
    score += 5
    match_reasons.append(f"Departs from your starting city ({starting_city.strip()})")

    # B. Interest: +25 pts (hard matched above)
    score += 25
    # Find matching display name
    matched_theme_name = next(
        (t_name for t_name, t_slug in pkg_themes if t_name.lower() == interest_clean or t_slug.lower() == interest_clean),
        interest.strip()
    )
    match_reasons.append(f"Matches your {matched_theme_name} interest")

    # A. Budget Fit: max 25 pts
    if estimated_total_cost <= budget_float:
        score += 25
        budget_status = 'within_budget'
        budget_difference = 0.0
        match_reasons.append(f"Fits your ₹{int(budget_float):,} total budget")
    else:
        budget_status = 'over_budget'
        budget_difference = round(estimated_total_cost - budget_float, 2)
        over_pct = ((estimated_total_cost - budget_float) / budget_float) * 100.0
        if over_pct <= 10.0:
            score += 18
        else:
            score += 10
        mismatches.append(f"₹{int(budget_difference):,} above your selected budget")

    # C. Duration: max 20 pts
    pkg_duration = getattr(pkg, 'duration_days', None)
    if isinstance(pkg, dict):
        pkg_duration = pkg.get('duration_days')
    pkg_duration = int(pkg_duration) if pkg_duration is not None else duration_days

    diff = abs(pkg_duration - duration_days)
    if diff == 0:
        score += 20
        match_reasons.append(f"Matches your {duration_days}-day duration preference")
    elif diff == 1:
        score += 16
        if pkg_duration > duration_days:
            match_reasons.append("Only 1 day longer than your preferred duration")
        else:
            match_reasons.append("Only 1 day shorter than your preferred duration")
        mismatches.append(f"Package is {pkg_duration} days instead of your preferred {duration_days} days")
    elif diff == 2:
        score += 12
        mismatches.append(f"Package is {pkg_duration} days instead of your preferred {duration_days} days")
    elif diff == 3:
        score += 8
        mismatches.append(f"Package is {pkg_duration} days instead of your preferred {duration_days} days")
    else:
        score += 4
        mismatches.append(f"Package is {pkg_duration} days instead of your preferred {duration_days} days")

    # D. Travel Type: max 15 pts
    pkg_travel_types = _get_pkg_travel_types(pkg)
    norm_travel_type = travel_type.strip().capitalize()
    if norm_travel_type in pkg_travel_types:
        score += 15
        match_reasons.append(f"Suitable for {norm_travel_type} travel")
    else:
        score += 0
        avail_types_str = ", ".join(pkg_travel_types) if pkg_travel_types else "other"
        mismatches.append(f"Designed for {avail_types_str} travel")

    # E. Month: max 10 pts
    pkg_months = _get_pkg_months(pkg)
    month_name = MONTH_NAMES.get(month, f"Month {month}")
    if month in pkg_months:
        score += 10
        match_reasons.append(f"Available in {month_name}")
    else:
        score += 0
        mismatches.append(f"Not listed for {month_name}")

    # Sanitize explanations against unsupported claims
    for r in match_reasons + mismatches:
        for claim in PROHIBITED_UNSUPPORTED_CLAIMS:
            if claim in r.lower():
                raise ValueError(f"Prohibited unsupported claim detected in explanation: {claim}")

    return {
        'match_score': score,
        'match_reasons': match_reasons,
        'mismatches': mismatches,
        'budget_status': budget_status,
        'budget_difference': budget_difference,
        'estimated_total_cost': estimated_total_cost
    }


def get_package_recommendations(
    starting_city: str,
    budget: Union[Decimal, float, int],
    travellers: int,
    duration_days: int,
    interest: str,
    travel_type: str,
    month: int,
    destination_id: Optional[int] = None,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Query candidate packages with hard database filters, score and explain them,
    and return the top ranked packages.
    """
    interest_clean = interest.strip().lower()
    budget_dec = Decimal(str(budget))

    # Base query: Active packages + starting city + interest theme (hard filters)
    query = (
        Package.query
        .filter(
            Package.is_active.is_(True),
            func.lower(Package.starting_city) == starting_city.strip().lower(),
            Package.themes.any(
                or_(
                    func.lower(Theme.name) == interest_clean,
                    func.lower(Theme.slug) == interest_clean
                )
            )
        )
    )

    if destination_id is not None:
        query = query.filter(Package.destination_id == destination_id)

    # Budget fallback logic:
    # 1. Check if any package is within budget
    within_budget_cond = (Package.price_per_person <= (budget_dec / Decimal(travellers)))
    has_within = query.filter(within_budget_cond).first() is not None
    if has_within:
        query = query.filter(within_budget_cond)
    else:
        # 2. Allow up to 20% over budget
        max_fallback_price = (budget_dec * Decimal('1.20')) / Decimal(travellers)
        query = query.filter(Package.price_per_person <= max_fallback_price)

    # Eager load relationships to prevent N+1 queries
    candidates = (
        query.distinct()
        .options(
            selectinload(Package.operator),
            selectinload(Package.destination),
            selectinload(Package.themes),
            selectinload(Package.travel_types),
            selectinload(Package.availability_months)
        )
        .all()
    )

    recommended_items = []
    for pkg in candidates:
        evaluation = score_and_explain_package(
            pkg=pkg,
            starting_city=starting_city,
            budget=budget,
            travellers=travellers,
            duration_days=duration_days,
            interest=interest,
            travel_type=travel_type,
            month=month,
            destination_id=destination_id
        )
        if evaluation is not None:
            summary = pkg.to_summary_dict(
                requested_travellers=travellers,
                match_score=evaluation['match_score'],
                budget_status=evaluation['budget_status'],
                budget_difference=evaluation['budget_difference'],
                match_reasons=evaluation['match_reasons'],
                mismatches=evaluation['mismatches']
            )
            recommended_items.append({
                'data': summary,
                'match_score': evaluation['match_score'],
                'budget_status': evaluation['budget_status'],
                'estimated_total_cost': evaluation['estimated_total_cost'],
                'name': pkg.name
            })

    # Sort deterministically:
    # 1. match_score DESC
    # 2. budget_status: within_budget before over_budget
    # 3. estimated_total_cost ASC
    # 4. package name ASC
    recommended_items.sort(
        key=lambda x: (
            -x['match_score'],
            0 if x['budget_status'] == 'within_budget' else 1,
            x['estimated_total_cost'],
            x['name'].lower()
        )
    )

    return [item['data'] for item in recommended_items[:limit]]


def generate_destination_reasons(
    destination_name: str,
    matching_packages: List[Any],
    budget: Union[Decimal, float, int],
    travellers: int,
    duration_days: int,
    interest: str,
    travel_type: str,
    month: int
) -> Tuple[List[str], List[str]]:
    """
    Generate factual explainability reasons and mismatches for a discovered destination
    based entirely on its qualifying matching packages.
    """
    match_reasons: List[str] = []
    mismatches: List[str] = []

    pkg_count = len(matching_packages)
    if pkg_count == 0:
        return [], ["No matching packages available"]

    # 1. Package count & theme (e.g. "1 Adventure package available" / "2 Adventure packages available")
    if pkg_count == 1:
        match_reasons.append(f"1 {interest.strip()} package available")
    else:
        match_reasons.append(f"{pkg_count} {interest.strip()} packages available")

    # 2. Budget distribution (e.g. "1 package is within your budget" / "2 packages are within your budget")
    budget_float = float(budget)
    within_budget_count = 0
    for pkg in matching_packages:
        price = getattr(pkg, 'price_per_person', None)
        if price is None and isinstance(pkg, dict):
            price = pkg.get('price_per_person', 0)
        total_cost = float(price) * travellers
        if total_cost <= budget_float:
            within_budget_count += 1

    if within_budget_count > 0:
        if within_budget_count == 1:
            match_reasons.append("1 package is within your budget")
        else:
            match_reasons.append(f"{within_budget_count} packages are within your budget")
    else:
        if pkg_count == 1:
            mismatches.append("Package is slightly above budget (within 20% fallback)")
        else:
            mismatches.append("Packages are slightly above budget (within 20% fallback)")

    # 3. Duration alignment (e.g. "1 package is close to your 5-day preference" / "Several packages are close to your 5-day preference")
    exact_duration_count = sum(
        1 for p in matching_packages
        if (getattr(p, 'duration_days', None) if not isinstance(p, dict) else p.get('duration_days')) == duration_days
    )
    diff_1_count = sum(
        1 for p in matching_packages
        if abs(((getattr(p, 'duration_days', None) if not isinstance(p, dict) else p.get('duration_days')) or 0) - duration_days) == 1
    )

    if exact_duration_count > 0:
        if exact_duration_count == 1:
            match_reasons.append(f"1 package matches your {duration_days}-day duration preference")
        else:
            match_reasons.append(f"{exact_duration_count} packages match your {duration_days}-day duration preference")
    elif diff_1_count > 0:
        if diff_1_count == 1:
            match_reasons.append(f"1 package is close to your {duration_days}-day preference")
        else:
            match_reasons.append(f"Several packages are close to your {duration_days}-day preference")
    else:
        if pkg_count == 1:
            mismatches.append(f"Package duration varies from your preferred {duration_days} days")
        else:
            mismatches.append(f"Package durations vary from your preferred {duration_days} days")

    # 4. Travel type availability (e.g. "Available package includes Couple travel" / "Available packages include Couple travel")
    norm_travel_type = travel_type.strip().capitalize()
    travel_type_match_count = 0
    all_avail_types = set()
    for p in matching_packages:
        tts = _get_pkg_travel_types(p)
        all_avail_types.update(tts)
        if norm_travel_type in tts:
            travel_type_match_count += 1

    if travel_type_match_count > 0:
        if travel_type_match_count == 1 and pkg_count == 1:
            match_reasons.append(f"Available package includes {norm_travel_type} travel")
        else:
            match_reasons.append(f"Available packages include {norm_travel_type} travel")
    else:
        types_str = ", ".join(sorted(all_avail_types)) if all_avail_types else "other"
        if pkg_count == 1:
            mismatches.append(f"Designed for {types_str} travel")
        else:
            mismatches.append(f"Available packages cater to {types_str} travel rather than {norm_travel_type}")

    # 5. Month availability & mismatch wording
    month_name = MONTH_NAMES.get(month, f"Month {month}")
    month_match_count = 0
    for p in matching_packages:
        months = _get_pkg_months(p)
        if month in months:
            month_match_count += 1

    if month_match_count > 0:
        match_reasons.append(f"Available in {month_name}")
    else:
        mismatches.append(f"No matching package is listed for {month_name}")

    # Sanitize against unsupported claims
    for r in match_reasons + mismatches:
        for claim in PROHIBITED_UNSUPPORTED_CLAIMS:
            if claim in r.lower():
                raise ValueError(f"Prohibited claim in destination reason: {claim}")

    return match_reasons, mismatches
