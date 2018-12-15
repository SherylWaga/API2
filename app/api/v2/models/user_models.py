from flask import Flask, request
from flask_jwt_extended import JWTManager
# local imports

from ....db_config import init_db
app = Flask(__name__)

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
            'password': password

        }
        query = """INSERT INTO users(firstname,lastname,email,phonenumber,username,password)
          VALUES(%(firstname)s, %(lastname)s,%(email)s, %(phonenumber)s ,%(username)s ,%(password)s)"""
        cur = self.db.cursor()
        cur.execute(query, users)
        self.db.commit()
        return users

    def fetch_user(self, username, password):
        cur = self.db.cursor()
       
        cur.execute("""SELECT * FROM users WHERE username = '%s'"""%(username))
        data = cur.fetchone()
     
        value = list(data)
        if password == value[6]:
            return True
        return False

    def verify_membership(self, username, email):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        value2 = str(data)
        if username in value2 or email in value2:
            return True
        return False


