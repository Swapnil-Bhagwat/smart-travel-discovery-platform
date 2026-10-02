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
from app.services.recommendation_service import (
    PROHIBITED_UNSUPPORTED_CLAIMS,
    score_and_explain_package,
    get_package_recommendations,
    generate_destination_reasons,
)


class TestRecommendationConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestRecommendations(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestRecommendationConfig)
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
        self.dest_goa = Destination(name='Goa', country='India', region='Goa')
        self.dest_manali = Destination(name='Manali', country='India', region='Himachal Pradesh')
        self.dest_jaipur = Destination(name='Jaipur', country='India', region='Rajasthan')
        db.session.add_all([self.dest_goa, self.dest_manali, self.dest_jaipur])
        db.session.commit()

        # Seed Themes
        self.th_beach = Theme(name='Beach', slug='beach', description='Beaches and coastlines')
        self.th_adv = Theme(name='Adventure', slug='adventure', description='Trekking and outdoor sports')
        self.th_cul = Theme(name='Culture', slug='culture', description='Culture and heritage')
        db.session.add_all([self.th_beach, self.th_adv, self.th_cul])
        db.session.commit()

        # Seed Packages:
        self.p1 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Beach Bliss', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('20000.00'), source_url='https://example.com/p1', is_active=True
        )
        self.p2 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Coastal Gathering', starting_city='Delhi', duration_days=6, duration_nights=5,
            price_per_person=Decimal('15000.00'), source_url='https://example.com/p2', is_active=True
        )
        self.p3 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Premium Sands', starting_city='Delhi', duration_days=7, duration_nights=6,
            price_per_person=Decimal('26000.00'), source_url='https://example.com/p3', is_active=True
        )
        self.p4 = Package(
            operator_id=self.op1.id, destination_id=self.dest_manali.id,
            name='Manali Alpine Trek', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('10000.00'), source_url='https://example.com/p4', is_active=True
        )
        self.p5 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Waves Ex-Mumbai', starting_city='Mumbai', duration_days=5, duration_nights=4,
            price_per_person=Decimal('20000.00'), source_url='https://example.com/p5', is_active=True
        )
        self.p6 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Retired Package', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('18000.00'), source_url='https://example.com/p6', is_active=False
        )
        self.p7 = Package(
            operator_id=self.op2.id, destination_id=self.dest_goa.id,
            name='Goa Ultra Luxury Beach Villa', starting_city='Delhi', duration_days=5, duration_nights=4,
            price_per_person=Decimal('40000.00'), source_url='https://example.com/p7', is_active=True
        )
        db.session.add_all([self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7])
        db.session.flush()

        self.p1.themes.append(self.th_beach)
        self.p1.travel_types.append(PackageTravelType(travel_type='Couple'))
        self.p1.availability_months.append(PackageAvailabilityMonth(month=12))

        self.p2.themes.append(self.th_beach)
        self.p2.travel_types.append(PackageTravelType(travel_type='Group'))
        self.p2.availability_months.append(PackageAvailabilityMonth(month=11))

        self.p3.themes.append(self.th_beach)
        self.p3.travel_types.append(PackageTravelType(travel_type='Couple'))
        self.p3.availability_months.append(PackageAvailabilityMonth(month=12))

        self.p4.themes.append(self.th_adv)
        self.p4.travel_types.append(PackageTravelType(travel_type='Couple'))
        self.p4.availability_months.append(PackageAvailabilityMonth(month=12))

        self.p5.themes.append(self.th_beach)
        self.p5.travel_types.append(PackageTravelType(travel_type='Couple'))
        self.p5.availability_months.append(PackageAvailabilityMonth(month=12))

        self.p6.themes.append(self.th_beach)
        self.p6.travel_types.append(PackageTravelType(travel_type='Couple'))
        self.p6.availability_months.append(PackageAvailabilityMonth(month=12))

        self.p7.themes.append(self.th_beach)
        self.p7.travel_types.append(PackageTravelType(travel_type='Couple'))
        self.p7.availability_months.append(PackageAvailabilityMonth(month=12))

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # 1. Exact match receives high score (100)
    def test_01_exact_match_receives_100(self):
        result = score_and_explain_package(
            pkg=self.p1,
            starting_city='Delhi',
            budget=Decimal('50000'),
            travellers=2,
            duration_days=5,
            interest='Beach',
            travel_type='Couple',
            month=12
        )
        self.assertIsNotNone(result)
        self.assertEqual(result['match_score'], 100)
        self.assertEqual(result['budget_status'], 'within_budget')
        self.assertEqual(result['budget_difference'], 0.0)

    # 2. Interest remains a hard filter
    def test_02_interest_remains_hard_filter(self):
        # Manali package has Adventure, not Beach
        result = score_and_explain_package(
            pkg=self.p4,
            starting_city='Delhi',
            budget=Decimal('50000'),
            travellers=2,
            duration_days=5,
            interest='Beach',
            travel_type='Couple',
            month=12
        )
        self.assertIsNone(result)

    # 3. Beach never returns a package without Beach theme
    def test_03_beach_never_returns_non_beach_package(self):
        res = self.client.get('/api/v1/recommendations/packages', query_string={
            'starting_city': 'Delhi',
            'budget': '50000',
            'travellers': '2',
            'duration_days': '5',
            'interest': 'Beach',
            'travel_type': 'Couple',
            'month': '12'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        # Every package must have Beach theme
        for p in data:
            theme_names = [t['name'].lower() for t in p['themes']]
            theme_slugs = [t['slug'].lower() for t in p['themes']]
            self.assertTrue('beach' in theme_names or 'beach' in theme_slugs)
            self.assertNotEqual(p['name'], 'Manali Alpine Trek')

    # 4. Budget score works correctly (+25 for within, +18 for 1-10% over, +10 for 10.01-20% over)
    def test_04_budget_score_graduations(self):
        # Within budget: p1 cost 40000 <= 50000 -> 25 pts
        res_within = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        self.assertEqual(res_within['match_score'], 100)

        # 4% over budget: p3 cost 52000 vs 50000 (18 pts) + 5 days preferred vs 7 days duration (diff 2 -> 12 pts)
        # city 5 + interest 25 + budget 18 + duration 12 + travel 15 + month 10 = 85
        res_4_over = score_and_explain_package(
            pkg=self.p3, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        self.assertEqual(res_4_over['match_score'], 85)

        # Also test 4% over budget with exact duration 7 days:
        # city 5 + interest 25 + budget 18 + duration 20 + travel 15 + month 10 = 93
        res_4_over_exact_dur = score_and_explain_package(
            pkg=self.p3, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=7, interest='Beach', travel_type='Couple', month=12
        )
        self.assertEqual(res_4_over_exact_dur['match_score'], 93)

        # 15% over budget: cost 57500 vs 50000 -> +10 pts
        # Let's test with a simulated package dict
        pkg_mock = {
            'is_active': True,
            'starting_city': 'Delhi',
            'price_per_person': 28750,  # 28750 * 2 = 57500 (15% over 50000)
            'duration_days': 5,
            'themes': [{'name': 'Beach', 'slug': 'beach'}],
            'travel_types': [{'travel_type': 'Couple'}],
            'availability_months': [{'month': 12}]
        }
        res_15_over = score_and_explain_package(
            pkg=pkg_mock, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        # city 5 + interest 25 + budget 10 + duration 20 + travel 15 + month 10 = 85
        self.assertEqual(res_15_over['match_score'], 85)
        self.assertEqual(res_15_over['budget_status'], 'over_budget')

    # 5. Within-budget ranks above over-budget
    def test_05_within_budget_ranks_above_over_budget(self):
        # Create a package that has same score but is over budget
        recs = get_package_recommendations(
            starting_city='Delhi', budget=50000, travellers=2, duration_days=5,
            interest='Beach', travel_type='Couple', month=12
        )
        self.assertTrue(len(recs) >= 2)
        # Check that within_budget items appear before over_budget items
        statuses = [r['budget_status'] for r in recs]
        if 'over_budget' in statuses and 'within_budget' in statuses:
            first_over = statuses.index('over_budget')
            last_within = len(statuses) - 1 - statuses[::-1].index('within_budget')
            self.assertTrue(last_within < first_over)

    # 6. 1-day duration difference receives expected score (+16 vs +20)
    def test_06_1_day_duration_difference(self):
        # p1 has 5 days (exact match = +20) -> score 100
        # If preferred duration is 4, diff is 1 -> +16 pts -> score 96
        res = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=4, interest='Beach', travel_type='Couple', month=12
        )
        self.assertEqual(res['match_score'], 96)
        self.assertIn("Only 1 day longer than your preferred duration", res['match_reasons'])
        self.assertIn("Package is 5 days instead of your preferred 4 days", res['mismatches'])

    # 7. 2-day duration difference receives expected score (+12 vs +20)
    def test_07_2_day_duration_difference(self):
        # If preferred duration is 3, diff is 2 -> +12 pts -> score 92
        res = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=3, interest='Beach', travel_type='Couple', month=12
        )
        self.assertEqual(res['match_score'], 92)
        self.assertIn("Package is 5 days instead of your preferred 3 days", res['mismatches'])

    # 8. Travel type match adds points (+15 vs 0)
    def test_08_travel_type_match_adds_points(self):
        # p1 has Couple
        res_match = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        res_no_match = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Solo', month=12
        )
        self.assertEqual(res_match['match_score'] - res_no_match['match_score'], 15)
        self.assertIn("Suitable for Couple travel", res_match['match_reasons'])
        self.assertIn("Designed for Couple travel", res_no_match['mismatches'])

    # 9. Month match adds points (+10 vs 0)
    def test_09_month_match_adds_points(self):
        # p1 is available in Month 12
        res_match = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        res_no_match = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=6
        )
        self.assertEqual(res_match['match_score'] - res_no_match['match_score'], 10)
        self.assertIn("Available in December", res_match['match_reasons'])
        self.assertIn("Not listed for June", res_no_match['mismatches'])

    # 10. Starting city remains hard
    def test_10_starting_city_remains_hard(self):
        # p5 departs from Mumbai
        res = score_and_explain_package(
            pkg=self.p5, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        self.assertIsNone(res)

    # 11. Explicit destination remains hard
    def test_11_explicit_destination_remains_hard(self):
        # p1 is in Goa; filter by Jaipur destination_id
        res = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12,
            destination_id=self.dest_jaipur.id
        )
        self.assertIsNone(res)

    # 12. Inactive packages excluded
    def test_12_inactive_packages_excluded(self):
        # p6 has is_active=False
        res = score_and_explain_package(
            pkg=self.p6, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        self.assertIsNone(res)

    # 13. >20% over-budget packages excluded
    def test_13_over_20_percent_excluded(self):
        # p7 cost 80000 vs 50000 budget (60% over budget)
        res = score_and_explain_package(
            pkg=self.p7, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        self.assertIsNone(res)

    # 14. Match reasons are generated correctly
    def test_14_match_reasons_generated_correctly(self):
        res = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        reasons = res['match_reasons']
        self.assertIn("Matches your Beach interest", reasons)
        self.assertIn("Fits your ₹50,000 total budget", reasons)
        self.assertIn("Matches your 5-day duration preference", reasons)
        self.assertIn("Suitable for Couple travel", reasons)
        self.assertIn("Available in December", reasons)
        self.assertIn("Departs from your starting city (Delhi)", reasons)

    # 15. Mismatches are generated correctly
    def test_15_mismatches_generated_correctly(self):
        # p2: 6 days (preferred 5), Group (preferred Couple), month 11 (preferred 12)
        res = score_and_explain_package(
            pkg=self.p2, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        mismatches = res['mismatches']
        self.assertIn("Package is 6 days instead of your preferred 5 days", mismatches)
        self.assertIn("Designed for Group travel", mismatches)
        self.assertIn("Not listed for December", mismatches)

    # 16. No unsupported recommendation claims are generated
    def test_16_no_unsupported_recommendation_claims(self):
        res = score_and_explain_package(
            pkg=self.p1, starting_city='Delhi', budget=50000, travellers=2,
            duration_days=5, interest='Beach', travel_type='Couple', month=12
        )
        all_text = " ".join(res['match_reasons'] + res['mismatches']).lower()
        for claim in PROHIBITED_UNSUPPORTED_CLAIMS:
            self.assertNotIn(claim, all_text)

        # Destination reasons also checked
        d_reasons, d_mismatches = generate_destination_reasons(
            destination_name='Goa', matching_packages=[self.p1, self.p2],
            budget=50000, travellers=2, duration_days=5, interest='Beach',
            travel_type='Couple', month=12
        )
        all_d_text = " ".join(d_reasons + d_mismatches).lower()
        for claim in PROHIBITED_UNSUPPORTED_CLAIMS:
            self.assertNotIn(claim, all_d_text)

    # 17. Recommendation ordering is deterministic
    def test_17_recommendation_ordering_deterministic(self):
        res1 = get_package_recommendations(
            starting_city='Delhi', budget=50000, travellers=2, duration_days=5,
            interest='Beach', travel_type='Couple', month=12
        )
        res2 = get_package_recommendations(
            starting_city='Delhi', budget=50000, travellers=2, duration_days=5,
            interest='Beach', travel_type='Couple', month=12
        )
        ids1 = [p['id'] for p in res1]
        ids2 = [p['id'] for p in res2]
        self.assertEqual(ids1, ids2)

    # 18. Limit works
    def test_18_limit_works(self):
        res = self.client.get('/api/v1/recommendations/packages', query_string={
            'starting_city': 'Delhi',
            'budget': '50000',
            'travellers': '2',
            'duration_days': '5',
            'interest': 'Beach',
            'travel_type': 'Couple',
            'month': '12',
            'limit': '1'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertLessEqual(len(data['data']), 1)
        self.assertEqual(data['pagination']['limit'], 1)

    # 19. Invalid input returns 400
    def test_19_invalid_input_returns_400(self):
        base_params = {
            'starting_city': 'Delhi',
            'budget': '50000',
            'travellers': '2',
            'duration_days': '5',
            'interest': 'Beach',
            'travel_type': 'Couple',
            'month': '12'
        }

        # Missing starting_city
        p = dict(base_params)
        del p['starting_city']
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

        # Negative budget
        p = dict(base_params, budget='-100')
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

        # Invalid travellers
        p = dict(base_params, travellers='0')
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

        # Invalid duration
        p = dict(base_params, duration_days='-5')
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

        # Missing interest
        p = dict(base_params, interest='')
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

        # Invalid travel_type
        p = dict(base_params, travel_type='Backpacker')
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

        # Invalid month
        p = dict(base_params, month='13')
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

        # Invalid limit
        p = dict(base_params, limit='25')
        self.assertEqual(self.client.get('/api/v1/recommendations/packages', query_string=p).status_code, 400)

    # Destination explainability test
    def test_20_destination_discovery_has_reasons_and_mismatches(self):
        res = self.client.get('/api/v1/discover/destinations', query_string={
            'starting_city': 'Delhi',
            'budget': '50000',
            'travellers': '2',
            'duration_days': '5',
            'interest': 'Beach',
            'travel_type': 'Couple',
            'month': '12'
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()['data']
        self.assertTrue(len(data) >= 1)
        dest = data[0]
        self.assertIn('match_reasons', dest)
        self.assertIn('mismatches', dest)
        self.assertTrue(len(dest['match_reasons']) > 0)
        self.assertTrue(any('Beach' in r for r in dest['match_reasons']))

    # 21. Exactly 1 matching package singular explanations
    def test_21_destination_reasons_exactly_1_matching_package(self):
        # 1 package with 6 days (1 day diff from 5), 20000/person (40000 <= 50000 budget), Couple, Month 12
        pkg_single = {
            'price_per_person': Decimal('20000.00'),
            'duration_days': 6,
            'travel_types': [{'travel_type': 'Couple'}],
            'availability_months': [{'month': 12}]
        }
        reasons, mismatches = generate_destination_reasons(
            destination_name='Goa',
            matching_packages=[pkg_single],
            budget=Decimal('50000'),
            travellers=2,
            duration_days=5,
            interest='Adventure',
            travel_type='Couple',
            month=12
        )
        # Check singular wording
        self.assertIn("1 Adventure package available", reasons)
        self.assertIn("1 package is within your budget", reasons)
        self.assertIn("1 package is close to your 5-day preference", reasons)
        self.assertIn("Available package includes Couple travel", reasons)
        self.assertIn("Available in December", reasons)
        self.assertNotIn("Several packages are close to your 5-day preference", reasons)

    # 22. Exactly 2 matching packages plural explanations
    def test_22_destination_reasons_exactly_2_matching_packages(self):
        # 2 packages, both with 6 days (1 day diff from 5), within budget, Couple, Month 12
        pkg_a = {
            'price_per_person': Decimal('20000.00'),
            'duration_days': 6,
            'travel_types': [{'travel_type': 'Couple'}],
            'availability_months': [{'month': 12}]
        }
        pkg_b = {
            'price_per_person': Decimal('22000.00'),
            'duration_days': 6,
            'travel_types': [{'travel_type': 'Couple'}],
            'availability_months': [{'month': 12}]
        }
        reasons, mismatches = generate_destination_reasons(
            destination_name='Goa',
            matching_packages=[pkg_a, pkg_b],
            budget=Decimal('50000'),
            travellers=2,
            duration_days=5,
            interest='Adventure',
            travel_type='Couple',
            month=12
        )
        self.assertIn("2 Adventure packages available", reasons)
        self.assertIn("2 packages are within your budget", reasons)
        self.assertIn("Several packages are close to your 5-day preference", reasons)
        self.assertIn("Available packages include Couple travel", reasons)
        self.assertIn("Available in December", reasons)

    # 23. 0 matching packages: never generate a package-count reason
    def test_23_destination_reasons_0_matching_packages(self):
        reasons, mismatches = generate_destination_reasons(
            destination_name='Goa',
            matching_packages=[],
            budget=Decimal('50000'),
            travellers=2,
            duration_days=5,
            interest='Adventure',
            travel_type='Couple',
            month=12
        )
        self.assertEqual(len(reasons), 0)
        for r in reasons:
            self.assertNotIn("package", r.lower())

    # 24. Month mismatch wording
    def test_24_destination_reasons_month_mismatch_wording(self):
        # Packages operate in December, user requested September (month 9)
        pkg = {
            'price_per_person': Decimal('20000.00'),
            'duration_days': 5,
            'travel_types': [{'travel_type': 'Couple'}],
            'availability_months': [{'month': 12}]
        }
        reasons, mismatches = generate_destination_reasons(
            destination_name='Goa',
            matching_packages=[pkg],
            budget=Decimal('50000'),
            travellers=2,
            duration_days=5,
            interest='Adventure',
            travel_type='Couple',
            month=9
        )
        self.assertIn("No matching package is listed for September", mismatches)
        self.assertNotIn("Not listed for September", mismatches)

    # 25. Singular/plural correctness with mixed package attributes
    def test_25_destination_reasons_singular_plural_correctness(self):
        # Package 1: within budget (cost 40000 <= 50000)
        # Package 2: over budget (cost 56000 > 50000)
        pkg_within = {
            'price_per_person': Decimal('20000.00'),
            'duration_days': 5,
            'travel_types': [{'travel_type': 'Couple'}],
            'availability_months': [{'month': 12}]
        }
        pkg_over = {
            'price_per_person': Decimal('28000.00'),
            'duration_days': 5,
            'travel_types': [{'travel_type': 'Couple'}],
            'availability_months': [{'month': 12}]
        }
        reasons, mismatches = generate_destination_reasons(
            destination_name='Goa',
            matching_packages=[pkg_within, pkg_over],
            budget=Decimal('50000'),
            travellers=2,
            duration_days=5,
            interest='Beach',
            travel_type='Couple',
            month=12
        )
        # Exactly 1 package is within budget even though 2 packages are available
        self.assertIn("2 Beach packages available", reasons)
        self.assertIn("1 package is within your budget", reasons)
        self.assertNotIn("2 packages are within your budget", reasons)


if __name__ == '__main__':
    unittest.main()
