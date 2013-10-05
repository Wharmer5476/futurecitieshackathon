from collections import namedtuple
from os import environ

from pymongo import MongoClient
from flask import Flask, abort, jsonify, request, render_template, url_for

from db import PedestrianCounts


app = Flask(__name__)

db_user = environ['futurecities_db_user']
db_pass = environ['futurecities_db_pass']
db_uri = 'mongodb://%s:%s@ds049548.mongolab.com:49548' % (db_user, db_pass)
db_name = 'futurecitieshackathon'
collection_name = 'pedestiranCounts'
conn = MongoClient('mongodb://%s:%s@ds049548.mongolab.com:49548/futurecitieshackathon' % (db_user, db_pass))
db = PedestrianCounts(conn, db_name, collection_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pedestrian-counts/')
def pedestrian_counts():
    return jsonify(pedestrianCounts=pedestrian_counts(parameters))

@app.route('/api/crowded')
def croweded():
    return jsonify(pedestrian_counts(parameters()))

Parameters = namedtuple('Parameters', 'threshold start stop limit')

def parameters():
    # TODO: validation
    threshold = request.args.get('threshold', 10)
    try:
        threshold = int(threshold)
    except ValueError:
        abort(400, 'threshold should be integer value, e.g. 10')
    start = request.args.get('from', None)
    stop = request.args.get('to', None)
    limit = request.args.get('limit', None)
    return Parameters(threshold, start, stop)

def pedestrian_counts(parameters):
    return {"2013-10-10T13:00": [{"site": {
                    "id": 1,
                    "name": "hyde park"
                },
                "borough": "Westminster",
                "geocode": {
                    "lat": 42.0,
                    "long": 23.0
                    },
                "pedestrianCount": {
                    "current": 22,
                    "mean": 20,
                    "std": 1 
                }}]}

def crowded(parameters):
    return pedestrian_counts(parameters)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)