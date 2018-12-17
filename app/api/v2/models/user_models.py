from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
from flask_bcrypt import Bcrypt
# local imports

from ....db_config import init_db
app = Flask(__name__)
bcrypt=Bcrypt(app)

class users():
    def __init__(self):
        self.db = init_db()

    def save_user(self, firstname, lastname, email, phonenumber, username, password):

        users = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phonenumber': phonenumber,
            'username': username,
            'password': bcrypt.generate_password_hash(password).decode('utf-8')

        }
        query = """INSERT INTO users(firstname,lastname,email,phonenumber,username,password)
          VALUES(%(firstname)s, %(lastname)s,%(email)s, %(phonenumber)s ,%(username)s ,%(password)s)"""
        cur = self.db.cursor()
        cur.execute(query, users)
        self.db.commit()
        return users

    def fetch_user(self):
        cur = self.db.cursor()
        username = request.json.get('username')
        cur.execute("""SELECT * FROM users WHERE username = '%s'"""%(username))
        data = cur.fetchone()
        value = list(data)
        if username == value[5]:
            return True
        return False

    
    #avoid duplicate entries
    def verify_membership(self, username, email, phonenumber, password):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        value2 = str(data)
        if username in value2 or email in value2 or phonenumber in value2 or password in value2:
            return True
        

    def validate_pass(self):
        con = self.db
        cur = con.cursor()
        username = request.json.get('username')
        password = request.json.get('password')
        cur.execute("SELECT * FROM users WHERE username='" + str(username) + "'")
        data = cur.fetchone()
        convert_data = list(data)
        pword = convert_data[4]
        if bcrypt.check_password_hash(pword, password):
            return True
   
class UsersRole(users):
        #verify admin
        def user_role(self):
            cur = self.db.cursor()
            cur.execute("SELECT username FROM users WHERE isadmin = 'true'")
            data = cur.fetchone()
            for item in data:
                print (data)
                return item
        
        def admin_role(self,username):
            cur = self.db.cursor()
            cur.execute("SELECT username FROM users WHERE isadmin = 'true'")
            data = cur.fetchone()
            for item in data:
                if item == username:
                   return True
                
            
           
            
