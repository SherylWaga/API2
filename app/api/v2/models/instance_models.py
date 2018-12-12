from flask import Flask, request
# local imports

from ....db_config import init_db
app = Flask(__name__)
app.config['SECRET_KEY'] = "shewags"


class Instances():
    def __init__(self):
        self.db = init_db()

    def create_incident(self, title, comment, instance_type, location, images, videos,  created_by):
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

  
     
