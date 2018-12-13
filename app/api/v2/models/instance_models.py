from flask import Flask, request
# local imports

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
        for item , items in enumerate(data):
            incident_id, created_on, created_by, title, comment, instance_type, location, status, images, videos = items
            value= dict(
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

       
    def get_one(self, instance_id):
        con = self.db
        cur= con.cursor()
        cur.execute("SELECT incident_id, created_on, created_by, title, comment, instance_type,"
                     " location, status FROM incidents WHERE incident_id='" + str(instance_id) + "'")
        data = cur.fetchall()
        response = []
        for item, items in enumerate(data):
            incident_id, created_on, created_by, title, comment, instance_type, location, status = items
            value= dict(
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
    
    def erase_instance(self, instance_id):
        con = self.db
        cur = con.cursor()
        cur.execute(
            "DELETE FROM incidents WHERE incident_id='" + str(instance_id) + "'")
        con.commit()
        return True
     
