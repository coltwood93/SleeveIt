"""Backend Flask server that handles API calls and recommendation logic"""

from os import environ
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import requests

app = Flask(__name__)
load_dotenv()
CORS(app)

SECRET_KEY = environ.get('API_KEY')     # get API Key from .env file
# Get temperature threshold from environment variable, default to 69 if not set
try:
    SLEEVE_THRESHOLD_F = int(environ.get('SLEEVE_THRESHOLD_F', 69))
except ValueError:
    SLEEVE_THRESHOLD_F = 69

@app.route("/get_recommendation", methods=["GET"])
def get_recommendation():
    """Requests temperature through OpenWeatherMap API, 
    then recommends sleeve length based on return data"""
    location = request.args.get("location")  # Retrieve location from frontend GET request
    if not location:
        return jsonify({'error': 'Location parameter is missing'}), 400

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={SECRET_KEY}"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        # parse temperature from returned JSON
        temperature_kelvin = data["main"]["temp"]
        temperature_fahrenheit = (temperature_kelvin - 273.15)*9/5 + 32

        #parse additional fields from JSON
        feelslike = (data["main"]["feels_like"] - 273.15)*9/5 + 32 # feel in fahrenheit
        windspeed = data["wind"]["speed"]   # meters/sec
        humidity = data["main"]["humidity"] # humidity %

        # recommendation logic using "feels like" temperature and configurable threshold
        recommendation = "short sleeves" if feelslike > SLEEVE_THRESHOLD_F else "long sleeves"

        # return data to frontend
        return jsonify({
            'temperature': temperature_fahrenheit,
            'recommendation': recommendation,
            'feelslike': feelslike,
            'windspeed': windspeed,
            'humidity': humidity
            }
        )
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            return jsonify({'error': f"City '{location}' not found"}), 404
        elif err.response.status_code == 401:
            return jsonify({'error': 'Invalid API key'}), 401
        else:
            return jsonify({'error': f"An error occurred: {err}"}), err.response.status_code
    except requests.exceptions.RequestException as err:
        return jsonify({'error': f'An error occurred: {err}'}), 400

if __name__ == "__main__":
    app.run(debug=True)
