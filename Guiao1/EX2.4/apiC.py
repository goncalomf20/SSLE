from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random
import requests

app = Flask(__name__)
api = Api(app)

class TemperatureC(Resource):
    def get(self):
        return {'TemperatureC': random.randint(0, 100)}

    def post(self):
        data = request.get_json()
        return jsonify(data)

api.add_resource(TemperatureC, '/')

if __name__ == '__main__':
    response = requests.post('http://127.0.0.1:5002/services', json={'name': 'TemperatureC', 'url': 'http://127.0.0.1:5000/'})
    print(response.json()['message'])
    app.run(debug=True)