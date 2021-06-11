import sys
import os

from info import Flights
from flask import Flask, abort, jsonify
from waitress import serve

"""In order to get a csv file."""
try:
    file_csv = sys.argv[1]
except IndexError:
    print("Please provide a csv file and try again.")
    sys.exit(20)

if os.path.exists(file_csv):
    flights = Flights(file_csv)
else:
    print(f"The file with name {file_csv} not found.")
    sys.exit(21)

"""In order to start a web server."""
app = Flask(__name__)


@app.route('/flights/<int:id_>', methods = ['GET'])
def get_flight(id_):
    flight_id = flights.search(id_)
    if flight_id is None:
        abort(404) 
    return flight_id


@app.errorhandler(404)
def id_not_found(error):
    return jsonify(
        message="The given flight Id not found.",
        category="error",
        status=404
    ), 404


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)
