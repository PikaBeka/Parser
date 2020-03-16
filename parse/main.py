import flask
import json
from flask import request, jsonify
from packages import AkmolaParse

data = AkmolaParse()

for p in data:
    print(p)
    print('\n')


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>CoronoVirus parsed data access:</h1><ul><li><a href="+"http://localhost:5000/akmola"+">Akmola city</a><br></li></ul>"


@app.route('/akmola', methods=['GET'])
def akmola():
    return jsonify(data)


app.run()