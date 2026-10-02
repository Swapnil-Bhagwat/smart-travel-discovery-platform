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
    PackageExclusion,
    PackageInclusion,
    PackageItinerary,
    PackageTravelType,
)
from app.models.theme import Theme


class TestPackageConfig(Config):
    """Isolated in-memory database for package tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestPackageAPIs(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestPackageConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._seed_data()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def _seed_data(self):
        # Operators
        self.op1 = Operator(name='Alpine Voyages', website_url='https://alpine.com', rating=Decimal('4.8'))
        self.op2 = Operator(name='Seaside Tours', website_url='https://seaside.com', rating=Decimal('4.5'))
        db.session.add_all([self.op1, self.op2])

        # Destinations
        self.dest1 = Destination(name='Manali', country='India', region='Himachal Pradesh')
        self.dest2 = Destination(name='Phuket', country='Thailand', region='Southern Thailand')
        db.session.add_all([self.dest1, self.dest2])

        # Themes
        self.th_adv = Theme(name='Adventure', slug='adventure', description='Thrills and treks')
        self.th_bch = Theme(name='Beach', slug='beach', description='Coastal relaxation')
        self.th_rom = Theme(name='Romantic', slug='romantic', description='Couples getaways')
        self.th_cul = Theme(name='Culture', slug='culture', description='Art and heritage')
        db.session.add_all([self.th_adv, self.th_bch, self.th_rom, self.th_cul])
        db.session.commit()

        # Package 1: Active, Manali, Delhi, 5 days, 10000/person, Adventure+Romantic, Couple+Group, Months 5,6,12
        self.pkg1 = Package(
            operator_id=self.op1.id,
            destination_id=self.dest1.id,
            name='Himalayan Escape',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('10000.00'),
            featured_image_url='https://images.unsplash.com/manali.jpg',
            source_url='https://alpine.com/packages/manali',
            is_active=True,
            hotel_info='4-star mountain lodge',
            meals_info='Breakfast and dinner included',
            transportation_info='AC Volvo from Delhi',
            sightseeing_info='Solang Valley and Rohtang Pass',
            activities_info='River rafting, paragliding'
        )
        self.pkg1.themes.extend([self.th_adv, self.th_rom])
        db.session.add(self.pkg1)
        db.session.flush()

        # Child records for Package 1
        db.session.add_all([
            PackageTravelType(package_id=self.pkg1.id, travel_type='Couple'),
            PackageTravelType(package_id=self.pkg1.id, travel_type='Group'),
            PackageAvailabilityMonth(package_id=self.pkg1.id, month=5),
            PackageAvailabilityMonth(package_id=self.pkg1.id, month=6),
            PackageAvailabilityMonth(package_id=self.pkg1.id, month=12),
            PackageItinerary(package_id=self.pkg1.id, day_number=1, title='Arrival in Manali', description='Check-in and local market stroll.'),
            PackageItinerary(package_id=self.pkg1.id, day_number=2, title='Solang Valley Excursion', description='Full day snow activities.'),
            PackageInclusion(package_id=self.pkg1.id, description='4 nights stay in luxury room'),
            PackageInclusion(package_id=self.pkg1.id, description='Daily breakfast and dinner'),
            PackageExclusion(package_id=self.pkg1.id, description='Personal expenses and tips')
        ])

        # Package 2: Active, Phuket, Mumbai, 7 days, 25000/person, Beach+Romantic, Couple+Family, Months 11,12,1
        self.pkg2 = Package(
            operator_id=self.op2.id,
            destination_id=self.dest2.id,
            name='Phuket Beach Bliss',
            starting_city='Mumbai',
            duration_days=7,
            duration_nights=6,
            price_per_person=Decimal('25000.00'),
            featured_image_url='https://images.unsplash.com/phuket.jpg',
            source_url='https://seaside.com/packages/phuket',
            is_active=True,
            hotel_info='5-star beach resort',
            meals_info='All-inclusive meals',
            transportation_info='Speedboat and private van transfers',
            sightseeing_info='Phi Phi Islands, Big Buddha',
            activities_info='Snorkeling, island hopping'
        )
        self.pkg2.themes.extend([self.th_bch, self.th_rom])
        db.session.add(self.pkg2)
        db.session.flush()

        db.session.add_all([
            PackageTravelType(package_id=self.pkg2.id, travel_type='Couple'),
            PackageTravelType(package_id=self.pkg2.id, travel_type='Family'),
            PackageAvailabilityMonth(package_id=self.pkg2.id, month=11),
            PackageAvailabilityMonth(package_id=self.pkg2.id, month=12),
            PackageAvailabilityMonth(package_id=self.pkg2.id, month=1),
            PackageItinerary(package_id=self.pkg2.id, day_number=1, title='Welcome to Phuket', description='Airport greeting and transfer.'),
            PackageInclusion(package_id=self.pkg2.id, description='Speedboat tour to Phi Phi islands'),
            PackageExclusion(package_id=self.pkg2.id, description='Thailand visa fees')
        ])

        # Package 3: INACTIVE package (should NEVER appear in search results)
        self.pkg3 = Package(
            operator_id=self.op1.id,
            destination_id=self.dest1.id,
            name='Inactive Manali Winter Trip',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('9000.00'),
            source_url='https://alpine.com/packages/inactive',
            is_active=False
        )
        db.session.add(self.pkg3)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.pkg3.id, travel_type='Solo'),
            PackageAvailabilityMonth(package_id=self.pkg3.id, month=12)
        ])

        # Package 4: Active, Manali, Delhi, 3 days, 6000/person, Adventure, Solo, Months 6,7,8
        self.pkg4 = Package(
            operator_id=self.op1.id,
            destination_id=self.dest1.id,
            name='Solo Trekker Express',
            starting_city='Delhi',
            duration_days=3,
            duration_nights=2,
            price_per_person=Decimal('6000.00'),
            source_url='https://alpine.com/packages/solo-trek',
            is_active=True
        )
        self.pkg4.themes.extend([self.th_adv, self.th_cul])
        db.session.add(self.pkg4)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.pkg4.id, travel_type='Solo'),
            PackageAvailabilityMonth(package_id=self.pkg4.id, month=6),
            PackageAvailabilityMonth(package_id=self.pkg4.id, month=7),
            PackageAvailabilityMonth(package_id=self.pkg4.id, month=8)
        ])

        db.session.commit()

    # --- Test Cases ---

    def test_01_package_list_no_filters(self):
        """1. Package list with no filters returns all active packages."""
        res = self.client.get('/api/v1/packages')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        # Should return exactly 3 active packages (pkg1, pkg2, pkg4)
        self.assertEqual(len(data['data']), 3)
        self.assertEqual(data['pagination']['total'], 3)
        pkg_ids = [p['id'] for p in data['data']]
        self.assertIn(self.pkg1.id, pkg_ids)
        self.assertIn(self.pkg2.id, pkg_ids)
        self.assertIn(self.pkg4.id, pkg_ids)

    def test_02_filter_by_starting_city(self):
        """2. Filter by starting city with case-insensitive matching."""
        res = self.client.get('/api/v1/packages?starting_city=delhi')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 2)
        for p in data['data']:
            self.assertEqual(p['starting_city'].lower(), 'delhi')

    def test_03_filter_by_destination(self):
        """3. Filter by destination ID."""
        res = self.client.get(f'/api/v1/packages?destination_id={self.dest2.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data['data']), 1)
        self.assertEqual(data['data'][0]['name'], 'Phuket Beach Bliss')
        self.assertEqual(data['data'][0]['destination']['name'], 'Phuket')

    def test_04_filter_by_budget_and_travellers(self):
        """4. Filter by total trip budget and number of travellers."""
        # For 2 travellers with a budget of 25000:
        # Max per person = 12500.
        # Pkg1: 10000 * 2 = 20000 <= 25000 (Matches!)
        # Pkg4: 6000 * 2 = 12000 <= 25000 (Matches!)
        # Pkg2: 25000 * 2 = 50000 > 25000 (Exceeds budget!)
        res = self.client.get('/api/v1/packages?budget=25000&travellers=2')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data['data']), 2)
        pkg_ids = [p['id'] for p in data['data']]
        self.assertIn(self.pkg1.id, pkg_ids)
        self.assertIn(self.pkg4.id, pkg_ids)
        self.assertNotIn(self.pkg2.id, pkg_ids)

        # Check total estimated cost calculation
        pkg1_data = next(p for p in data['data'] if p['id'] == self.pkg1.id)
        self.assertEqual(pkg1_data['requested_travellers'], 2)
        self.assertEqual(pkg1_data['estimated_total_cost'], 20000.0)

    def test_05_filter_by_duration(self):
        """5. Duration is a soft preference: exact match ranks highest, others not eliminated."""
        res = self.client.get('/api/v1/packages?duration_days=7')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        # All 3 active packages are returned (not eliminated), Phuket ranks first with 100
        self.assertEqual(len(data['data']), 3)
        self.assertEqual(data['data'][0]['name'], 'Phuket Beach Bliss')
        self.assertEqual(data['data'][0]['duration_days'], 7)
        self.assertEqual(data['data'][0]['match_score'], 100)
        self.assertLess(data['data'][1]['match_score'], 100)

    def test_06_filter_by_travel_type(self):
        """6. Travel type is a soft preference: matching travel type ranks highest."""
        res = self.client.get('/api/v1/packages?travel_type=Solo')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        # Solo Trekker Express matches Solo and ranks #1
        self.assertEqual(len(data['data']), 3)
        self.assertEqual(data['data'][0]['name'], 'Solo Trekker Express')
        self.assertEqual(data['data'][0]['match_score'], 100)

        # Case-insensitive / normalized test
        res_couple = self.client.get('/api/v1/packages?travel_type=couple')
        self.assertEqual(res_couple.status_code, 200)
        data_couple = res_couple.get_json()
        # Couple matches Pkg1 and Pkg2 (100), Pkg4 has Solo (80)
        top_names = [p['name'] for p in data_couple['data'][:2]]
        self.assertIn('Himalayan Escape', top_names)
        self.assertIn('Phuket Beach Bliss', top_names)

    def test_07_filter_by_interest_theme(self):
        """7. Travel interest is a hard filter: only matching themes appear."""
        # 1. By Name: Beach -> only Phuket Beach Bliss has Beach theme
        res_name = self.client.get('/api/v1/packages?interest=Beach')
        self.assertEqual(res_name.status_code, 200)
        data_name = res_name.get_json()
        self.assertEqual(len(data_name['data']), 1)
        self.assertEqual(data_name['data'][0]['name'], 'Phuket Beach Bliss')
        self.assertEqual(data_name['data'][0]['match_score'], 100)

        # 2. By Slug (case-insensitive): adventure -> Himalayan Escape and Solo Trekker Express
        res_slug = self.client.get('/api/v1/packages?interest=adventure')
        self.assertEqual(res_slug.status_code, 200)
        data_slug = res_slug.get_json()
        self.assertEqual(len(data_slug['data']), 2)
        adv_names = [p['name'] for p in data_slug['data']]
        self.assertIn('Himalayan Escape', adv_names)
        self.assertIn('Solo Trekker Express', adv_names)
        self.assertNotIn('Phuket Beach Bliss', adv_names)

        # 3. By Name: Culture -> only Solo Trekker Express
        res_cul = self.client.get('/api/v1/packages?interest=Culture')
        self.assertEqual(res_cul.status_code, 200)
        data_cul = res_cul.get_json()
        self.assertEqual(len(data_cul['data']), 1)
        self.assertEqual(data_cul['data'][0]['name'], 'Solo Trekker Express')

    def test_08_filter_by_month(self):
        """8. Operating calendar month is a soft preference."""
        # Month 1 (January) -> Phuket operates in Jan, ranks first
        res_jan = self.client.get('/api/v1/packages?month=1')
        self.assertEqual(res_jan.status_code, 200)
        data_jan = res_jan.get_json()
        self.assertEqual(len(data_jan['data']), 3)
        self.assertEqual(data_jan['data'][0]['name'], 'Phuket Beach Bliss')
        self.assertEqual(data_jan['data'][0]['match_score'], 100)

        # Month 6 (June) -> Pkg1 and Pkg4 operate in June, rank top
        res_jun = self.client.get('/api/v1/packages?month=6')
        self.assertEqual(res_jun.status_code, 200)
        data_jun = res_jun.get_json()
        top_jun = [p['name'] for p in data_jun['data'][:2]]
        self.assertIn('Himalayan Escape', top_jun)
        self.assertIn('Solo Trekker Express', top_jun)

    def test_09_combined_filters(self):
        """9. Multi-criteria search returns exact matches top and close alternatives below."""
        # Search: Delhi, Budget 25000 for 2 travellers, 5 days, Couple, Adventure, Month 12
        url = (
            '/api/v1/packages'
            '?starting_city=Delhi'
            '&budget=25000'
            '&travellers=2'
            '&duration_days=5'
            '&travel_type=Couple'
            '&interest=Adventure'
            '&month=12'
        )
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        # Both Delhi packages returned: Pkg1 (exact match, 100), Pkg4 (close match, 55)
        self.assertEqual(len(data['data']), 2)
        self.assertEqual(data['data'][0]['id'], self.pkg1.id)
        self.assertEqual(data['data'][0]['name'], 'Himalayan Escape')
        self.assertEqual(data['data'][0]['match_score'], 100)
        self.assertEqual(data['data'][0]['budget_status'], 'within_budget')
        self.assertEqual(data['data'][0]['budget_difference'], 0.0)
        self.assertEqual(data['data'][0]['estimated_total_cost'], 20000.0)

        self.assertEqual(data['data'][1]['id'], self.pkg4.id)
        self.assertEqual(data['data'][1]['name'], 'Solo Trekker Express')
        self.assertEqual(data['data'][1]['match_score'], 55)

    def test_10_only_active_packages_returned(self):
        """10. Verify inactive packages are never included in query results."""
        # Pkg3 is inactive, in Delhi, month 12
        res = self.client.get('/api/v1/packages?starting_city=Delhi&month=12')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        pkg_ids = [p['id'] for p in data['data']]
        self.assertNotIn(self.pkg3.id, pkg_ids)

    def test_11_pagination(self):
        """11. Verify pagination limit and pages calculation."""
        res = self.client.get('/api/v1/packages?page=1&per_page=2')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data['data']), 2)
        self.assertEqual(data['pagination']['page'], 1)
        self.assertEqual(data['pagination']['per_page'], 2)
        self.assertEqual(data['pagination']['total'], 3)
        self.assertEqual(data['pagination']['pages'], 2)

        # Page 2
        res2 = self.client.get('/api/v1/packages?page=2&per_page=2')
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(len(res2.get_json()['data']), 1)

    def test_12_invalid_travellers_400(self):
        """12. Validate travellers parameter (must be >= 1)."""
        for invalid in ['0', '-1', 'abc']:
            res = self.client.get(f'/api/v1/packages?travellers={invalid}')
            self.assertEqual(res.status_code, 400)
            data = res.get_json()
            self.assertFalse(data['success'])
            self.assertIn("travellers", data['error']['message'])

    def test_13_invalid_month_400(self):
        """13. Validate month parameter (must be 1 to 12)."""
        for invalid in ['0', '13', '-5', 'nov']:
            res = self.client.get(f'/api/v1/packages?month={invalid}')
            self.assertEqual(res.status_code, 400)
            data = res.get_json()
            self.assertFalse(data['success'])
            self.assertIn("month", data['error']['message'])

    def test_14_invalid_travel_type_400(self):
        """14. Validate travel_type parameter (must be Solo, Couple, Family, Group)."""
        res = self.client.get('/api/v1/packages?travel_type=Business')
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertIn("travel_type", data['error']['message'])

    def test_15_package_detail_endpoint(self):
        """15. Complete package detail endpoint with itinerary, inclusions, exclusions."""
        res = self.client.get(f'/api/v1/packages/{self.pkg1.id}?travellers=3')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        pkg = data['data']
        self.assertEqual(pkg['id'], self.pkg1.id)
        self.assertEqual(pkg['name'], 'Himalayan Escape')
        self.assertEqual(pkg['requested_travellers'], 3)
        self.assertEqual(pkg['estimated_total_cost'], 30000.0)
        self.assertEqual(pkg['operator']['name'], 'Alpine Voyages')
        self.assertEqual(pkg['destination']['name'], 'Manali')
        self.assertEqual(pkg['hotel_info'], '4-star mountain lodge')
        self.assertEqual(len(pkg['itinerary']), 2)
        self.assertEqual(pkg['itinerary'][0]['day_number'], 1)
        self.assertEqual(len(pkg['inclusions']), 2)
        self.assertEqual(len(pkg['exclusions']), 1)

    def test_16_package_not_found_404(self):
        """16. Package not found returns 404."""
        res = self.client.get('/api/v1/packages/9999')
        self.assertEqual(res.status_code, 404)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error']['message'], 'Package with id 9999 not found')

    def test_17_no_duplicate_results_on_multi_joins(self):
        """17. Ensure distinct results and no duplicates across multiple joins."""
        res = self.client.get('/api/v1/packages?travel_type=Couple&month=12&interest=Adventure')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        pkg_ids = [p['id'] for p in data['data']]
        # No duplicates
        self.assertEqual(len(pkg_ids), len(set(pkg_ids)))
        self.assertEqual(data['data'][0]['id'], self.pkg1.id)

    def test_18_exact_package_match_ranks_highly(self):
        """18. Exact package match receives maximum 100 match score."""
        url = (
            '/api/v1/packages'
            '?starting_city=Delhi'
            '&budget=25000'
            '&travellers=2'
            '&duration_days=5'
            '&travel_type=Couple'
            '&interest=Adventure'
            '&month=12'
        )
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(data[0]['match_score'], 100)
        self.assertEqual(data[0]['budget_status'], 'within_budget')

    def test_19_different_duration_returns_close_package(self):
        """19. Different duration returns close package with deducted duration points."""
        # Request 7 days for Delhi; Pkg1 has 5 days (diff 2 -> 15 pts), Pkg4 has 3 days (diff 4 -> 5 pts)
        url = '/api/v1/packages?starting_city=Delhi&duration_days=7&travellers=2&budget=25000'
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 2)
        # Pkg1 has diff 2 -> score 90 (15 dur + 25 int + 20 tt + 15 m + 15 bud)
        self.assertEqual(data[0]['id'], self.pkg1.id)
        self.assertEqual(data[0]['match_score'], 90)

    def test_20_different_travel_type_returns_close_package(self):
        """20. Different travel type still returns close package."""
        # Request Family for Delhi; Pkg1 has Couple/Group (0), Pkg4 has Solo (0)
        url = '/api/v1/packages?starting_city=Delhi&travel_type=Family&travellers=2&budget=25000'
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 2)
        # Packages still returned with 80 score (losing 20 travel type points)
        self.assertEqual(data[0]['match_score'], 80)

    def test_21_different_month_returns_close_package(self):
        """21. Different month still returns close package."""
        # Month 10: neither Pkg1 nor Pkg4 operates in Month 10
        url = '/api/v1/packages?starting_city=Delhi&month=10&travellers=2&budget=25000'
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 2)
        # Returned with 85 score (losing 15 month points)
        self.assertEqual(data[0]['match_score'], 85)

    def test_22_package_without_requested_interest_is_excluded(self):
        """22. A package without the requested interest is excluded even when all other preferences match."""
        # Request Heritage for Delhi; no Delhi packages have Heritage
        url = (
            '/api/v1/packages'
            '?starting_city=Delhi'
            '&interest=Heritage'
            '&duration_days=5'
            '&travel_type=Couple'
            '&month=12'
            '&budget=25000'
            '&travellers=2'
        )
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 0)
        self.assertIn("No packages match the selected travel interest", res.get_json()['message'])

    def test_23_packages_up_to_20_percent_over_budget_fallback(self):
        """23. When no package is within budget, packages up to 20% over budget appear as fallback."""
        # For Delhi: Pkg4 cost is 6000 for 1 traveller.
        # Budget = 5500:
        # Pkg4 cost (6000) is 9.09% over budget (< 20% over budget).
        # Since NO package is <= 5500, fallback activates!
        res = self.client.get('/api/v1/packages?starting_city=Delhi&budget=5500&travellers=1')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 1)
        pkg = data[0]
        self.assertEqual(pkg['id'], self.pkg4.id)
        self.assertEqual(pkg['budget_status'], 'over_budget')
        self.assertEqual(pkg['budget_difference'], 500.0)
        # 1-10% over budget receives +10 budget points instead of +15 -> score 95
        self.assertEqual(pkg['match_score'], 95)

    def test_24_more_than_20_percent_over_budget_excluded(self):
        """24. Packages more than 20% over budget do not appear as fallback."""
        # Lowest cost in Delhi is 6000.
        # Budget = 4000: 20% above budget is 4800. Pkg4 (6000) > 4800.
        res = self.client.get('/api/v1/packages?starting_city=Delhi&budget=4000&travellers=1')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 0)

    def test_25_destination_filter_remains_hard(self):
        """25. Destination filter remains hard when explicitly selected."""
        res = self.client.get(f'/api/v1/packages?destination_id={self.dest1.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        # Only Manali packages (pkg1, pkg4), never Phuket (dest2)
        dest_ids = {p['destination']['id'] for p in data}
        self.assertEqual(dest_ids, {self.dest1.id})

    def test_26_starting_city_filter_remains_hard(self):
        """26. Starting city filter remains hard when explicitly selected."""
        res = self.client.get('/api/v1/packages?starting_city=Delhi')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        cities = {p['starting_city'] for p in data}
        self.assertEqual(cities, {'Delhi'})


if __name__ == '__main__':
    unittest.main()
