import unittest
from decimal import Decimal
from app import create_app
from app.config import Config
from app.extensions import db
from app.models.destination import Destination
from app.models.operator import Operator
from app.models.theme import Theme


class TestConfig(Config):
    """Isolated in-memory configuration for testing without touching MySQL."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestCoreAPIs(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # --- Destinations API Tests ---

    def test_get_destinations_empty(self):
        """Test GET /api/v1/destinations returns empty list when no records exist."""
        response = self.client.get('/api/v1/destinations')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertTrue(json_data['success'])
        self.assertEqual(json_data['data'], [])
        self.assertEqual(json_data['pagination']['total'], 0)
        self.assertEqual(json_data['pagination']['page'], 1)

    def test_get_destinations_list_and_search(self):
        """Test GET /api/v1/destinations with data and search/filter query parameters."""
        d1 = Destination(name='Bali', country='Indonesia', region='Southeast Asia', description='Island of Gods')
        d2 = Destination(name='Paris', country='France', region='Western Europe', description='City of Lights')
        d3 = Destination(name='Goa', country='India', region='Western India', description='Sun, sand and sea')
        db.session.add_all([d1, d2, d3])
        db.session.commit()

        # All destinations
        res = self.client.get('/api/v1/destinations')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 3)
        self.assertEqual(data['pagination']['total'], 3)

        # Search by destination name
        res_search = self.client.get('/api/v1/destinations?search=bal')
        self.assertEqual(res_search.status_code, 200)
        data_search = res_search.get_json()
        self.assertEqual(len(data_search['data']), 1)
        self.assertEqual(data_search['data'][0]['name'], 'Bali')

        # Filter by country
        res_country = self.client.get('/api/v1/destinations?country=France')
        self.assertEqual(res_country.status_code, 200)
        data_country = res_country.get_json()
        self.assertEqual(len(data_country['data']), 1)
        self.assertEqual(data_country['data'][0]['country'], 'France')

    def test_get_destinations_pagination(self):
        """Test pagination query parameters on /api/v1/destinations."""
        for i in range(1, 6):
            db.session.add(Destination(name=f'City {i}', country='Country X'))
        db.session.commit()

        res = self.client.get('/api/v1/destinations?page=2&per_page=2')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data['data']), 2)
        self.assertEqual(data['pagination']['page'], 2)
        self.assertEqual(data['pagination']['per_page'], 2)
        self.assertEqual(data['pagination']['total'], 5)
        self.assertEqual(data['pagination']['pages'], 3)

    def test_get_destinations_invalid_pagination(self):
        """Test invalid pagination parameters return 400 error."""
        res = self.client.get('/api/v1/destinations?page=-1')
        self.assertEqual(res.status_code, 400)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertIn('error', data)

        res2 = self.client.get('/api/v1/destinations?page=abc')
        self.assertEqual(res2.status_code, 400)
        self.assertFalse(res2.get_json()['success'])

    def test_get_destination_by_id(self):
        """Test GET /api/v1/destinations/<id> returns one destination."""
        dest = Destination(name='Kyoto', country='Japan', region='Kansai', description='Ancient temples')
        db.session.add(dest)
        db.session.commit()

        res = self.client.get(f'/api/v1/destinations/{dest.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Kyoto')
        self.assertEqual(data['data']['country'], 'Japan')

    def test_get_destination_not_found_404(self):
        """Test GET /api/v1/destinations/<id> returns 404 if not found."""
        res = self.client.get('/api/v1/destinations/999')
        self.assertEqual(res.status_code, 404)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error']['message'], 'Destination with id 999 not found')

    # --- Operators API Tests ---

    def test_get_operators_empty(self):
        """Test GET /api/v1/operators returns empty list when no records exist."""
        res = self.client.get('/api/v1/operators')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data'], [])
        self.assertEqual(data['pagination']['total'], 0)

    def test_get_operators_list_and_search(self):
        """Test GET /api/v1/operators with data and search."""
        op1 = Operator(name='Wanderlust Travels', website_url='https://wanderlust.com', rating=Decimal('4.8'))
        op2 = Operator(name='Summit Adventures', website_url='https://summit.com', rating=Decimal('4.5'))
        db.session.add_all([op1, op2])
        db.session.commit()

        res = self.client.get('/api/v1/operators')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data['data']), 2)

        # Search by operator name
        res_search = self.client.get('/api/v1/operators?search=summit')
        self.assertEqual(res_search.status_code, 200)
        data_search = res_search.get_json()
        self.assertEqual(len(data_search['data']), 1)
        self.assertEqual(data_search['data'][0]['name'], 'Summit Adventures')

    def test_get_operators_pagination(self):
        """Test pagination query parameters on /api/v1/operators."""
        for i in range(1, 4):
            db.session.add(Operator(name=f'Operator {i}'))
        db.session.commit()

        res = self.client.get('/api/v1/operators?page=1&per_page=2')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(len(data['data']), 2)
        self.assertEqual(data['pagination']['total'], 3)
        self.assertEqual(data['pagination']['pages'], 2)

    def test_get_operator_by_id(self):
        """Test GET /api/v1/operators/<id> returns one operator."""
        op = Operator(name='Horizon Holidays', contact_email='info@horizon.com', rating=Decimal('4.7'))
        db.session.add(op)
        db.session.commit()

        res = self.client.get(f'/api/v1/operators/{op.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Horizon Holidays')
        self.assertEqual(data['data']['contact_email'], 'info@horizon.com')
        self.assertEqual(data['data']['rating'], 4.7)

    def test_get_operator_not_found_404(self):
        """Test GET /api/v1/operators/<id> returns 404 if not found."""
        res = self.client.get('/api/v1/operators/999')
        self.assertEqual(res.status_code, 404)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error']['message'], 'Operator with id 999 not found')

    # --- Themes API Tests ---

    def test_get_themes_empty(self):
        """Test GET /api/v1/themes returns empty list when no records exist."""
        res = self.client.get('/api/v1/themes')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data'], [])

    def test_get_themes_list(self):
        """Test GET /api/v1/themes returns all available themes."""
        t1 = Theme(name='Beach & Islands', slug='beach-islands', description='Coastal escapes')
        t2 = Theme(name='Adventure & Trekking', slug='adventure-trekking', description='High adrenaline trips')
        db.session.add_all([t1, t2])
        db.session.commit()

        res = self.client.get('/api/v1/themes')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 2)
        # Verify ordering by name
        self.assertEqual(data['data'][0]['name'], 'Adventure & Trekking')
        self.assertEqual(data['data'][1]['name'], 'Beach & Islands')

    def test_get_theme_by_id(self):
        """Test GET /api/v1/themes/<id> returns one theme."""
        t = Theme(name='Cultural Heritage', slug='cultural-heritage', description='Historical exploration')
        db.session.add(t)
        db.session.commit()

        res = self.client.get(f'/api/v1/themes/{t.id}')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'Cultural Heritage')
        self.assertEqual(data['data']['slug'], 'cultural-heritage')

    def test_get_theme_not_found_404(self):
        """Test GET /api/v1/themes/<id> returns 404 if not found."""
        res = self.client.get('/api/v1/themes/999')
        self.assertEqual(res.status_code, 404)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error']['message'], 'Theme with id 999 not found')

    def test_unregistered_route_404(self):
        """Test non-existent route returns 404 with standard error JSON."""
        res = self.client.get('/api/v1/nonexistent')
        self.assertEqual(res.status_code, 404)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(data['error']['message'], 'Resource not found')


class TestDatabaseSSLConfig(unittest.TestCase):
    """Verify TiDB Cloud and MySQL SSL/TLS configuration logic."""

    def setUp(self):
        import os
        self._orig_ssl = os.environ.get('MYSQL_SSL')
        self._orig_ca = os.environ.get('MYSQL_SSL_CA')

    def tearDown(self):
        import os
        import importlib
        if self._orig_ssl is not None:
            os.environ['MYSQL_SSL'] = self._orig_ssl
        else:
            os.environ.pop('MYSQL_SSL', None)

        if self._orig_ca is not None:
            os.environ['MYSQL_SSL_CA'] = self._orig_ca
        else:
            os.environ.pop('MYSQL_SSL_CA', None)

        import app.config
        importlib.reload(app.config)

    def test_default_ssl_disabled(self):
        """When MYSQL_SSL is unset or false, SSL connect_args are not included."""
        import os
        import importlib
        os.environ['MYSQL_SSL'] = 'false'
        os.environ.pop('MYSQL_SSL_CA', None)
        import app.config
        importlib.reload(app.config)

        self.assertFalse(app.config.Config.MYSQL_SSL)
        self.assertNotIn('connect_args', app.config.Config.SQLALCHEMY_ENGINE_OPTIONS)

    def test_tidb_cloud_ssl_enabled_default_ca(self):
        """When MYSQL_SSL=true without MYSQL_SSL_CA, default Linux CA bundle path is used."""
        import os
        import importlib
        os.environ['MYSQL_SSL'] = 'true'
        os.environ.pop('MYSQL_SSL_CA', None)
        import app.config
        importlib.reload(app.config)

        self.assertTrue(app.config.Config.MYSQL_SSL)
        opts = app.config.Config.SQLALCHEMY_ENGINE_OPTIONS
        self.assertIn('connect_args', opts)
        self.assertTrue(opts['connect_args']['ssl_verify_cert'])
        self.assertTrue(opts['connect_args']['ssl_verify_identity'])
        self.assertEqual(opts['connect_args']['ssl_ca'], '/etc/ssl/certs/ca-certificates.crt')

    def test_tidb_cloud_ssl_enabled_custom_ca(self):
        """When MYSQL_SSL=true with MYSQL_SSL_CA, custom CA bundle path is used."""
        import os
        import importlib
        os.environ['MYSQL_SSL'] = 'true'
        os.environ['MYSQL_SSL_CA'] = '/etc/pki/tls/certs/custom-ca.pem'
        import app.config
        importlib.reload(app.config)

        self.assertTrue(app.config.Config.MYSQL_SSL)
        opts = app.config.Config.SQLALCHEMY_ENGINE_OPTIONS
        self.assertIn('connect_args', opts)
        self.assertTrue(opts['connect_args']['ssl_verify_cert'])
        self.assertTrue(opts['connect_args']['ssl_verify_identity'])
        self.assertEqual(opts['connect_args']['ssl_ca'], '/etc/pki/tls/certs/custom-ca.pem')


if __name__ == '__main__':
    unittest.main()

