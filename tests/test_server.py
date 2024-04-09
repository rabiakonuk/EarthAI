import json
import unittest
from server.server import app

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        # Test the /predict endpoint
        response = self.app.post('/predict', data=json.dumps({"input": "test data"}),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        # Assert conditions on the response format and content
        self.assertIn('predictions', data, "Response should contain predictions")

if __name__ == '__main__':
    unittest.main()
