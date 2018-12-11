from flask import Flask, request, send_file
from flask_api import status
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from db import db
from searchEngine import searchEngine, getTopFive

app = Flask(__name__)
# db = db()
# searchEngine = searchEngine(db=db)

def get_db():
    database = db()
    return database

# @app.teardown_appcontext
# def close_connection(exception):
#     db = get_db()
#     db.closeDb()

@app.route("/api/searchengine")
def index():
    query = request.args.get('query')
    db = get_db()
    db.start()
    result,totscore = searchEngine(db=db).searchQuery(query)
    response = jsonify(getTopFive(result,totscore))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# api.add_resource(SearchEngine, '/api/searchengine') # Route_1


if __name__ == '__main__':
     app.run(debug=True, port=5002)
    #  app.run(debug=True, host='0.0.0.0', port=5002)