from flask import Flask, request
# local imports

from ....db_config import init_db
from ..views.user_views import Login




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
        current_user = Login().current_user()
        con = self.db
        cur = con.cursor()
        cur.execute(
            "DELETE FROM incidents WHERE incident_id='" + str(_id) + "' AND created_by='" + str(current_user) + "'")
        con.commit()
      
    def edit_by_admin(self, _id, status):
        con = self.db
        cur = con.cursor()
        new_value = {  
            'status': status
                    }

        cur.execute("""UPDATE incidents SET status=%s WHERE incident_id=%s""", (status, _id))
        con.commit()


    def check_comment(self, comment):
       cur = self.db.cursor()
       cur.execute("SELECT * FROM incidents")
       data = cur.fetchall()
       value2 = str(data)
       if comment in value2:
            return True
       return False


    def get_by_id(self, _id):
        con = self.db
        cur = con.cursor()
        cur.execute("SELECT created_by FROM incidents WHERE incident_id='" + _id + "'")
        data = cur.fetchall()
        data_list = list(data)
        if len(data_list) == 0:
            return True
     
        
    def verification(self, _id):
        current_user = Login().current_user()
        con = self.db
        cur = con.cursor()
        cur.execute("SELECT incident_id FROM incidents WHERE created_by='" + current_user + "'")
        data = cur.fetchall()
        value = str(data)
        if str(_id) in value:
            return True

    def edit_incident(self, _id):
        current_user = Login().current_user()
        con = self.db
        cur = con.cursor()
        location = request.json.get('location')
        comment = request.json.get('comment')   
        payload = { 
            'comment': comment,
            'location': location
        }
        query = "UPDATE incidents SET comment=%(comment)s," \
                "location=%(location)s WHERE incident_id='" + str(_id) + "' AND created_by='" + str(
            current_user) + "'"
        cur.execute(query, payload)
       
    #check status
    def check_status(self):
        con = self.db
        cur = con.cursor()
        cur.execute("SELECT status FROM incidents WHERE status='draft'")
        data = cur.fetchone()
        
        return True
    
    #re-update of already existing status
    def duplicate_update(self, _id, status):
        con = self.db
        cur = con.cursor()
        cur.execute("SELECT status FROM incidents WHERE status=%s",(_id))
        data = cur.fetchone()
        for item in data:
            if item == status:
                return True