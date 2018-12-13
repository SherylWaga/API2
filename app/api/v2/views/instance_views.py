from flask_restful import Resource
from flask import Flask, jsonify, request, make_response
from app.api.v2.models.instance_models import Instances


app = Flask(__name__)


class Create_incident(Resource, Instances):

    def post(self):
            title = request.get_json()['title']
            comment = request.get_json()['comment']
            instance_type = request.get_json()['instance_type']
            location = request.get_json()['location']
            images = request.get_json()['images']
            videos = request.get_json()['videos']
            created_by = request.get_json()['created_by']
        
            errors = {}
            for key, value in request.get_json().items():
                if not value.strip():
                    errors[key] = "cannot be empty"
            if errors:
                return make_response(jsonify(
                   {"status": 400, "data": errors}), 400)

            Instances().create_incident(title, comment, instance_type, location, images, videos,  created_by)
            return make_response(jsonify(
                {"status": 201, "data": [
                    {"message": "successfully created"}]}), 201)

    def get(self):
        """GET all incidents"""
        rsp = Instances().get_all()
        return make_response(jsonify({
            "status": 200,
            "data": rsp,
            "message": "All incidents fetched successfully."
        }), 200)            
 

class Specific(Resource, Instances):
   
    def get(self, instance_id):      
        rsp = Instances().get_one(instance_id)
        if not rsp:
            return make_response(jsonify({
                "status": 404,
                "message": "Record not found."
            }), 404)
        return make_response(jsonify({
            "status": 200,
            "data": rsp,
            "message": "Record fetched successfully"
        }), 200)
             