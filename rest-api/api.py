from collections import namedtuple
from os import environ
from datetime import datetime

from pymongo import MongoClient
from flask import Flask, abort, jsonify, request, render_template, url_for

from db import PedestrianCounts


db_user = environ['futurecities_db_user']
db_pass = environ['futurecities_db_pass']
db_uri = 'mongodb://%s:%s@ds049548.mongolab.com:49548' % (db_user, db_pass)
db_name = 'futurecitieshackathon'
collection_name = 'pedestrianCounts'
client = MongoClient('mongodb://%s:%s@ds049548.mongolab.com:49548/futurecitieshackathon' % (db_user, db_pass))
db = PedestrianCounts(client[db_name][collection_name])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pedestrian-counts/')
def pedestrian_counts():
    return jsonify(pedestrianCounts=pedestrian_counts(parameters()))

Parameters = namedtuple('Parameters', 'threshold start stop limit')

def parameters():
    # TODO: validation
    threshold = request.args.get('threshold', 10)
    try:
        threshold = int(threshold)
    except ValueError:
        abort(400, 'threshold should be integer value, e.g. 10')
    start = request.args.get('from', None)
    if start:
        start = parse_timestamp(start)
    stop = request.args.get('to', None)
    if stop:
        stop = parse_timestamp(stop)
    limit = request.args.get('limit', None)
    p = Parameters(threshold, start, stop, limit)
    print p
    return p

def parse_timestamp(timestamp):
    try:
        return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M')
    except ValueError:
        abort(400, 'start and stop should be in the format yyyy-mm-ddThh:mm')

def pedestrian_counts(parameters):
    return {"2013-10-10T13:00": db.counts(parameters.start, parameters.stop)}

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)