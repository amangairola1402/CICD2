import unittest
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_predict_endpoint(self):
        response = self.client.post('/api/predict', json={"sentence": "John kicked the ball."})
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("roles", data)
        self.assertIn("sentence", data)

if _name_ == '_main_':
    unittest.main()