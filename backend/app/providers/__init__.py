"""
Providers Package for Smart Travel Platform.
Step 9 - Provider-Ready Architecture.
"""

from app.providers.base import BaseTravelProvider
from app.providers.demo_provider import DemoTravelProvider
from app.providers.viator_provider import ViatorTravelProvider
from app.providers.booking_provider import BookingTravelProvider
from app.providers.registry import TravelProviderRegistry

# Default global provider registry
provider_registry = TravelProviderRegistry()

# Register core demo provider and future provider stubs
provider_registry.register(DemoTravelProvider())
provider_registry.register(ViatorTravelProvider())
provider_registry.register(BookingTravelProvider())

__all__ = [
    "BaseTravelProvider",
    "DemoTravelProvider",
    "ViatorTravelProvider",
    "BookingTravelProvider",
    "TravelProviderRegistry",
    "provider_registry"
]
