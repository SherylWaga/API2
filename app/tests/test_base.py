# import os
# import unittest
# import json
# import pytest

# from app import create_app
# from app.db_config import _init_db


# class BaseClass(unittest.TestCase):
#     # valid sign up data
#         self.sign_up = {
                
#         "firstname": "jael",
#         "lastname": "mega",
#         "email": "mega@gmail.com",
#         "phonenumber":"07347890765",
#         "username":"jael",
#         "password":"jael22"
                        

#         }

#         # valid sign in data from valid sign up
#         self.sign_in = {
#                 "user_name": "jael",
#                 "password": "$2b$12$1DK4IwTSTLigMxrMj39F7.N49W.AZ2DiU3PEh.Wg2p23UlVzByzD2"
#         }

#         # sign in data with wrong username
#         self.invalid_username = {
#                 "user_name": "bettie",
#                 "password":"$2b$12$1DK4IwTSTLigMxrMj39F7.N49W.AZ2DiU3PEh.Wg2p23UlVzByzD2"
#         }

#         # sign in data with wrong password
#         self.wrong_password= {
#                 "user_name": "jael",
#                 "password": "2354#5778"
#         }


#         # wrong email
#         self.invalid_email = {
#         "firstname": "jael",
#         "lastname": "mega",
#         "email": "megagmail.com",
#         "phonenumber":"07347890765",
#         "username":"jael",
#         "password":"jael22"
                        

#         }
#         # invalid username
#         self.empty_string= {
#         "firstname": "",
#         "lastname": "",
#         "email": "",
#         "phonenumber":"",
#         "username":"",
#         "password":""
                        
#         }
#         #whitespaces
#         self.spaces= {
#         "firstname": "   ",
#         "lastname": "  ",
#         "email": "   ",
#         "phonenumber":"  ",
#         "username":"    ",
#         "password":"    "
                        
#         }

#         self.existing_record = {
#         "firstname": "jael",
#         "lastname": "mega",
#         "email": "mega@gmail.com",
#         "phonenumber":"07347890765",
#         "username":"jael",
#         "password":"jael22"
#         }

#         def setUp(self):
       
#                 self.app = create_app(config_name="development")
#                 self.client = self.app.test_client()
#                 self.db = init_db()


#                 res = self.client.post(
#                 '/api/v2/users',
#                 data=json.dumps(self.auth_signup),
#                 headers={"content-type": "application/json"}
#                 )

#                 login_res = self.client.post(
#                 '/api/v2/users/login',
#                 data=json.dumps(self.token_login),
#                 headers={"content-type": "application/json"}
#                 )
#                 response = json.loads(login_res.data.decode())
#                 self.token = response["access_token"]
                
#         def tearDown(self):

#             pass


# if __name__ == "__main__":
#     unittest.main()





