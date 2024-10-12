from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Registry(Resource):        
    services = []
    
    def get(self, service_id=None):
        if service_id is None:
            return jsonify(self.services)
        for service in self.services:
            if service['id'] == service_id:
                return jsonify(service)
        return {'message': 'Service not found'}, 404

    def post(self):
        data = request.get_json()
        if 'name' not in data or 'url' not in data:
            return {'message': 'Invalid request'}, 400
        service_id = len(self.services) + 1
        service = {
            'id': service_id,
            'name': data['name'],
            'url': data['url']
        }
        self.services.append(service)
        return jsonify(service), 201

    def put(self, service_id):
        data = request.get_json()
        if 'name' not in data and 'url' not in data:
            return {'message': 'Invalid request'}, 400
        for service in self.services:
            if service['id'] == service_id:
                service['name'] = data.get('name', service['name'])
                service['url'] = data.get('url', service['url'])
                return jsonify(service)
        return {'message': 'Service not found'}, 404

    def delete(self, service_id):
        if not any(service['id'] == service_id for service in self.services):
            return {'message': 'Service not found'}, 404
        self.services = [service for service in self.services if service['id'] != service_id]
        return {'message': 'Service deleted'}

api.add_resource(Registry, '/services', '/services/<int:service_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5002)