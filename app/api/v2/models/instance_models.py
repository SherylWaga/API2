from flask import Flask, request
# local imports

from ....db_config import init_db
app = Flask(__name__)
app.config['SECRET_KEY'] = "shewags"


def serialiser_incident(incidents):
    return dict(
        incident_id=incidents[0],
        created_on=incidents[1],
        created_by=incidents[2],
        title=incidents[3],
        comment=incidents[4],
        instance_type=incidents[5],
        location=incidents[6],
        status=incidents[7],
        image=incidents[8],
        video=incidents[9]
        )


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
       
        cur = self.db.cursor()
        cur.execute("SELECT * FROM incidents")
        incidents = cur.fetchall()
        new_incidents = []
        for record in incidents:
            new_incidents.append(serialiser_incident(record))
           
            return new_incidents

       
    def fetch_instance(self):
        cur = self.db.cursor()
        username = request.json.get('username')
        password = request.json.get('password')
        cur.execute("""SELECT * FROM users WHERE username = '%s'""" % (username))
        data = cur.fetchone()
        value = list(data)
        if password == value[6]:
            return True
        return False
     
