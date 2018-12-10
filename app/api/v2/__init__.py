from flask import Blueprint
from flask_restful import Api

from .views.user_views import Registration 

version_2=Blueprint('api_v2',__name__,url_prefix='/api/v2')
api=Api(version_2)

api.add_resource(Registration,'/users')