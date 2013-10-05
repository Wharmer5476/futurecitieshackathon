from collections import namedtuple

from flask import Flask, abort, jsonify, request, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pedestrian-counts/')
def pedestrian_counts():
    return jsonify(pedestrian_counts(parameters))

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
    return {
        "2013-10-10T13:00": {
            "mongo-id-1": {
                "site": {
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
                }
            }
        }
    }

def crowded(parameters):
    return pedestrian_counts(parameters)

if __name__ == "__main__":
    app.run(host="172.16.12.87", debug=True)