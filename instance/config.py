import os


class Config(object):
    """
    Common configurations
    """
    # DATABASE_URL = 'postgres://nktlakqprtmmcj:4343708d44c97d374c9928afb66bb98fb4b09ab05281535ac616a99a11bf9165@ec2-23-21-188-236.compute-1.amazonaws.com:5432/deq12r5mm0ej4p
# '
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
