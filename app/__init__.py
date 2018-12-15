from flask import Flask, Blueprint 
from flask_jwt_extended import (JWTManager)
from flask import Flask, jsonify, request, make_response
#local imports
from instance.config import app_config
from .db_config import create_tables
from .api.v2 import version_2 as v2

def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config = True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(v2)
    create_tables()
    app.config['JWT_SECRET_KEY'] = 'WAGS'
    jwt = JWTManager(app)

    @app.errorhandler(403)
    def forbidden(error):
        return make_response(jsonify(
            {"message": "forbidden"}), 403)
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return make_response(jsonify(
            {"message": "server error"}), 500)

    @app.errorhandler(404)
    def page_not_found(error):
        return make_response(jsonify(
            {"message": "method not allowed"}), 404)

    @app.errorhandler(500)
    def internal_server_error(error):
        return make_response(jsonify(
            {"message": "server error"}), 500)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return make_response(jsonify(
            {"message": "method not allowed"}), 405)
    return app
