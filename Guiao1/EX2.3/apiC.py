from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random
import requests

app = Flask(__name__)
api = Api(app)

class TemperatureC(Resource):
    def get(self):
        return {'temperature': random.randint(0, 100)}

    def post(self):
        data = request.get_json()
        return jsonify(data)

api.add_resource(TemperatureC, '/')

if __name__ == '__main__':
    response = requests.get("http://127.0.0.1:5002/services/1")
    if response.status_code == 404:
        requests.post('http://127.0.0.1:5002/services', json={'name': 'TemperatureC', 'url': 'http://127.0.0.1:5000/'})
    app.run(debug=True)