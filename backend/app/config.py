import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from backend/.env if it exists
backend_dir = Path(__file__).resolve().parent.parent
env_path = backend_dir / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)


class Config:
    """Application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'smart-travel-dev-secret-key')
    
    # MySQL Database Settings
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'travel_app')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'smart_travel_db')
    
    # TiDB Cloud / SSL Configuration
    MYSQL_SSL = os.environ.get('MYSQL_SSL', 'false').lower() in ('true', '1', 'yes')
    MYSQL_SSL_CA = os.environ.get('MYSQL_SSL_CA', '').strip()

    import urllib.parse
    _encoded_password = urllib.parse.quote_plus(MYSQL_PASSWORD)
    
    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{_encoded_password}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 280,
    }

    # Configure TLS/SSL for TiDB Cloud or production MySQL when enabled
    if MYSQL_SSL:
        ssl_ca_path = MYSQL_SSL_CA or '/etc/ssl/certs/ca-certificates.crt'
        SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_pre_ping': True,
            'pool_recycle': 280,
            'connect_args': {
                'ssl_verify_cert': True,
                'ssl_verify_identity': True,
                'ssl_ca': ssl_ca_path,
            }
        }

    # Step 9 - Provider Architecture Configuration
    DEMO_PROVIDER_ENABLED = os.environ.get('DEMO_PROVIDER_ENABLED', 'true').lower() in ('true', '1', 'yes')
    
    # Future live providers remain strictly disabled by default
    VIATOR_ENABLED = os.environ.get('VIATOR_ENABLED', 'false').lower() in ('true', '1', 'yes')
    VIATOR_API_KEY = os.environ.get('VIATOR_API_KEY', '')
    
    BOOKING_ENABLED = os.environ.get('BOOKING_ENABLED', 'false').lower() in ('true', '1', 'yes')
    BOOKING_API_KEY = os.environ.get('BOOKING_API_KEY', '')
    BOOKING_AFFILIATE_ID = os.environ.get('BOOKING_AFFILIATE_ID', '')

