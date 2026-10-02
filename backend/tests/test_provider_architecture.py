"""
Unit and Integration Tests for Step 9: Provider Architecture.
Covers:
1. Demo provider registration
2. Demo provider lookup
3. Provider registry behavior
4. Normalized package conversion
5. Provider search service
6. Provider deduplication
7. Disabled provider behavior
8. Missing provider credentials behavior
9. Provider health endpoint
10. Demo provider search results
11. Existing package search remains correct
12. Existing discovery remains correct
13. Existing recommendations remain correct
14. Existing comparison remains correct
15. Beach remains a hard interest filter
16. Starting city remains a hard filter
17. Explicit destination remains a hard filter
18. No inactive demo packages returned
19. API error format remains consistent
20. No secrets are exposed
"""

import unittest
from decimal import Decimal
from app import create_app
from app.config import Config
from app.extensions import db
from app.models.destination import Destination
from app.models.operator import Operator
from app.models.theme import Theme
from app.models.package import Package, PackageTravelType, PackageAvailabilityMonth, PackageItinerary, PackageInclusion, PackageExclusion
from app.providers import (
    BaseTravelProvider,
    DemoTravelProvider,
    ViatorTravelProvider,
    BookingTravelProvider,
    TravelProviderRegistry,
    provider_registry,
)
from app.schemas.package_dto import NormalizedPackage
from app.services.provider_search_service import ProviderSearchService
from app.services.cache_service import InMemoryCache


class TestProviderConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEMO_PROVIDER_ENABLED = True
    VIATOR_ENABLED = False
    VIATOR_API_KEY = ''
    BOOKING_ENABLED = False
    BOOKING_API_KEY = ''


class TestProviderArchitecture(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestProviderConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._seed_test_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def _seed_test_data(self):
        """Seed minimal in-memory test data for provider tests."""
        dest_goa = Destination(name="Goa", country="India", region="Goa")
        dest_manali = Destination(name="Manali", country="India", region="Himachal Pradesh")
        op = Operator(name="WanderNest Travels", rating=Decimal("4.8"))
        theme_beach = Theme(name="Beach", slug="beach")
        theme_adventure = Theme(name="Adventure", slug="adventure")
        db.session.add_all([dest_goa, dest_manali, op, theme_beach, theme_adventure])
        db.session.commit()

        with db.session.no_autoflush:
            # Active Beach Package in Goa from Mumbai
            pkg1 = Package(
                operator_id=op.id,
                destination_id=dest_goa.id,
                name="Goa Sun & Sand Explorer",
                starting_city="Mumbai",
                duration_days=4,
                duration_nights=3,
                price_per_person=Decimal("12000.00"),
                is_active=True,
                featured_image_url="https://images.unsplash.com/photo-goa",
                source_url="https://wandernest-demo.example.com/packages/goa-sun-sand"
            )
            pkg1.themes.append(theme_beach)
            pkg1.travel_types.append(PackageTravelType(travel_type="Couple"))
            pkg1.availability_months.append(PackageAvailabilityMonth(month=11))
            pkg1.itineraries.append(PackageItinerary(day_number=1, title="Arrival", description="Welcome", accommodation="Hotel", meals_provided="Dinner"))
            pkg1.inclusions.append(PackageInclusion(description="Breakfast"))
            pkg1.exclusions.append(PackageExclusion(description="Flights"))

            # Active Adventure Package in Manali from Delhi
            pkg2 = Package(
                operator_id=op.id,
                destination_id=dest_manali.id,
                name="Manali Alpine Trek",
                starting_city="Delhi",
                duration_days=5,
                duration_nights=4,
                price_per_person=Decimal("18000.00"),
                is_active=True,
                featured_image_url="https://images.unsplash.com/photo-manali",
                source_url="https://wandernest-demo.example.com/packages/manali-trek"
            )
            pkg2.themes.append(theme_adventure)
            pkg2.travel_types.append(PackageTravelType(travel_type="Solo"))
            pkg2.availability_months.append(PackageAvailabilityMonth(month=12))

            # Inactive Package (Should never appear)
            pkg_inactive = Package(
                operator_id=op.id,
                destination_id=dest_goa.id,
                name="Inactive Goa Tour",
                starting_city="Mumbai",
                duration_days=3,
                duration_nights=2,
                price_per_person=Decimal("8000.00"),
                is_active=False,
                source_url="https://wandernest-demo.example.com/packages/inactive-goa"
            )
            pkg_inactive.themes.append(theme_beach)

            db.session.add_all([pkg1, pkg2, pkg_inactive])
        db.session.commit()

    # 1. Demo provider registration
    def test_demo_provider_registration(self):
        reg = TravelProviderRegistry()
        demo = DemoTravelProvider()
        reg.register(demo)
        self.assertIn("demo", reg._providers)
        self.assertEqual(reg.get("demo"), demo)

    # 2. Demo provider lookup (case-insensitive)
    def test_demo_provider_lookup(self):
        demo = provider_registry.get("DEMO")
        self.assertIsNotNone(demo)
        self.assertEqual(demo.provider_name, "demo")
        self.assertEqual(demo.source_type, "demo")

    # 3. Provider registry behavior (enabled vs all)
    def test_provider_registry_behavior(self):
        reg = TravelProviderRegistry()
        demo = DemoTravelProvider()
        viator = ViatorTravelProvider()
        reg.register(demo)
        reg.register(viator)

        all_provs = reg.all_providers()
        self.assertEqual(len(all_provs), 2)

        enabled = reg.enabled_providers()
        self.assertIn(demo, enabled)
        self.assertNotIn(viator, enabled)

    # 4. Normalized package conversion
    def test_normalized_package_conversion(self):
        pkg = Package.query.filter_by(name="Goa Sun & Sand Explorer").first()
        norm = NormalizedPackage.from_db_model(pkg, requested_travellers=2, include_details=True)
        
        self.assertEqual(norm.provider, "demo")
        self.assertEqual(norm.source_type, "demo")
        self.assertEqual(norm.external_id, str(pkg.id))
        self.assertEqual(norm.name, "Goa Sun & Sand Explorer")
        self.assertEqual(norm.destination["name"], "Goa")
        self.assertEqual(norm.price_per_person, 12000.0)
        self.assertEqual(norm.estimated_total_cost, 24000.0)
        self.assertEqual(len(norm.itinerary), 1)
        self.assertEqual(len(norm.inclusions), 1)
        self.assertEqual(len(norm.exclusions), 1)

        d = norm.to_dict()
        self.assertEqual(d["id"], pkg.id)
        self.assertEqual(d["provider"], "demo")
        self.assertEqual(d["source_type"], "demo")

    # 5. Provider search service
    def test_provider_search_service(self):
        svc = ProviderSearchService(provider_registry)
        results = svc.search({
            "starting_city": "Mumbai",
            "interest": "Beach",
            "travellers": 1
        })
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Goa Sun & Sand Explorer")
        self.assertEqual(results[0].provider, "demo")
        self.assertEqual(results[0].source_type, "demo")

    # 6. Provider deduplication
    def test_provider_deduplication(self):
        # Create a mock provider that yields the same package twice
        class DuplicateMockProvider(BaseTravelProvider):
            @property
            def provider_name(self): return "mock"
            @property
            def source_type(self): return "demo"
            @property
            def is_enabled(self): return True
            def search_packages(self, criteria):
                pkg1 = NormalizedPackage(
                    provider="mock", source_type="demo", external_id="101",
                    name="Dup Pkg", destination={}, starting_city="Mumbai",
                    duration_days=3, duration_nights=2, price_per_person=10000
                )
                pkg2 = NormalizedPackage(
                    provider="mock", source_type="demo", external_id="101", # same identity
                    name="Dup Pkg Again", destination={}, starting_city="Mumbai",
                    duration_days=3, duration_nights=2, price_per_person=10000
                )
                return [pkg1, pkg2]
            def get_package_details(self, external_id, context=None): return None
            def health_check(self): return {"status": "healthy"}

        reg = TravelProviderRegistry()
        reg.register(DuplicateMockProvider())
        svc = ProviderSearchService(reg)
        results = svc.search({})
        self.assertEqual(len(results), 1, "Duplicate package with same provider+external_id should be deduplicated")

    # 7. Disabled provider behavior
    def test_disabled_provider_behavior(self):
        viator = provider_registry.get("viator")
        self.assertFalse(viator.is_enabled)
        # Search returns empty list, does not throw or execute network calls
        self.assertEqual(viator.search_packages({}), [])
        self.assertIsNone(viator.get_package_details("123"))

    # 8. Missing provider credentials behavior
    def test_missing_credentials_behavior(self):
        booking = provider_registry.get("booking")
        self.assertFalse(booking.is_enabled)
        h = booking.health_check()
        self.assertEqual(h["status"], "disabled")
        self.assertFalse(h["enabled"])

    # 9. Provider health endpoint
    def test_provider_health_endpoint(self):
        res = self.client.get('/api/v1/providers')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        provs = {p["provider"]: p for p in data["data"]}
        
        self.assertIn("demo", provs)
        self.assertEqual(provs["demo"]["status"], "healthy")
        self.assertEqual(provs["demo"]["source_type"], "demo")
        self.assertTrue(provs["demo"]["enabled"])

        self.assertIn("viator", provs)
        self.assertEqual(provs["viator"]["status"], "disabled")
        self.assertFalse(provs["viator"]["enabled"])

        self.assertIn("booking", provs)
        self.assertEqual(provs["booking"]["status"], "disabled")

    # 10. Demo provider search endpoint
    def test_provider_search_api_endpoint(self):
        res = self.client.get('/api/v1/providers/search?starting_city=Mumbai&interest=Beach&provider=demo')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(len(data["data"]), 1)
        pkg = data["data"][0]
        self.assertEqual(pkg["provider"], "demo")
        self.assertEqual(pkg["source_type"], "demo")
        self.assertEqual(pkg["name"], "Goa Sun & Sand Explorer")

    # 11. Existing package search remains correct
    def test_existing_package_search_correctness(self):
        res = self.client.get('/api/v1/packages?starting_city=Mumbai&interest=Beach')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(len(data["data"]), 1)
        self.assertEqual(data["data"][0]["provider"], "demo")
        self.assertEqual(data["data"][0]["source_type"], "demo")

    # 12. Existing discovery remains correct
    def test_existing_discovery_correctness(self):
        res = self.client.get('/api/v1/discover/destinations?starting_city=Mumbai&interest=Beach&budget=50000&travellers=1&duration_days=4&travel_type=Couple&month=11')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(len(data["data"]), 1)
        self.assertEqual(data["data"][0]["destination_name"], "Goa")

    # 13. Existing recommendations remain correct
    def test_existing_recommendations_correctness(self):
        res = self.client.get('/api/v1/recommendations/packages?starting_city=Mumbai&interest=Beach&budget=50000&travellers=1&duration_days=4&travel_type=Couple&month=11')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(len(data["data"]), 1)
        self.assertEqual(data["data"][0]["name"], "Goa Sun & Sand Explorer")
        self.assertEqual(data["data"][0]["match_score"], 100)

    # 14. Existing comparison compatibility
    def test_existing_comparison_compatibility(self):
        pkg = Package.query.filter_by(name="Goa Sun & Sand Explorer").first()
        res = self.client.get(f'/api/v1/packages/{pkg.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(data["data"]["provider"], "demo")
        self.assertEqual(data["data"]["source_type"], "demo")
        self.assertEqual(len(data["data"]["itinerary"]), 1)
        self.assertEqual(len(data["data"]["inclusions"]), 1)

    # 15. Beach remains a hard interest filter
    def test_beach_hard_interest_filter(self):
        # Manali is adventure, not beach. Searching Mumbai + Beach should NEVER return Manali
        res = self.client.get('/api/v1/packages?starting_city=Delhi&interest=Beach')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data["data"]), 0, "No Beach packages exist from Delhi in test data")

    # 16. Starting city remains a hard filter
    def test_starting_city_hard_filter(self):
        res = self.client.get('/api/v1/packages?starting_city=Pune&interest=Beach')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data["data"]), 0, "No Beach packages exist from Pune in test data")

    # 17. Explicit destination remains a hard filter
    def test_destination_hard_filter(self):
        dest_manali = Destination.query.filter_by(name="Manali").first()
        res = self.client.get(f'/api/v1/packages?destination_id={dest_manali.id}&starting_city=Mumbai')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data["data"]), 0, "Manali packages do not depart from Mumbai in test data")

    # 18. No inactive demo packages returned
    def test_no_inactive_packages_returned(self):
        res = self.client.get('/api/v1/packages?starting_city=Mumbai&interest=Beach')
        names = [p["name"] for p in res.get_json()["data"]]
        self.assertNotIn("Inactive Goa Tour", names)

    # 19. API error format remains consistent
    def test_api_error_format_consistency(self):
        res = self.client.get('/api/v1/providers/search?travellers=-1')
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertFalse(data["success"])
        self.assertIn("error", data)
        self.assertIn("message", data["error"])

    # 20. No secrets are exposed
    def test_no_secrets_exposed(self):
        res = self.client.get('/api/v1/providers')
        data_str = res.get_data(as_text=True)
        self.assertNotIn("api_key", data_str.lower())
        self.assertNotIn("secret", data_str.lower())
        self.assertNotIn("password", data_str.lower())
