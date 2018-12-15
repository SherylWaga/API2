from flask_restful import Resource
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

from app.api.v2.models.instance_models import Instances
from ....db_config import init_db
from ..views.user_views import Login

app = Flask(__name__)


class Create_incident(Resource, Instances):
    @jwt_required
    def post(self):
            title = request.get_json()['title']
            comment = request.get_json()['comment']
            instance_type = request.get_json()['instance_type']
            location = request.get_json()['location']
            images = request.get_json()['images']
            videos = request.get_json()['videos']
            created_by = get_jwt_identity()
        
            errors = {}
            for key, value in request.get_json().items():
                if not value.strip():
                    errors[key] = "cannot be empty"
            if errors:
                return make_response(jsonify(
                   {"status": 400, "data": errors}), 400)
            if  Instances().check_comment(comment):
                return make_response(jsonify(
                {"status": 400, "data": [
                    {"message": "Record already exists"}]}), 400) 
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
    @jwt_required
    def get(self, _id):      
        rsp = Instances().get_one(_id)
        if rsp:
                
            return make_response(jsonify({
                "status": 200,
                "data": rsp,
                "message": "Record fetched successfully"
            }), 200)
        return make_response(jsonify({
                "status": 404,
                "message": "Record not found."
            }), 404)
    
    @jwt_required
    
    def delete(self,_id):
        """Delete existing record"""
        if Login().current_logged():         
            if Instances().get_by_id(_id):
                return jsonify({'status_code': 404,
                                'message': ' Record does not exist'})
            if not Instances().verification(_id):
                return jsonify({'status_code': 403,
                                'message': 'You can only delete your records.'})
            Instances().erase_instance(_id)
            resp = jsonify(
                {
                    'status_code':200,
                    'message':'successfully deleted',

                })
            response.status_code = 200
            return resp

    def put(self,_id):
        """Edit existing record"""
        if Login().current_logged(): 
            
            location=request.json.get('location')
            comment = request.json.get('comment')        
            if Instances().get_by_id(_id):
                return jsonify({'status_code': 404,
                                'message': ' Record does not exist'})
            if not Instances().verification(_id):
                return jsonify({'status_code': 403,
                                'message': 'You can only edit your records.'})
            Instances().edit_incident, (_id)
            resp = jsonify(
                {
                    'status_code':200,
                    'message':'successfully updated',

                })
            
            return resp

         
        
      
        
        
        