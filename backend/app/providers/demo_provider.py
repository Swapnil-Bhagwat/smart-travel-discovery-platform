"""
Demo Travel Provider Implementation.
Step 9 - Provider-Ready Architecture.

Exposes the existing MySQL smart_travel_db demonstration inventory through the unified provider interface.
"""

from decimal import Decimal
from typing import Any, Dict, List, Optional
from flask import current_app
from sqlalchemy import func, or_
from sqlalchemy.orm import selectinload

from app.extensions import db
from app.models.package import Package, PackageTravelType, PackageAvailabilityMonth
from app.models.theme import Theme
from app.providers.base import BaseTravelProvider
from app.schemas.package_dto import NormalizedPackage

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}


class DemoTravelProvider(BaseTravelProvider):
    """
    Travel provider backed by the local demonstration MySQL database.
    """

    @property
    def provider_name(self) -> str:
        return "demo"

    @property
    def source_type(self) -> str:
        return "demo"

    @property
    def is_enabled(self) -> bool:
        if current_app:
            return current_app.config.get("DEMO_PROVIDER_ENABLED", True)
        return True

    def search_packages(self, criteria: Dict[str, Any]) -> List[NormalizedPackage]:
        """
        Search active demo packages in MySQL using the established platform filtering and scoring rules.
        """
        if not self.is_enabled:
            return []

        starting_city = criteria.get("starting_city")
        budget = criteria.get("budget")
        travellers = criteria.get("travellers", 1) or 1
        duration_days = criteria.get("duration_days")
        interest = criteria.get("interest")
        travel_type = criteria.get("travel_type")
        month = criteria.get("month")
        destination_id = criteria.get("destination_id")
        limit = criteria.get("limit")

        # Base query: Always strictly active packages
        query = Package.query.filter(Package.is_active.is_(True))

        # Hard Constraint: Destination ID
        if destination_id is not None:
            query = query.filter(Package.destination_id == int(destination_id))

        # Hard Constraint: Starting City (case-insensitive)
        if starting_city and str(starting_city).strip():
            query = query.filter(func.lower(Package.starting_city) == str(starting_city).strip().lower())

        # Hard Constraint: Interest (theme match on name or slug)
        interest_clean = str(interest).strip().lower() if interest and str(interest).strip() else None
        if interest_clean is not None:
            query = query.filter(
                Package.themes.any(
                    or_(
                        func.lower(Theme.name) == interest_clean,
                        func.lower(Theme.slug) == interest_clean
                    )
                )
            )

        # Budget Constraint & 20% near-budget fallback
        if budget is not None:
            budget_dec = Decimal(str(budget))
            within_budget_cond = (Package.price_per_person <= (budget_dec / Decimal(travellers)))
            has_within = query.filter(within_budget_cond).first() is not None
            if has_within:
                query = query.filter(within_budget_cond)
            else:
                max_fallback_price = (budget_dec * Decimal('1.20')) / Decimal(travellers)
                query = query.filter(Package.price_per_person <= max_fallback_price)

        # Eagerly load relationships to avoid N+1 queries
        query = query.distinct().options(
            selectinload(Package.operator),
            selectinload(Package.destination),
            selectinload(Package.themes),
            selectinload(Package.travel_types),
            selectinload(Package.availability_months)
        )

        candidates = query.all()

        # Score candidates deterministically
        normalized_results: List[NormalizedPackage] = []
        for pkg in candidates:
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
            has_type_match = False
            if travel_type is not None:
                has_type_match = any(
                    tt.travel_type.lower() == str(travel_type).strip().lower()
                    for tt in pkg.travel_types
                )
                if has_type_match:
                    score += 20
            else:
                score += 20

            # 4. Month (max 15)
            has_month_match = False
            if month is not None:
                has_month_match = any(
                    m.month == int(month)
                    for m in pkg.availability_months
                )
                if has_month_match:
                    score += 15
            else:
                score += 15

            # 5. Budget fit (max 15)
            if budget is not None:
                b_val = float(budget)
                if pkg_cost <= b_val:
                    score += 15
                    b_status = "within_budget"
                    b_diff = 0.0
                else:
                    b_status = "over_budget"
                    b_diff = round(pkg_cost - b_val, 2)
                    over_pct = ((pkg_cost - b_val) / b_val) * 100.0
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

            # Generate match reasons and mismatches
            match_reasons: List[str] = []
            mismatches: List[str] = []

            if starting_city:
                match_reasons.append(f"Departs from your starting city ({str(starting_city).strip()})")

            if interest_clean is not None:
                matched_theme = next(
                    (t.name for t in pkg.themes if t.name.lower() == interest_clean or t.slug.lower() == interest_clean),
                    str(interest).strip()
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
                m_int = int(month)
                month_name = MONTH_NAMES.get(m_int, f"Month {m_int}")
                if has_month_match:
                    match_reasons.append(f"Available in {month_name}")
                else:
                    mismatches.append(f"Not listed for {month_name}")

            norm_pkg = NormalizedPackage.from_db_model(
                pkg=pkg,
                requested_travellers=travellers,
                match_score=score,
                budget_status=b_status,
                budget_difference=b_diff,
                match_reasons=match_reasons if (match_reasons or mismatches) else None,
                mismatches=mismatches if (match_reasons or mismatches) else None,
                include_details=False
            )
            normalized_results.append(norm_pkg)

        # Sort deterministically
        normalized_results.sort(
            key=lambda p: (
                -(p.match_score or 0),
                0 if p.budget_status == "within_budget" else 1,
                p.estimated_total_cost or 0.0,
                p.name.lower()
            )
        )

        if limit and limit > 0:
            return normalized_results[:limit]
        return normalized_results

    def get_package_details(self, external_id: str, context: Optional[Dict[str, Any]] = None) -> Optional[NormalizedPackage]:
        """Fetch complete package with itineraries, inclusions, and exclusions."""
        if not self.is_enabled:
            return None

        try:
            pkg_id = int(external_id)
        except (ValueError, TypeError):
            return None

        pkg = (
            Package.query.filter_by(id=pkg_id, is_active=True)
            .options(
                selectinload(Package.operator),
                selectinload(Package.destination),
                selectinload(Package.themes),
                selectinload(Package.travel_types),
                selectinload(Package.availability_months),
                selectinload(Package.itineraries),
                selectinload(Package.inclusions),
                selectinload(Package.exclusions),
            )
            .first()
        )

        if not pkg:
            return None

        travellers = 1
        if context and "travellers" in context:
            try:
                travellers = max(1, int(context["travellers"]))
            except (ValueError, TypeError):
                travellers = 1

        return NormalizedPackage.from_db_model(pkg, requested_travellers=travellers, include_details=True)

    def health_check(self) -> Dict[str, Any]:
        """Perform database liveness check for demo inventory."""
        if not self.is_enabled:
            return {
                "provider": self.provider_name,
                "source_type": self.source_type,
                "enabled": False,
                "status": "disabled",
                "message": "Demo provider is disabled in configuration"
            }

        try:
            count = Package.query.filter(Package.is_active.is_(True)).count()
            return {
                "provider": self.provider_name,
                "source_type": self.source_type,
                "enabled": True,
                "status": "healthy",
                "message": f"Demo database active ({count} active packages)"
            }
        except Exception as e:
            return {
                "provider": self.provider_name,
                "source_type": self.source_type,
                "enabled": True,
                "status": "unhealthy",
                "error": str(e)
            }
