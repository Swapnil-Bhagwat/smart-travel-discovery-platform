"""
Normalized Package Schema / DTO for the Smart Travel Platform.
Step 9 - Provider-Ready Architecture.

Provides a unified, provider-independent representation of travel packages.
"""

from dataclasses import dataclass, field, asdict
from decimal import Decimal
from typing import Any, Dict, List, Optional


@dataclass
class NormalizedPackage:
    """
    Unified package representation across all inventory sources (Demo and future Live providers).
    """
    provider: str                      # e.g., "demo", "viator", "booking"
    source_type: str                   # e.g., "demo", "live"
    external_id: str                   # Unique package ID in provider system, e.g., "1"
    name: str                          # Title of the travel package
    destination: Dict[str, Any]        # {"id": ..., "name": "...", "region": "...", "country": "..."}
    starting_city: str                 # Departure city
    duration_days: int                 # Duration in days
    duration_nights: int               # Duration in nights
    price_per_person: float            # Per-person price
    currency: str = "INR"              # Default currency
    themes: List[Dict[str, Any]] = field(default_factory=list)      # [{"id": ..., "name": ..., "slug": ...}]
    travel_types: List[str] = field(default_factory=list)          # ["Solo", "Couple", "Family", "Group"]
    available_months: List[int] = field(default_factory=list)      # [1, 2, ..., 12]
    featured_image_url: Optional[str] = None
    source_url: Optional[str] = None
    description: Optional[str] = None
    operator: Optional[Dict[str, Any]] = None                      # {"id": ..., "name": ..., "rating": ...}
    is_active: bool = True

    # Detailed itinerary & inclusions
    hotel_info: Optional[str] = None
    meals_info: Optional[str] = None
    transportation_info: Optional[str] = None
    sightseeing_info: Optional[str] = None
    activities_info: Optional[str] = None
    itinerary: List[Dict[str, Any]] = field(default_factory=list)
    inclusions: List[str] = field(default_factory=list)
    exclusions: List[str] = field(default_factory=list)

    # Search & match scoring metadata (optional)
    match_score: Optional[int] = None
    budget_status: Optional[str] = "within_budget"
    budget_difference: Optional[float] = 0.0
    estimated_total_cost: Optional[float] = None
    match_reasons: Optional[List[str]] = None
    mismatches: Optional[List[str]] = None

    @property
    def identity(self) -> str:
        """Unique compound identity key for provider deduplication."""
        return f"{self.provider}:{self.external_id}"

    def to_dict(self) -> Dict[str, Any]:
        """Convert normalized package to serializable dictionary format."""
        data = asdict(self)
        
        # Provide both numeric id (for legacy/frontend backwards compatibility) and external_id
        if self.external_id.isdigit():
            data["id"] = int(self.external_id)
        else:
            data["id"] = self.external_id
            
        # Support image_url alias for frontend compatibility
        data["image_url"] = self.featured_image_url
        
        # Calculate estimated total cost if not explicitly provided
        if self.estimated_total_cost is None:
            data["estimated_total_cost"] = self.price_per_person
            
        return data

    @classmethod
    def from_db_model(
        cls,
        pkg: Any,
        requested_travellers: int = 1,
        match_score: Optional[int] = None,
        budget_status: str = 'within_budget',
        budget_difference: float = 0.0,
        match_reasons: Optional[List[str]] = None,
        mismatches: Optional[List[str]] = None,
        include_details: bool = False
    ) -> 'NormalizedPackage':
        """
        Factory to construct NormalizedPackage from SQLAlchemy Package model.
        """
        pkg_price = float(pkg.price_per_person)
        total_cost = round(pkg_price * requested_travellers, 2)

        themes_data = [
            {'id': t.id, 'name': t.name, 'slug': t.slug}
            for t in pkg.themes
        ] if hasattr(pkg, 'themes') and pkg.themes else []

        travel_types_data = [
            tt.travel_type for tt in pkg.travel_types
        ] if hasattr(pkg, 'travel_types') and pkg.travel_types else []

        months_data = sorted([
            m.month for m in pkg.availability_months
        ]) if hasattr(pkg, 'availability_months') and pkg.availability_months else []

        dest_data = {
            'id': pkg.destination.id,
            'name': pkg.destination.name,
            'country': pkg.destination.country,
            'region': pkg.destination.region,
        } if getattr(pkg, 'destination', None) else {'id': 0, 'name': 'Unknown', 'country': 'India', 'region': ''}

        op_data = {
            'id': pkg.operator.id,
            'name': pkg.operator.name,
            'rating': float(pkg.operator.rating) if pkg.operator and pkg.operator.rating is not None else 0.0,
        } if getattr(pkg, 'operator', None) else None

        itinerary_data = []
        inclusions_data = []
        exclusions_data = []

        if include_details:
            if hasattr(pkg, 'itineraries') and pkg.itineraries:
                itinerary_data = [
                    {
                        'id': it.id,
                        'day_number': it.day_number,
                        'title': it.title,
                        'description': it.description,
                        'accommodation': it.accommodation,
                        'meals_provided': it.meals_provided,
                    }
                    for it in sorted(pkg.itineraries, key=lambda x: x.day_number)
                ]
            if hasattr(pkg, 'inclusions') and pkg.inclusions:
                inclusions_data = [inc.description for inc in pkg.inclusions]
            if hasattr(pkg, 'exclusions') and pkg.exclusions:
                exclusions_data = [exc.description for exc in pkg.exclusions]

        return cls(
            provider="demo",
            source_type="demo",
            external_id=str(pkg.id),
            name=pkg.name,
            destination=dest_data,
            starting_city=pkg.starting_city,
            duration_days=pkg.duration_days,
            duration_nights=pkg.duration_nights,
            price_per_person=pkg_price,
            currency="INR",
            themes=themes_data,
            travel_types=travel_types_data,
            available_months=months_data,
            featured_image_url=pkg.featured_image_url,
            source_url=pkg.source_url,
            description=getattr(pkg, 'description', None),
            operator=op_data,
            is_active=pkg.is_active,
            hotel_info=getattr(pkg, 'hotel_info', None),
            meals_info=getattr(pkg, 'meals_info', None),
            transportation_info=getattr(pkg, 'transportation_info', None),
            sightseeing_info=getattr(pkg, 'sightseeing_info', None),
            activities_info=getattr(pkg, 'activities_info', None),
            itinerary=itinerary_data,
            inclusions=inclusions_data,
            exclusions=exclusions_data,
            match_score=match_score,
            budget_status=budget_status,
            budget_difference=float(budget_difference),
            estimated_total_cost=total_cost,
            match_reasons=match_reasons,
            mismatches=mismatches
        )
