import os
import requests
import json
import random
import time

from flask import Flask, json

api = Flask(__name__)

with open("microservice/cities.json",'r') as file:
    cities = json.load(file)

@api.route('/cities', methods=['GET'])
def get_cities():
    state = random.choice(list(cities.keys()))
    city = random.choice(cities[state])
    response = {"city":city, "state":state}
    return json.dumps(response)

if __name__ == '__main__':
    api.run(debug=False, port=5001)
