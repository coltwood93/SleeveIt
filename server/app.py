from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "4f36787a2ef947e2e69b1012c3809efd"

@app.route("/get_recommendation", methods=["GET"])
def get_recommendation():
    location = request.args.get("location")  # Retrieve location from query parameters
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"

    try:
        response = requests.get(api_url)
        data = response.json()
        temperature_kelvin = data["main"]["temp"]
        temperature_fahrenheit = (temperature_kelvin - 273.15)*9/5 + 32
        recommendation = "short sleeves" if temperature_fahrenheit > 65 else "long sleeves"
        return jsonify({'temperature': temperature_fahrenheit, 'recommendation': recommendation})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Invalid request format'}), 400

if __name__ == "__main__":
    app.run(debug=True)
