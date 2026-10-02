"""
Base Travel Provider Abstract Interface.
Step 9 - Provider-Ready Architecture.

Defines the contract that all travel package inventory providers (Demo and future Live) must implement.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from app.schemas.package_dto import NormalizedPackage


class BaseTravelProvider(ABC):
    """
    Abstract interface for travel providers.
    All providers must expose a consistent set of capabilities regardless of their underlying data source.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Unique machine identifier for the provider (e.g. 'demo', 'viator', 'booking')."""
        pass

    @property
    @abstractmethod
    def source_type(self) -> str:
        """Origin classification: 'demo' for internal demonstration data, 'live' for external real-world inventory."""
        pass

    @property
    @abstractmethod
    def is_enabled(self) -> bool:
        """Whether this provider is currently enabled in application configuration."""
        pass

    @abstractmethod
    def search_packages(self, criteria: Dict[str, Any]) -> List[NormalizedPackage]:
        """
        Search for travel packages according to unified criteria.
        
        Expected criteria keys:
        - starting_city (str)
        - budget (Decimal or float, optional)
        - travellers (int, optional)
        - duration_days (int, optional)
        - interest (str, optional)
        - travel_type (str, optional)
        - month (int, optional)
        - destination_id (int, optional)
        - limit (int, optional)
        """
        pass

    @abstractmethod
    def get_package_details(self, external_id: str, context: Optional[Dict[str, Any]] = None) -> Optional[NormalizedPackage]:
        """
        Retrieve full details (including itinerary, inclusions, and operator metadata)
        for a specific package by its external identifier.
        """
        pass

    @abstractmethod
    def health_check(self) -> Dict[str, Any]:
        """
        Verify the availability, operational health, and connectivity of this provider.
        Returns a dict containing:
        - provider (str)
        - source_type (str)
        - enabled (bool)
        - status (str: 'healthy', 'degraded', 'disabled', 'unhealthy')
        - message (str, optional)
        """
        pass
