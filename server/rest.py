from flask import Flask, request, send_file
from flask_api import status
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class SearchEngine(Resource):
    def post(self, body):
        result = body
        return jsonify(result)
        

api.add_resource(SearchEngine, '/api/searchengine') # Route_1


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5002)