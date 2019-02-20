import unittest
import os
import json
from app import create_app


class user(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.invalid_email = {
                
            "firstname": "jael",
            "lastname": "mega",
            "email": "megagmail.com",
            "phonenumber": "07347890765",
            "username": "jael",
            "password": "jael22"
            

        }
        self.login = {
                
       
        
            "username": "jael",
            "password": "jael22"
                        

        }

    def test_register_user(self):
        res = self.client().post('/api/v2/users', data=json.dumps(self.invalid_email),
                                 content_type="application/json")
        self.assertEqual(res.status_code, 404)
        self.assertIn("invalid email", str(res.data))
  
    
if __name__ == '__main__':
    unittest.main()