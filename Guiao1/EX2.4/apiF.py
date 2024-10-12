from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random
import requests

app = Flask(__name__)
api = Api(app)

class TemperatureF(Resource):
    def get(self):
        return {'TemperatureF': random.randint(32, 212)}
        

    def post(self):
        data = request.get_json()
        return jsonify(data)

api.add_resource(TemperatureF, '/')

if __name__ == '__main__':
    response = requests.post('http://127.0.0.1:5002/services', json={'name': 'TemperatureF', 'url': 'http://127.0.0.1:5001/'})
    print(response.json()['message'])
    app.run(debug=True, port=5001)