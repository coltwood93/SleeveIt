from os import environ
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import requests

app = Flask(__name__)
load_dotenv()
CORS(app)

SECRET_KEY = environ.get('API_KEY')

@app.route("/get_recommendation", methods=["GET"])
def get_recommendation():
    """Requests temperature through OpenWeatherMap API, 
    then recommends sleeve length based on return data"""
    location = request.args.get("location")  # Retrieve location from query parameters
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={SECRET_KEY}"

    try:
        response = requests.get(api_url)
        data = response.json()
        temperature_kelvin = data["main"]["temp"]
        temperature_fahrenheit = (temperature_kelvin - 273.15)*9/5 + 32
        recommendation = "short sleeves" if temperature_fahrenheit > 69 else "long sleeves"
        return jsonify({'temperature': temperature_fahrenheit, 'recommendation': recommendation})
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Invalid request format'}), 400

if __name__ == "__main__":
    app.run(debug=True)
