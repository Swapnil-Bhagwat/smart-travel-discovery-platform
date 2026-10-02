import unittest
from decimal import Decimal

from app import create_app
from app.config import Config
from app.extensions import db
from app.models.destination import Destination
from app.models.operator import Operator
from app.models.package import (
    Package,
    PackageAvailabilityMonth,
    PackageTravelType,
)
from app.models.theme import Theme


class TestHardFilterConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestInterestHardFilter(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestHardFilterConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        # Seed Operators
        self.op1 = Operator(name='Summit Adventures', website_url='https://summit.example.com', rating=Decimal('4.8'))
        self.op2 = Operator(name='Coastal Escapes', website_url='https://coastal.example.com', rating=Decimal('4.5'))
        db.session.add_all([self.op1, self.op2])
        db.session.commit()

        # Seed Destinations
        self.dest_manali = Destination(name='Manali', country='India', region='Himachal Pradesh')
        self.dest_goa = Destination(name='Goa', country='India', region='Goa')
        self.dest_jaipur = Destination(name='Jaipur', country='India', region='Rajasthan')
        db.session.add_all([self.dest_manali, self.dest_goa, self.dest_jaipur])
        db.session.commit()

        # Seed Themes
        self.th_beach = Theme(name='Beach', slug='beach', description='Beaches and coastal life')
        self.th_adv = Theme(name='Adventure', slug='adventure', description='Trekking and adventures')
        self.th_cul = Theme(name='Culture', slug='culture', description='Culture and heritage')
        self.th_nat = Theme(name='Nature', slug='nature', description='Nature and landscapes')
        db.session.add_all([self.th_beach, self.th_adv, self.th_cul, self.th_nat])
        db.session.commit()

        # Seed Packages
        # P1: Manali (Delhi, 5 days, 10000/person, Themes: Adventure + Nature, Couple, Month 12, Active)
        self.p1 = Package(
            operator_id=self.op1.id, destination_id=self.dest_manali.id,
            name='Manali Alpine Trek', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('10000.00'), source_url='https://example.com/p1', is_active=True
        )
        self.p1.themes.extend([self.th_adv, self.th_nat])
        db.session.add(self.p1)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.p1.id, travel_type='Couple'),
            PackageAvailabilityMonth(package_id=self.p1.id, month=12)
        ])

        # P2: Manali (Delhi, 4 days, 8000/person, Themes: Adventure, Solo, Month 12, Active) - 2nd package in Manali for aggregation
        self.p2 = Package(
            operator_id=self.op1.id, destination_id=self.dest_manali.id,
            name='Manali Quick Explorer', starting_city='Delhi', duration_days=4, duration_nights=3,
            price_per_person=Decimal('8000.00'), source_url='https://example.com/p2', is_active=True
        )
        self.p2.themes.append(self.th_adv)
        db.session.add(self.p2)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.p2.id, travel_type='Solo'),
            PackageAvailabilityMonth(package_id=self.p2.id, month=12)
        ])

        # P3: Goa (Delhi, 5 days, 12000/person, Themes: Beach + Nature, Couple, Month 12, Active)
        self.p3 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Tropical Retreat', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('12000.00'), source_url='https://example.com/p3', is_active=True
        )
        self.p3.themes.extend([self.th_beach, self.th_nat])
        db.session.add(self.p3)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.p3.id, travel_type='Couple'),
            PackageAvailabilityMonth(package_id=self.p3.id, month=12)
        ])

        # P4: Jaipur (Delhi, 5 days, 7000/person, Themes: Culture, Couple, Month 10, Active)
        self.p4 = Package(
            operator_id=self.op1.id, destination_id=self.dest_jaipur.id,
            name='Jaipur Royal Heritage', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('7000.00'), source_url='https://example.com/p4', is_active=True
        )
        self.p4.themes.append(self.th_cul)
        db.session.add(self.p4)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.p4.id, travel_type='Couple'),
            PackageAvailabilityMonth(package_id=self.p4.id, month=10)
        ])

        # P5: Manali (Delhi, Inactive package)
        self.p5 = Package(
            operator_id=self.op1.id, destination_id=self.dest_manali.id,
            name='Manali Winter Special (Inactive)', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('5000.00'), source_url='https://example.com/p5', is_active=False
        )
        self.p5.themes.extend([self.th_adv, self.th_beach])
        db.session.add(self.p5)

        # P6: Goa (Mumbai, starting city is Mumbai, Active, Beach)
        self.p6 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Beach Weekend from Mumbai', starting_city='Mumbai', duration_days=5, duration_nights=4,
            price_per_person=Decimal('11000.00'), source_url='https://example.com/p6', is_active=True
        )
        self.p6.themes.append(self.th_beach)
        db.session.add(self.p6)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.p6.id, travel_type='Couple'),
            PackageAvailabilityMonth(package_id=self.p6.id, month=12)
        ])

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # 1. Interest = Beach returns only packages with Beach theme.
    def test_01_interest_beach_returns_only_beach_packages(self):
        res = self.client.get('/api/v1/packages?interest=Beach')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertGreater(len(data), 0)
        for pkg in data:
            theme_names = [t['name'] for t in pkg['themes']]
            self.assertIn('Beach', theme_names)
            self.assertNotIn(pkg['name'], ['Manali Alpine Trek', 'Jaipur Royal Heritage'])

    # 2. Interest = Adventure returns only packages with Adventure theme.
    def test_02_interest_adventure_returns_only_adventure_packages(self):
        res = self.client.get('/api/v1/packages?interest=Adventure')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertGreater(len(data), 0)
        for pkg in data:
            theme_names = [t['name'] for t in pkg['themes']]
            self.assertIn('Adventure', theme_names)
            self.assertNotIn(pkg['name'], ['Goa Tropical Retreat', 'Jaipur Royal Heritage'])

    # 3. Interest = Culture returns only packages with Culture theme.
    def test_03_interest_culture_returns_only_culture_packages(self):
        res = self.client.get('/api/v1/packages?interest=Culture')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Jaipur Royal Heritage')
        theme_names = [t['name'] for t in data[0]['themes']]
        self.assertIn('Culture', theme_names)

    # 4. A package without the requested interest is excluded even when all other preferences match.
    def test_04_package_without_requested_interest_excluded_when_all_other_match(self):
        # Query with criteria matching P1 (Delhi, 5 days, 20000 budget, Couple, Month 12), BUT interest=Culture
        # P1 has Adventure+Nature, NOT Culture -> MUST be excluded!
        res = self.client.get(
            '/api/v1/packages?starting_city=Delhi&budget=25000&travellers=2&duration_days=5&interest=Culture&travel_type=Couple&month=12'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        pkg_names = [p['name'] for p in data]
        self.assertNotIn('Manali Alpine Trek', pkg_names)
        self.assertIn('Jaipur Royal Heritage', pkg_names)

    # 5. A destination without any matching-interest package is excluded from discovery.
    def test_05_destination_without_matching_interest_package_excluded_from_discovery(self):
        # Query discovery for Beach in Delhi: only Goa has active Beach package from Delhi.
        # Manali and Jaipur have NO active Beach packages from Delhi.
        res = self.client.get(
            '/api/v1/discover/destinations?starting_city=Delhi&budget=30000&travellers=2&duration_days=5&interest=Beach&travel_type=Couple&month=12'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        dest_names = [d['destination_name'] for d in data]
        self.assertEqual(dest_names, ['Goa'])
        self.assertNotIn('Manali', dest_names)
        self.assertNotIn('Jaipur', dest_names)

    # 6. Multiple packages within the same destination aggregate correctly.
    def test_06_multiple_packages_aggregate_correctly_in_discovery(self):
        # Query Adventure for Delhi: Manali has 2 active packages (P1 and P2)
        res = self.client.get(
            '/api/v1/discover/destinations?starting_city=Delhi&budget=30000&travellers=2&duration_days=5&interest=Adventure&travel_type=Couple&month=12'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        manali = next(d for d in data if d['destination_name'] == 'Manali')
        self.assertEqual(manali['matching_package_count'], 2)
        self.assertEqual(manali['lowest_price_per_person'], 8000.0)
        self.assertEqual(manali['lowest_estimated_total_cost'], 16000.0)

    # 7. Budget flexibility still works (within budget preferred, up to 20% over budget fallback).
    def test_07_budget_flexibility_works(self):
        # Query with low budget where only fallback (<= 20% over budget) can match:
        # P3 in Goa costs 12000/person = 24000 total for 2 travellers.
        # Budget = 21000: 21000 * 1.20 = 25200. P3 (24000) is 14.3% over budget (<= 20%).
        res = self.client.get(
            '/api/v1/packages?starting_city=Delhi&budget=21000&travellers=2&interest=Beach'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Goa Tropical Retreat')
        self.assertEqual(data[0]['budget_status'], 'over_budget')

    # 8. Duration remains soft.
    def test_08_duration_remains_soft(self):
        # P1 is 5 days, P2 is 4 days. Query with duration_days=7 (difference of 2 and 3)
        res = self.client.get(
            '/api/v1/packages?starting_city=Delhi&interest=Adventure&duration_days=7'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 2)
        # Packages still returned even though duration differed

    # 9. Travel type remains soft.
    def test_09_travel_type_remains_soft(self):
        # P1 has Couple, P2 has Solo. Query with travel_type=Family (neither has Family)
        res = self.client.get(
            '/api/v1/packages?starting_city=Delhi&interest=Adventure&travel_type=Family'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 2)
        # Both packages returned despite non-matching travel type

    # 10. Month remains soft.
    def test_10_month_remains_soft(self):
        # P1 and P2 have month 12. Query with month=4
        res = self.client.get(
            '/api/v1/packages?starting_city=Delhi&interest=Adventure&month=4'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 2)
        # Both packages returned despite operating in month 12

    # 11. Starting city remains hard.
    def test_11_starting_city_remains_hard(self):
        # Query with starting_city=Delhi: P6 starts in Mumbai -> MUST be excluded
        res = self.client.get('/api/v1/packages?starting_city=Delhi&interest=Beach')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        for p in data:
            self.assertEqual(p['starting_city'], 'Delhi')
            self.assertNotEqual(p['name'], 'Goa Beach Weekend from Mumbai')

    # 12. Explicit destination remains hard.
    def test_12_explicit_destination_remains_hard(self):
        # Query with destination_id of Manali
        res = self.client.get(f'/api/v1/packages?destination_id={self.dest_manali.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        for p in data:
            self.assertEqual(p['destination']['id'], self.dest_manali.id)

    # 13. Inactive packages remain excluded.
    def test_13_inactive_packages_remain_excluded(self):
        # P5 is inactive and has Beach and Adventure
        res = self.client.get('/api/v1/packages?interest=Beach')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        ids = [p['id'] for p in data]
        self.assertNotIn(self.p5.id, ids)

    # 14. No duplicate package results.
    def test_14_no_duplicate_package_results(self):
        res = self.client.get('/api/v1/packages?interest=Adventure')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        ids = [p['id'] for p in data]
        self.assertEqual(len(ids), len(set(ids)))

    # 15. No duplicate destination results.
    def test_15_no_duplicate_destination_results(self):
        res = self.client.get(
            '/api/v1/discover/destinations?starting_city=Delhi&budget=40000&travellers=2&duration_days=5&interest=Adventure&travel_type=Couple&month=12'
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        dest_ids = [d['destination_id'] for d in data]
        self.assertEqual(len(dest_ids), len(set(dest_ids)))

    # 16. Empty results work correctly when no interest match exists.
    def test_16_empty_results_when_no_interest_match_exists(self):
        # Packages search with non-existent interest
        res_pkg = self.client.get('/api/v1/packages?interest=NonExistentInterest')
        self.assertEqual(res_pkg.status_code, 200)
        json_pkg = res_pkg.get_json()
        self.assertEqual(json_pkg['data'], [])
        self.assertIn("No packages match the selected travel interest", json_pkg['message'])

        # Discover destinations with non-existent interest
        res_disc = self.client.get(
            '/api/v1/discover/destinations?starting_city=Delhi&budget=40000&travellers=2&duration_days=5&interest=NonExistentInterest&travel_type=Couple&month=12'
        )
        self.assertEqual(res_disc.status_code, 200)
        json_disc = res_disc.get_json()
        self.assertEqual(json_disc['data'], [])
        self.assertIn("No destinations currently have packages matching your selected travel interest", json_disc['message'])


if __name__ == '__main__':
    unittest.main()
