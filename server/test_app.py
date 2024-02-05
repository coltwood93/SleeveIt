import unittest
from unittest import TestCase
from app import app, get_recommendation

class TestApp(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_recommendation(self):
        # Test with valid request data
        response = self.client.post('/get_recommendation', json={'location': 'Seattle'})
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('temperature', data)
        self.assertIn('recommendation', data)

        # Test with invalid request data
        response = self.client.post('/get_recommendation', json={})
        self.assertEqual(response.status_code, 400)
        data = response.json
        self.assertEqual(data['error'], 'Invalid request format')

if __name__ == '__main__':
    unittest.main()
