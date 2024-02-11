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

@app.route("/get_recommendation", methods=["GET"])
def get_recommendation():
    """Requests temperature through OpenWeatherMap API, 
    then recommends sleeve length based on return data"""
    location = request.args.get("location")  # Retrieve location from frontend GET request
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={SECRET_KEY}"

    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()

        # parse temperature from returned JSON
        temperature_kelvin = data["main"]["temp"]
        temperature_fahrenheit = (temperature_kelvin - 273.15)*9/5 + 32

        # recommendation logic
        recommendation = "short sleeves" if temperature_fahrenheit > 69 else "long sleeves"

        # return data to frontend
        return jsonify({'temperature': temperature_fahrenheit, 'recommendation': recommendation})
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Invalid request format'}), 400

if __name__ == "__main__":
    app.run(debug=True)
