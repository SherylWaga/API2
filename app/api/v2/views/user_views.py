
from flask import jsonify,json,request, make_response
from flask_restful import Resource
# local imports
from app.api.v2.models.user_models import users 
class Registration(Resource):


    def post(self):
        firstname  = request.get_json()['firstname']
        lastname = request.get_json()['lastname']
        email = request.get_json()['email']
        phonenumber = request.get_json()['phonenumber']
        username =  request.get_json()['username']
        password = request.get_json()['password']
            
        if not firstname or not lastname or not email or not phonenumber or not username or not password:
            return make_response(jsonify({"status":201, "data":[{"message":"cannot be empty"}]}), 201)
         
        if firstname.isspace() or lastname.isspace() or email.isspace() or phonenumber.isspace() or username.isspace() or password.isspace():
            return make_response(jsonify({"status":201, "data":[{"message":"no blanks"}]}), 201)
        response= users().save_user(firstname,lastname,email,phonenumber,username,password)
        return make_response(jsonify({"status":201, "data":[{"message":"Registration successful"}]}), 201)
       
       
        









