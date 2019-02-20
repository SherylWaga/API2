from flask import Flask, jsonify, json, request, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
# local imports
from app.api.v2.models.user_models import users , UsersRole
app = Flask(__name__)

api = Api(app) 
app.config['JWT_SECRET_KEY'] = 'WAGS'


class Registration(Resource):

    def post(self):
        try:

            firstname = request.get_json()['firstname']
            lastname = request.get_json()['lastname']
            email = request.get_json()['email']
            phonenumber = request.get_json()['phonenumber']
            username = request.get_json()['username']
            password = request.get_json()['password']
            validator = "@"
            validator2 = ".com"
            errors = {}
            for key, value in request.get_json().items():
                if not value.strip():
                    errors[key] = "cannot be empty"
            if errors:
                return make_response(jsonify(
                   {"status": 404, "data": errors}), 404)
                
            if validator not in email or validator2 not in email:
                return make_response(jsonify(
                   {"status": 404, "message": "invalid email"}), 404)
                        
            if users().verify_membership(username, email, phonenumber, password):
                return make_response(jsonify(
                   {"status": 404, "message": "user already exists"}), 404)
            users().save_user(firstname, lastname, email, phonenumber, username, password)
            return make_response(jsonify(
                   {"status": 200, "data": [
                    {"message": "Registration successful"}]}), 200)
        except:
            return make_response(jsonify(
                {"status": 404, "data": [
                    {"message": "Required field or fields"}]}), 404)  


class Login (Resource):
        def post(self):
            username = request.json.get('username')
            password = request.json.get('password')
            if not users().fetch_user():
                return jsonify({'status_code': 404,
                                'message': 'invalid username'})
            if not users().validate_pass():
                return jsonify({'status_code': 404,
                                'message': 'invalid password.'})
            

            token = create_access_token(identity=username)
            response = jsonify({'token': token,
                                "message": "Welcome " + username,
                                "status_code": 201})
            return response

        @jwt_required
        def current_user(self):
            current = get_jwt_identity()
            return current

        @jwt_required
        def current_logged(self):
            return True
    
class Alogin (Resource):
        def post(self):
            username = request.json.get('username')
            password = request.json.get('password')
            if UsersRole().admin_role:
            

                token = create_access_token(identity=username)
                response = jsonify({'token': token,
                                    "message": "Welcome " + username,
                                    "status_code": 201})
                return response
            
            return jsonify({'status_code': 403,
                                'message': 'admin only'})