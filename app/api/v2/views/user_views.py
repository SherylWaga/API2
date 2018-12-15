
from flask import Flask, jsonify, json, request, make_response
from flask_restful import Resource ,Api
from flask_jwt_extended import (JWTManager,jwt_required, create_access_token,get_jwt_identity)
# local imports
from app.api.v2.models.user_models import users
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
            
            errors = {}
            for key, value in request.get_json().items():
                if not value.strip():
                    errors[key] = "cannot be empty"
            if errors:
                return make_response(jsonify(
                   {"status": 400, "data": errors}), 400)
            if users().verify_membership(username, email):
                return make_response(jsonify(
                   {"status": 400, "message": "user already exists"}), 400)
            users().save_user(firstname, lastname, email, phonenumber, username, password)
            return make_response(jsonify(
                   {"status": 200, "data": [
                    {"message": "Registration successful"}]}), 200)
        except:
            return make_response(jsonify(
                {"status": 400, "data": [
                    {"message": "Required field or fields"}]}), 400)  


class Login (Resource):
        def post(self):
            username = request.json.get('username')
            password = request.json.get('password')
            if users().fetch_user(username, password):
             
                access_token = create_access_token(identity=username)
                response = jsonify({'token':access_token,
                        "message":"Welcome " + username,
                        "status_code":201})
                return response

            return make_response(jsonify({"status": 201, "data": [
                    {"message": "Please sign up or check log in details"}]
                    }), 201)

        @jwt_required
        def current_user(self):
            current = get_jwt_identity()
            return current

        @jwt_required
        def current_logged(self):
            return True

