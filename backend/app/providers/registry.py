"""
Travel Provider Registry.
Step 9 - Provider-Ready Architecture.

Maintains registered travel inventory providers and prevents provider-specific branching in service code.
"""

from typing import Dict, List, Optional, Any
from app.providers.base import BaseTravelProvider


class TravelProviderRegistry:
    """
    Registry for managing available travel providers.
    Enforces the Open/Closed Principle: new providers can be added without modifying core search logic.
    """

    def __init__(self):
        self._providers: Dict[str, BaseTravelProvider] = {}

    def register(self, provider: BaseTravelProvider) -> None:
        """Register a provider instance."""
        if not isinstance(provider, BaseTravelProvider):
            raise TypeError(f"Expected BaseTravelProvider instance, got {type(provider)}")
        self._providers[provider.provider_name.lower()] = provider

    def get(self, provider_name: str) -> Optional[BaseTravelProvider]:
        """Retrieve a registered provider by name (case-insensitive)."""
        if not provider_name:
            return None
        return self._providers.get(provider_name.lower())

    def enabled_providers(self) -> List[BaseTravelProvider]:
        """Return a list of all currently enabled providers."""
        return [p for p in self._providers.values() if p.is_enabled]

    def all_providers(self) -> List[BaseTravelProvider]:
        """Return all registered providers regardless of enabled state."""
        return list(self._providers.values())

    def get_health_status(self) -> List[Dict[str, Any]]:
        """
        Execute health checks across all registered providers and return aggregated status.
        Disabled providers return status: 'disabled' without making external network calls.
        """
        results = []
        for provider in self._providers.values():
            try:
                status = provider.health_check()
                results.append(status)
            except Exception as e:
                results.append({
                    "provider": provider.provider_name,
                    "source_type": provider.source_type,
                    "enabled": provider.is_enabled,
                    "status": "unhealthy",
                    "error": str(e)
                })
        return results

    def clear(self) -> None:
        """Clear all registered providers (primarily for test isolation)."""
        self._providers.clear()
