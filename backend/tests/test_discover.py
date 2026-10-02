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


class TestDiscoverConfig(Config):
    """Isolated in-memory database for discovery tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestDiscoverAPIs(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestDiscoverConfig)
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
        # Operator
        self.operator = Operator(name='Discovery Voyages', rating=Decimal('4.9'))
        db.session.add(self.operator)

        # Destinations
        self.dest_manali = Destination(name='Manali', country='India', region='Himachal Pradesh', description='Snowy peaks')
        self.dest_goa = Destination(name='Goa', country='India', region='Western India', description='Sunny beaches')
        self.dest_jaipur = Destination(name='Jaipur', country='India', region='Rajasthan', description='Pink city palaces')
        db.session.add_all([self.dest_manali, self.dest_goa, self.dest_jaipur])

        # Themes
        self.th_adv = Theme(name='Adventure', slug='adventure', description='Trekking & thrills')
        self.th_bch = Theme(name='Beach', slug='beach', description='Coastal bliss')
        self.th_her = Theme(name='Heritage', slug='heritage', description='Royal culture')
        self.th_nat = Theme(name='Nature', slug='nature', description='Scenic landscapes')
        db.session.add_all([self.th_adv, self.th_bch, self.th_her, self.th_nat])
        db.session.commit()

        # Package 1: Manali (Active, Delhi, 5 days, 10000/person, Themes: Adventure & Nature, Couple, Month 12)
        self.pkg1 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_manali.id,
            name='Manali Super Explorer',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('10000.00'),
            source_url='https://example.com/p1',
            is_active=True
        )
        self.pkg1.themes.extend([self.th_adv, self.th_nat])
        db.session.add(self.pkg1)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.pkg1.id, travel_type='Couple'),
            PackageAvailabilityMonth(package_id=self.pkg1.id, month=12)
        ])

        # Package 2: Manali (Active, Delhi, 5 days, 8000/person, Themes: Adventure & Nature, Solo, Month 12)
        self.pkg2 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_manali.id,
            name='Manali Budget Trek',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('8000.00'),
            source_url='https://example.com/p2',
            is_active=True
        )
        self.pkg2.themes.extend([self.th_adv, self.th_nat])
        db.session.add(self.pkg2)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.pkg2.id, travel_type='Solo'),
            PackageAvailabilityMonth(package_id=self.pkg2.id, month=12)
        ])

        # Package 3: Goa (Active, Delhi, 5 days, 12000/person, Themes: Beach & Nature, Solo, Month 12)
        self.pkg3 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_goa.id,
            name='Goa Sun & Sand',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('12000.00'),
            source_url='https://example.com/p3',
            is_active=True
        )
        self.pkg3.themes.extend([self.th_bch, self.th_nat])
        db.session.add(self.pkg3)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.pkg3.id, travel_type='Solo'),
            PackageAvailabilityMonth(package_id=self.pkg3.id, month=12)
        ])

        # Package 4: Jaipur (Active, Delhi, 5 days, 7000/person, Themes: Heritage & Nature, Family, Month 10)
        self.pkg4 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_jaipur.id,
            name='Royal Jaipur Heritage',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('7000.00'),
            source_url='https://example.com/p4',
            is_active=True
        )
        self.pkg4.themes.extend([self.th_her, self.th_nat])
        db.session.add(self.pkg4)
        db.session.flush()
        db.session.add_all([
            PackageTravelType(package_id=self.pkg4.id, travel_type='Family'),
            PackageAvailabilityMonth(package_id=self.pkg4.id, month=10)
        ])

        # Package 5: Inactive package (Should be ignored by discovery)
        self.pkg5 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_manali.id,
            name='Inactive Manali Winter',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('5000.00'),
            source_url='https://example.com/p5',
            is_active=False
        )
        self.pkg5.themes.append(self.th_adv)
        db.session.add(self.pkg5)

        # Package 6: Wrong duration (7 days)
        self.pkg6 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_manali.id,
            name='Manali Week Long',
            starting_city='Delhi',
            duration_days=7,
            duration_nights=6,
            price_per_person=Decimal('15000.00'),
            source_url='https://example.com/p6',
            is_active=True
        )
        self.pkg6.themes.append(self.th_adv)
        db.session.add(self.pkg6)

        # Package 7: Wrong starting city (Mumbai)
        self.pkg7 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_manali.id,
            name='Manali from Mumbai',
            starting_city='Mumbai',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('14000.00'),
            source_url='https://example.com/p7',
            is_active=True
        )
        self.pkg7.themes.append(self.th_adv)
        db.session.add(self.pkg7)

        # Package 8: Over budget (60000)
        self.pkg8 = Package(
            operator_id=self.operator.id,
            destination_id=self.dest_manali.id,
            name='Ultra Luxury Manali',
            starting_city='Delhi',
            duration_days=5,
            duration_nights=4,
            price_per_person=Decimal('60000.00'),
            source_url='https://example.com/p8',
            is_active=True
        )
        self.pkg8.themes.append(self.th_adv)
        db.session.add(self.pkg8)

        db.session.commit()

    # Base valid parameters helper
    def _base_params(self, **overrides):
        params = {
            'starting_city': 'Delhi',
            'budget': '30000',
            'travellers': '2',
            'duration_days': '5',
            'interest': 'Adventure',
            'travel_type': 'Couple',
            'month': '12',
            'limit': '10'
        }
        params.update(overrides)
        return '&'.join(f'{k}={v}' for k, v in params.items())

    # --- Test Cases ---

    def test_01_discovery_returns_matching_destinations(self):
        """1. Discovery returns matching destinations with correct structure."""
        url = f"/api/v1/discover/destinations?{self._base_params()}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertIsInstance(data['data'], list)
        self.assertGreater(len(data['data']), 0)
        first = data['data'][0]
        for field in [
            'destination_id', 'destination_name', 'country', 'region',
            'description', 'image_url', 'match_score', 'matching_package_count',
            'lowest_price_per_person', 'lowest_estimated_total_cost',
            'best_matching_package_id', 'best_matching_package_name'
        ]:
            self.assertIn(field, first)

    def test_02_starting_city_filtering(self):
        """2. Starting city filtering (case-insensitive hard match)."""
        # Starting city 'delhi' should match Delhi packages, but not Mumbai packages
        url = f"/api/v1/discover/destinations?{self._base_params(starting_city='delhi')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        dest_names = [d['destination_name'] for d in res.get_json()['data']]
        self.assertIn('Manali', dest_names)

        # Non-matching city
        url_none = f"/api/v1/discover/destinations?{self._base_params(starting_city='Kolkata')}"
        res_none = self.client.get(url_none)
        self.assertEqual(res_none.status_code, 200)
        self.assertEqual(res_none.get_json()['data'], [])

    def test_03_budget_and_travellers_filtering(self):
        """3. Budget + travellers hard filtering."""
        # Travellers = 2, Budget = 18000 -> Max per person = 9000
        # Pkg2 (8000) and Pkg4 (7000) pass. Pkg1 (10000) and Pkg3 (12000) exceed budget.
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Nature', budget='18000', travellers='2')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        dest_names = [d['destination_name'] for d in data]
        self.assertIn('Manali', dest_names)
        self.assertIn('Jaipur', dest_names)
        # Goa (Pkg3 = 12000) exceeds 9000 max per person
        self.assertNotIn('Goa', dest_names)

    def test_04_duration_filtering(self):
        """4. Duration is a soft preference in discovery: closest duration ranks highest."""
        # Duration 7 days with neutral travel type and month:
        # Pkg6 (7 days, diff 0 -> +15 dur) scores 85, beating Pkg1 (5 days, diff 2 -> +9 dur, score 79)
        url = f"/api/v1/discover/destinations?{self._base_params(duration_days='7', budget='50000', travel_type='Group', month='5')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        # Multiple destinations returned (alternatives not eliminated)
        self.assertGreaterEqual(len(data), 1)
        # Manali is #1 with exact duration match on Pkg6
        self.assertEqual(data[0]['destination_name'], 'Manali')
        self.assertEqual(data[0]['best_matching_package_name'], 'Manali Week Long')

    def test_05_interest_theme_matching(self):
        """5. Interest/theme is a hard filter: only destinations with matching active packages appear."""
        # Query for 'Beach' interest (Goa has beach; Manali and Jaipur do not)
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Beach', travel_type='Couple')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        dest_names = [d['destination_name'] for d in data]
        self.assertEqual(dest_names, ['Goa'])

        goa = data[0]
        # Goa package: starting city (+15), Beach (+35), Budget fit (+20), 5 days (+15), Month 12 (+5), Couple (0) -> score 90
        self.assertEqual(goa['match_score'], 90)
        self.assertNotIn('Manali', dest_names)
        self.assertNotIn('Jaipur', dest_names)

    def test_06_travel_type_matching(self):
        """6. Travel type matching awards +10 points as a soft scoring factor."""
        # Query with travel_type='Family' (Jaipur has Family)
        url = f"/api/v1/discover/destinations?{self._base_params(travel_type='Family', month='10', interest='Heritage')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        jaipur = next(d for d in data if d['destination_name'] == 'Jaipur')
        # Jaipur: starting city (+15), Heritage (+35), Budget fit (+20), Duration (+15), Family (+10), Month 10 (+5) -> score 100
        self.assertEqual(jaipur['match_score'], 100)

        # Query with non-matching travel_type='Solo': Jaipur is still returned, but without +10
        url_solo = f"/api/v1/discover/destinations?{self._base_params(travel_type='Solo', month='10', interest='Heritage')}"
        res_solo = self.client.get(url_solo)
        jaipur_solo = next(d for d in res_solo.get_json()['data'] if d['destination_name'] == 'Jaipur')
        # Score = 15 (city) + 35 (interest) + 20 (budget) + 15 (duration) + 0 (travel_type) + 5 (month) = 90
        self.assertEqual(jaipur_solo['match_score'], 90)

    def test_07_month_matching(self):
        """7. Month matching awards +5 points as a soft scoring factor."""
        # Query for Jaipur with month 10 (matching) vs month 5 (non-matching)
        url_match = f"/api/v1/discover/destinations?{self._base_params(month='10', interest='Heritage', travel_type='Group')}"
        res_match = self.client.get(url_match)
        self.assertEqual(res_match.status_code, 200)
        jaipur_match = next(d for d in res_match.get_json()['data'] if d['destination_name'] == 'Jaipur')
        # 15 (city) + 35 (interest) + 20 (budget) + 15 (duration) + 0 (travel_type) + 5 (month) = 90
        self.assertEqual(jaipur_match['match_score'], 90)

        # Non-matching month: Jaipur is still returned (soft factor), but score is 85 (0 for month)
        url_nomatch = f"/api/v1/discover/destinations?{self._base_params(month='5', interest='Heritage', travel_type='Group')}"
        res_nomatch = self.client.get(url_nomatch)
        self.assertEqual(res_nomatch.status_code, 200)
        jaipur_nomatch = next(d for d in res_nomatch.get_json()['data'] if d['destination_name'] == 'Jaipur')
        # 15 (city) + 35 (interest) + 20 (budget) + 15 (duration) + 0 (travel_type) + 0 (month) = 85
        self.assertEqual(jaipur_nomatch['match_score'], 85)

    def test_08_combined_matching_full_score(self):
        """8. Combined matching achieves perfect 100 score."""
        # Pkg1 has Delhi, Adventure, Couple, Month 12
        url = f"/api/v1/discover/destinations?{self._base_params(starting_city='Delhi', interest='Adventure', travel_type='Couple', month='12')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        manali = next(d for d in data if d['destination_name'] == 'Manali')
        self.assertEqual(manali['match_score'], 100)
        self.assertEqual(manali['best_matching_package_name'], 'Manali Super Explorer')

    def test_09_multiple_packages_same_destination_aggregate(self):
        """9. Multiple packages for the same destination aggregate correctly."""
        # In Delhi Adventure packages within budget 30000, Manali has Pkg1 (10000), Pkg2 (8000), Pkg6 (15000)
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Adventure', travellers='2')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        manali = next(d for d in data if d['destination_name'] == 'Manali')
        self.assertEqual(manali['matching_package_count'], 3)
        self.assertEqual(manali['lowest_price_per_person'], 8000.0)
        self.assertEqual(manali['lowest_estimated_total_cost'], 16000.0)

    def test_10_best_matching_package_selection(self):
        """10. Best matching package is selected correctly based on highest score."""
        # For Manali, Pkg1 scores 100 (Adventure+Couple+12), Pkg2 scores 90 (Adventure+Solo+12)
        url = f"/api/v1/discover/destinations?{self._base_params(travel_type='Couple', interest='Adventure', month='12')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        manali = next(d for d in data if d['destination_name'] == 'Manali')
        self.assertEqual(manali['best_matching_package_id'], self.pkg1.id)
        self.assertEqual(manali['best_matching_package_name'], 'Manali Super Explorer')

    def test_11_destination_ordering_ranking(self):
        """11. Destination ordering follows defined ranking."""
        # Query with interest='Nature', travel_type='Couple', month='12':
        # - Manali (Pkg1): Delhi (15) + Nature (35) + Budget (20) + 5 days (15) + Couple (10) + Month 12 (5) = 100
        # - Goa (Pkg3): Delhi (15) + Nature (35) + Budget (20) + 5 days (15) + Solo (!= Couple: 0) + Month 12 (5) = 90
        # - Jaipur (Pkg4): Delhi (15) + Nature (35) + Budget (20) + 5 days (15) + Family (!= Couple: 0) + Month 10 (!= 12: 0) = 85
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Nature', travel_type='Couple', month='12')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['destination_name'], 'Manali')
        self.assertEqual(data[0]['match_score'], 100)
        self.assertEqual(data[1]['destination_name'], 'Goa')
        self.assertEqual(data[1]['match_score'], 90)
        self.assertEqual(data[2]['destination_name'], 'Jaipur')
        self.assertEqual(data[2]['match_score'], 85)

    def test_12_limit_parameter(self):
        """12. Limit parameter restricts returned count."""
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Nature', limit='1')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 1)

    def test_13_invalid_missing_parameters_400(self):
        """13. Missing or invalid required parameters return 400 with standardized error structure."""
        # Missing starting_city
        res1 = self.client.get('/api/v1/discover/destinations?budget=30000&travellers=2&duration_days=5&interest=Adventure&travel_type=Couple&month=12')
        self.assertEqual(res1.status_code, 400)
        json1 = res1.get_json()
        self.assertFalse(json1['success'])
        self.assertIsInstance(json1['error'], dict)
        self.assertIn("starting_city", json1['error']['message'])

        # Negative budget
        url_neg_budget = f"/api/v1/discover/destinations?{self._base_params(budget='-100')}"
        res2 = self.client.get(url_neg_budget)
        self.assertEqual(res2.status_code, 400)
        json2 = res2.get_json()
        self.assertFalse(json2['success'])
        self.assertIsInstance(json2['error'], dict)
        self.assertIn("budget", json2['error']['message'])

        # Zero travellers
        url_zero_travellers = f"/api/v1/discover/destinations?{self._base_params(travellers='0')}"
        res3 = self.client.get(url_zero_travellers)
        self.assertEqual(res3.status_code, 400)
        json3 = res3.get_json()
        self.assertFalse(json3['success'])
        self.assertIsInstance(json3['error'], dict)
        self.assertIn("travellers", json3['error']['message'])

        # Zero duration_days
        url_zero_duration = f"/api/v1/discover/destinations?{self._base_params(duration_days='0')}"
        res4 = self.client.get(url_zero_duration)
        self.assertEqual(res4.status_code, 400)
        json4 = res4.get_json()
        self.assertFalse(json4['success'])
        self.assertIsInstance(json4['error'], dict)
        self.assertIn("duration_days", json4['error']['message'])

        # Invalid limit
        url_invalid_limit = f"/api/v1/discover/destinations?{self._base_params(limit='25')}"
        res5 = self.client.get(url_invalid_limit)
        self.assertEqual(res5.status_code, 400)
        json5 = res5.get_json()
        self.assertFalse(json5['success'])
        self.assertIsInstance(json5['error'], dict)
        self.assertIn("limit", json5['error']['message'])

    def test_14_invalid_month_400(self):
        """14. Month outside 1–12 returns 400 with standardized error structure."""
        for invalid_m in ['0', '13', '-1', 'spring']:
            url = f"/api/v1/discover/destinations?{self._base_params(month=invalid_m)}"
            res = self.client.get(url)
            self.assertEqual(res.status_code, 400)
            json_data = res.get_json()
            self.assertFalse(json_data['success'])
            self.assertIsInstance(json_data['error'], dict)
            self.assertIn("month", json_data['error']['message'])

    def test_15_invalid_travel_type_400(self):
        """15. Invalid travel type returns 400 with standardized error structure."""
        url = f"/api/v1/discover/destinations?{self._base_params(travel_type='Luxury')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 400)
        json_data = res.get_json()
        self.assertFalse(json_data['success'])
        self.assertIsInstance(json_data['error'], dict)
        self.assertIn("travel_type", json_data['error']['message'])

    def test_16_no_matching_destinations_empty_array(self):
        """16. No matching destinations returns empty data array with message."""
        # Unrealistic low budget of 100 for 5-day trip
        url = f"/api/v1/discover/destinations?{self._base_params(budget='100')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data'], [])
        self.assertEqual(data['message'], "No destinations currently have packages matching your selected travel interest and requirements.")

    def test_17_inactive_packages_ignored(self):
        """17. Inactive packages are completely ignored."""
        # Pkg5 has price 5000 and duration 5 for Manali, but is_active=False
        url = f"/api/v1/discover/destinations?{self._base_params()}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        manali = next(d for d in data if d['destination_name'] == 'Manali')
        # Lowest price should be 8000 (from Pkg2), not 5000 (Pkg5 is inactive)
        self.assertEqual(manali['lowest_price_per_person'], 8000.0)

    def test_18_no_duplicate_destination_results(self):
        """18. Ensure no duplicate destination results in output."""
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Nature')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        dest_ids = [d['destination_id'] for d in res.get_json()['data']]
        self.assertEqual(len(dest_ids), len(set(dest_ids)))

    def test_19_destination_without_matching_interest_package_excluded(self):
        """19. A destination without any matching-interest package is excluded from discovery (hard filter)."""
        url = f"/api/v1/discover/destinations?{self._base_params(interest='NonExistentInterest')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data'], [])
        self.assertEqual(data['message'], "No destinations currently have packages matching your selected travel interest and requirements.")

    def test_20_travel_type_and_month_are_soft_factors(self):
        """20. When travel type and month do not match, matching packages are still returned (score 85)."""
        # User selects Group and Month 5 (none of the Jaipur packages have Group or Month 5)
        # Packages with Delhi (15) + Heritage (35) + budget (20) + 5 days (15) + Group (0) + Month 5 (0) = 85
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Heritage', travel_type='Group', month='5')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertGreaterEqual(len(data), 1)
        jaipur = next(d for d in data if d['destination_name'] == 'Jaipur')
        self.assertEqual(jaipur['match_score'], 85)

    def test_21_discovery_fallback_up_to_20_percent_over_budget(self):
        """21. When no package is within budget, packages up to 20% over budget appear as fallback."""
        # For Delhi with 2 travellers and Heritage interest: lowest package is Jaipur (7000/person = 14000 total).
        # Budget = 12500:
        # 12500 * 1.20 = 15000. Jaipur (14000) is 12% over budget (<= 20% over budget).
        # Fallback activates!
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Heritage', budget='12500', travellers='2')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertGreaterEqual(len(data), 1)
        jaipur = next(d for d in data if d['destination_name'] == 'Jaipur')
        self.assertEqual(jaipur['lowest_estimated_total_cost'], 14000.0)

    def test_22_discovery_more_than_20_percent_over_budget_excluded(self):
        """22. When packages exceed 20% over budget, they do not appear as fallback."""
        # Lowest in Delhi is 14000 for 2 travellers.
        # Budget = 10000: 20% above is 12000. 14000 > 12000.
        url = f"/api/v1/discover/destinations?{self._base_params(interest='Heritage', budget='10000', travellers='2')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['data'], [])
        self.assertEqual(data['message'], "No destinations currently have packages matching your selected travel interest and requirements.")

    def test_23_discovery_starting_city_remains_hard(self):
        """23. Starting city remains a hard constraint in destination discovery."""
        # Query with Mumbai: only Pkg7 (Manali from Mumbai) should be eligible
        url = f"/api/v1/discover/destinations?{self._base_params(starting_city='Mumbai', budget='50000')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['destination_name'], 'Manali')
        self.assertEqual(data[0]['best_matching_package_name'], 'Manali from Mumbai')

    def test_24_discovery_inactive_packages_excluded(self):
        """24. Inactive packages are excluded from destination discovery."""
        # Pkg5 is inactive in Manali. If all active packages are deleted/unmatched, it should not appear.
        url = f"/api/v1/discover/destinations?{self._base_params()}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        for dest in data:
            self.assertNotEqual(dest['best_matching_package_id'], self.pkg5.id)

    def test_25_discovery_does_not_become_empty_on_duration_month_travel_type_diff(self):
        """25. Discovery does not become empty simply because duration, month, or travel type differ."""
        # User selects duration 10, month 3, travel type Group
        url = f"/api/v1/discover/destinations?{self._base_params(duration_days='10', month='3', travel_type='Group')}"
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        # Still returns destinations!
        self.assertGreater(len(data), 0)


if __name__ == '__main__':
    unittest.main()
