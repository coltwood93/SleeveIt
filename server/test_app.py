import unittest
from unittest.mock import patch, Mock
from server.app import app
import requests

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('server.app.requests.get')
    def test_get_recommendation_short_sleeves(self, mock_get):
        # Mock the response from the OpenWeatherMap API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {
                "temp": 300,  # 80.33°F
                "feels_like": 305,  # 89.33°F
                "humidity": 50
            },
            "wind": {
                "speed": 5
            }
        }
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'SLEEVE_THRESHOLD_F': '69'}):
            response = self.app.get('/get_recommendation?location=test')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['recommendation'], 'short sleeves')
            self.assertAlmostEqual(data['temperature'], 80.33, places=2)
            self.assertAlmostEqual(data['feelslike'], 89.33, places=2)

    @patch('server.app.requests.get')
    def test_get_recommendation_long_sleeves(self, mock_get):
        # Mock the response from the OpenWeatherMap API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {
                "temp": 280,  # 44.33°F
                "feels_like": 275,  # 35.33°F
                "humidity": 50
            },
            "wind": {
                "speed": 5
            }
        }
        mock_get.return_value = mock_response

        with patch.dict('os.environ', {'SLEEVE_THRESHOLD_F': '69'}):
            response = self.app.get('/get_recommendation?location=test')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['recommendation'], 'long sleeves')
            self.assertAlmostEqual(data['temperature'], 44.33, places=2)
            self.assertAlmostEqual(data['feelslike'], 35.33, places=2)

    def test_get_recommendation_missing_location(self):
        response = self.app.get('/get_recommendation')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Location parameter is missing')

    @patch('server.app.requests.get')
    def test_get_recommendation_city_not_found(self, mock_get):
        # Mock the response from the OpenWeatherMap API
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)
        mock_get.return_value = mock_response

        response = self.app.get('/get_recommendation?location=nonexistentcity')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], "City 'nonexistentcity' not found")

    @patch('server.app.requests.get')
    def test_get_recommendation_invalid_api_key(self, mock_get):
        # Mock the response from the OpenWeatherMap API
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)
        mock_get.return_value = mock_response

        response = self.app.get('/get_recommendation?location=test')
        data = response.get_json()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 'Invalid API key')

if __name__ == '__main__':
    unittest.main()
