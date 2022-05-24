from pysondb import db
from flask import request, Flask, jsonify
app = Flask(__name__)
a = db.getDb("db")

@app.route('/', methods=['GET'])
def get():
    return jsonify(a.getAll())

@app.route('/', methods=['PUT'])
def put():
    a.deleteAll()
    a.addMany(request.json)
    return jsonify(a.getAll())

@app.route('/', methods=['DELETE'])
def delete():
    a.deleteAll()
    return jsonify(a.getAll())

app.run(debug=True)