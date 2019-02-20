import unittest
import os
import json
from app import create_app
class user(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.incident = {
                
           
            "comment": "police officer receivi bribe",
            "instance_type": "Intervention",
            "location": "west nairobi",
            "title": "corruption",
            "images": "photo.jpg",
            "videos": "nate.mp4"           

        }
     
    # def test_create(self):
    #     res = self.client().post('/api/v2/incidents', data=json.dumps(self.incident),
    #                              content_type="application/json")
    #     self.assertIn("successfully created", str(res.data))
       
  
    
if __name__ == '__main__':
    unittest.main()
 
 
 
 
 
 
 
 
 
 
 
 
 
 