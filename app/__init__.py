from flask import Flask, Blueprint
from .api.v2 import version_2 as v2
#local imports
from instance.config import app_config
from .db_config import create_tables


def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config = True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(v2)
    create_tables()
    return app