import json
from unittest import result
from flask import Flask, jsonify, request, url_for
from flask_pymongo import PyMongo
import pymongo


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/dbtestmongo"
#connector
mongo = PyMongo(app)
db = mongo.db


@app.route('/login')
def login():
    return render_template('login.html')
