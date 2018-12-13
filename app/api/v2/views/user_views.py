
from flask import Flask, jsonify, json, request, make_response
from flask_restful import Resource ,Api

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

            users().save_user(firstname, lastname, email, phonenumber, username, password)
            return make_response(jsonify(
                {"status": 201, "data": [
                    {"message": "Registration successful"}]}), 201)
        except:
            return make_response(jsonify(
                {"status": 400, "data": [
                    {"message": "Required field or fields"}]}), 400)  


class Login (Resource):
        def post(self):

            if users().fetch_user():
                return make_response(jsonify({"status": 201, "data": [
                    {"message": "successfully logged in"}]
                    }), 201)
                access_token = create_access_token(identity=username)
                return jsonify(access_token=access_token)
                con.commit()

            return make_response(jsonify({"status": 201, "data": [
                    {"message": "Please sign up or check log in details"}]
                    }), 201)
            

