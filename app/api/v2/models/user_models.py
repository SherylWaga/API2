from flask import Flask
#local imports
from  ....db_config import init_db
app =Flask(__name__)
app.config['SECRET_KEY']="shewags"

class users():
    def __init__(self):
        self.db=init_db()
    
    def save_user(self,firstname,lastname,email,phonenumber,username,password):
       
         users = {
              'firstname':firstname,
              'lastname':lastname,
              'email':email,
              'phonenumber':phonenumber,
              'username':username,
              'password':password

         }
         query = """INSERT INTO users(firstname,lastname,email,phonenumber,username,password)
          VALUES(%(firstname)s, %(lastname)s, %(email)s, %(phonenumber)s ,%(username)s ,%(password)s)"""
         cur=self.db.cursor()
         cur.execute(query,users)
         self.db.commit()


         return users