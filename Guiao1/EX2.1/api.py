from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Temperature(Resource):
    def get(self):
        return {'temperature': '37ºC'}

    def post(self):
        data = request.get_json()
        return jsonify(data)

api.add_resource(Temperature, '/')

if __name__ == '__main__':
    app.run(debug=True)