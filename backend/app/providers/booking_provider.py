"""
Booking.com Live Travel Provider Stub.
Step 9 - Provider-Ready Architecture.

Represents a future live external provider. Kept strictly disabled until authorized credentials are provided.
"""

from typing import Any, Dict, List, Optional
from flask import current_app
from app.providers.base import BaseTravelProvider
from app.schemas.package_dto import NormalizedPackage


class BookingTravelProvider(BaseTravelProvider):
    """
    Adapter for Booking.com Package & Hotel API (future integration).
    Strictly disabled by default; does not execute network calls when disabled.
    """

    @property
    def provider_name(self) -> str:
        return "booking"

    @property
    def source_type(self) -> str:
        return "live"

    @property
    def is_enabled(self) -> bool:
        if current_app:
            return current_app.config.get("BOOKING_ENABLED", False)
        return False

    def search_packages(self, criteria: Dict[str, Any]) -> List[NormalizedPackage]:
        if not self.is_enabled:
            return []
        # Future live API invocation will go here once authorized credentials are provided
        return []

    def get_package_details(self, external_id: str, context: Optional[Dict[str, Any]] = None) -> Optional[NormalizedPackage]:
        if not self.is_enabled:
            return None
        return None

    def health_check(self) -> Dict[str, Any]:
        if not self.is_enabled:
            return {
                "provider": self.provider_name,
                "source_type": self.source_type,
                "enabled": False,
                "status": "disabled",
                "message": "Booking.com live provider is disabled in configuration"
            }
        
        api_key = current_app.config.get("BOOKING_API_KEY", "") if current_app else ""
        if not api_key:
            return {
                "provider": self.provider_name,
                "source_type": self.source_type,
                "enabled": True,
                "status": "unhealthy",
                "message": "Booking.com API key is not configured"
            }

        return {
            "provider": self.provider_name,
            "source_type": self.source_type,
            "enabled": True,
            "status": "healthy"
        }
