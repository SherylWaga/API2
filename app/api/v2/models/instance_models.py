from flask import Flask, request
# local imports
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
from ....db_config import init_db



app = Flask(__name__)
app.config['SECRET_KEY'] = "shewags"


class Instances():
    def __init__(self):
        self.db = init_db()
     
    def create_incident(self, title, comment, instance_type, location, images, videos, created_by):
        incident = { 
            'title': title,
            'comment': comment,
            'instance_type': instance_type,
            'location': location,
            'images': images,
            'videos': videos,
            'created_by': created_by
        }
        query = """INSERT INTO incidents (created_by,title,comment,instance_type,location,images,videos) 
              VALUES(%(created_by)s,%(title)s,%(comment)s,%(instance_type)s,%(location)s,%(images)s,%(videos)s)"""
        cur = self.db.cursor()
        cur.execute(query, incident)
        self.db.commit()
        return incident

    def get_all(self):
        con = self.db
        cur = con.cursor()
        cur.execute("SELECT * FROM incidents")
        data = cur.fetchall()
        response = []
        for item, items in enumerate(data):
            incident_id, created_on, created_by, title, comment, instance_type, location, status, images, videos = items
            value = dict(
                incident_id_id=int(incident_id),
                created_on=created_on,
                created_by=created_by,
                title=title,
                comment=comment,
                instance_type=instance_type,
                location=location,
                status=status

            )
            response.append(value)
        return response

    def get_one(self, _id):
        con = self.db
        cur = con.cursor()
        cur.execute("SELECT incident_id, created_on, created_by, title, comment, instance_type,"
                     " location, status FROM incidents WHERE incident_id='" + str(_id) + "'")
        data = cur.fetchall()
        response = []
        for item, items in enumerate(data):
            incident_id, created_on, created_by, title, comment, instance_type, location, status = items
            value = dict(
                incident_id=int(incident_id),
                created_on=created_on,
                created_by=created_by,
                title=title,
                comment=comment,
                instance_type=instance_type,
                location=location,
                status=status

            )
            response.append(value)
        return response
    
    def erase_instance(self, _id):
        con = self.db
        cur = con.cursor()
        cur.execute("SELECT * FROM incidents")
        data = cur.fetchall()
        value = str(data)
        if _id in value:
            cur.execute(
                "DELETE FROM incidents WHERE incident_id='" + str(_id) + "'")
            con.commit()
        return "successfully deleted"
        

    def check_comment(self, comment):
       cur = self.db.cursor()
       cur.execute("SELECT * FROM incidents")
       data = cur.fetchall()
       value2 = str(data)
       if comment in value2:
            return True
       return False

    def verify_action(self):
        cur = self.db.cursor()
       
        cur.execute("SELECT * FROM incidents")
        data = cur.fetchone()
       
        value = list(data)
    
        return value[2]

    def get_by_id(self, _id):
        con = self.db
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM incidents WHERE incident_id='" + str(_id) + "'")
        data = cur.fetchone()
        
