from flask import Blueprint
from flask_restful import Api


from .views.user_views import Registration, Login ,Alogin
from .views.instance_views import Create_incident, Specific, Admin
version_2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_2)

api.add_resource(Registration, '/users')
api.add_resource(Login, '/users/login')
api.add_resource(Create_incident, '/incidents')
api.add_resource(Specific, '/incidents/<_id>') 
api.add_resource(Admin, '/incidents/<_id>')
api.add_resource(Alogin, '/admin/login')
