import unittest
import json
from tests.server_test import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_request(self):
        response = self.client.post('/requests', json={"name": "Test", "description": "Testing"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('id', data)


if __name__ == '__main__':
    unittest.main()

