"""
Unified Provider Search Service.
Step 9 - Provider-Ready Architecture.

Provides a unified coordinator for package search across all enabled providers,
handling provider selection, deduplication, and result aggregation.
"""

from typing import Any, Dict, List, Optional
from app.providers import provider_registry, TravelProviderRegistry
from app.schemas.package_dto import NormalizedPackage


class ProviderSearchService:
    """
    Coordinates multi-provider search, deduplication, and aggregation.
    """

    def __init__(self, registry: Optional[TravelProviderRegistry] = None):
        self.registry = registry or provider_registry

    def search(
        self,
        criteria: Dict[str, Any],
        provider_name: Optional[str] = None
    ) -> List[NormalizedPackage]:
        """
        Execute unified package search across target providers.
        
        Args:
            criteria: Search filters (starting_city, budget, travellers, duration_days, interest, travel_type, month, destination_id)
            provider_name: Specific provider to query ('demo', 'viator', etc.), or None to query all enabled providers.

        Returns:
            Deduplicated, ranked list of NormalizedPackage instances.
        """
        # Determine target providers
        if provider_name and provider_name.strip():
            p = self.registry.get(provider_name.strip().lower())
            if not p or not p.is_enabled:
                return []
            target_providers = [p]
        else:
            target_providers = self.registry.enabled_providers()

        aggregated_results: List[NormalizedPackage] = []
        seen_identities = set()

        for provider in target_providers:
            try:
                packages = provider.search_packages(criteria)
                for pkg in packages:
                    # Deduplication rule: provider + external_id
                    identity = pkg.identity
                    if identity not in seen_identities:
                        seen_identities.add(identity)
                        aggregated_results.append(pkg)
            except Exception as e:
                # Log or handle provider-specific errors gracefully without failing entire search
                continue

        # Sort aggregated results consistently:
        # 1. match_score DESC (if present)
        # 2. budget_status: within_budget before over_budget
        # 3. estimated_total_cost ASC
        # 4. package name ASC
        aggregated_results.sort(
            key=lambda x: (
                -(x.match_score if x.match_score is not None else 0),
                0 if x.budget_status == "within_budget" else 1,
                x.estimated_total_cost or 0.0,
                x.name.lower()
            )
        )

        limit = criteria.get("limit")
        if limit and isinstance(limit, int) and limit > 0:
            return aggregated_results[:limit]

        return aggregated_results

    def get_details(
        self,
        external_id: str,
        provider_name: str = "demo",
        context: Optional[Dict[str, Any]] = None
    ) -> Optional[NormalizedPackage]:
        """
        Fetch complete details for a package from a specified provider.
        """
        provider = self.registry.get(provider_name.lower())
        if not provider or not provider.is_enabled:
            return None
        return provider.get_package_details(external_id=external_id, context=context)


# Global service instance
provider_search_service = ProviderSearchService()
