import os


class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """Development configurations"""
    url = os.getenv('DATABASE_URL')
    DEBUG = True
    

class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration, with test database."""
    test_url ="dbname='ireporter_test' host='localhost' port='5432' user='postgres' password='pycoders'"
    TESTING = True
    DEBUG = True
    test_url = os.getenv('TESTDATABASE_URL')

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
