from json import JSONEncoder,  loads
import re
from xml.etree.ElementTree import tostring
from pysondb import db
from flask import request, Flask, jsonify
app = Flask(__name__)
a = db.getDb("static/db.json")
authToken = 'gh8j33m002mhxfOl2Hg094jNhFF0sw'

@app.route('/', methods=['GET'])
def get():
    if(request.args.get("auth") == authToken):
        return jsonify(a.getAll())
    else:
        return "<h1 style=\"color:red\">ERROR: not authenticated</h1>"

@app.route('/', methods=['PUT'])
def put():
    if(request.args.get("auth") == authToken):
        a.deleteAll()
        #loads(a.getAll)[""][0].pop()
        a.addMany(request.json)
        request.json[0].pop("id")
        a.deleteAll()
        a.addMany(request.json)
        return jsonify(request.json)
    else:
        return "<h1 style=\"color:red\">ERROR: not authenticated</h1>"

@app.route('/', methods=['DELETE'])
def delete():
    if(request.args.get("auth") == authToken):
        a.deleteAll()
        return jsonify(a.getAll())
    else:
        return "<h1 style=\"color:red\">ERROR: not authenticated</h1>"

if "__name__" == "__main__":
    app.run(debug=True)