from flask import Flask, request, send_file
from flask_api import status
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from db import db
from searchEngine import searchEngine

app = Flask(__name__)
api = Api(app)
db = db()
searchEngine = searchEngine(db=db)

class SearchEngine(Resource):
    def get(self, body):
        query = request.args.get('query')
        result = searchEngine.searchQuery(query)
        return jsonify(result)

api.add_resource(SearchEngine, '/api/searchengine') # Route_1


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5002)