import json
from unittest import result
from flask import Flask, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/dbtestmongo"

#connector
mongo = PyMongo(app)

@app.route('/')
def index():
    online_users =  mongo.db.user.find({"username": "Mary"})
    output = []
    for s in online_users:
        output.append({'User Name' : s['username']})
    return jsonify({'result' : output})


if __name__ == "__main__":
    app.run(debug=True)
