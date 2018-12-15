import os


class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """Development configurations"""
    DATABASE_URL = "dbname='ireporter' host='localhost' port='5432' user='postgres' password='pycoders'"
    DEBUG = True


class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration, with test database."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = "dbname='ireporter' host='localhost' port='5432' user='postgres' password='pycoders'"

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
