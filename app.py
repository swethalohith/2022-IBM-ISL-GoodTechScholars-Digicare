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
@app.route('/')
def index():
    return '''
    <form method = 'POST' action="/create" enctype="multipart/form-data">
      <input type= "text" name = "username">
      <input type= "file" name = "lab_test">
      <input type= "submit">
      </form>
      '''
    
@app.route('/create',methods=['POST'])
def create():
    #db = pymongo.MongoClient("localhost:27017")
    if 'lab_test' in request.files:
        lab_test = request.files['lab_test']
        mongo.save_file(lab_test.filename,lab_test)
        mongo.db.user.insert_one({'username' : request.form.get('username'), 'lab_test_name' : lab_test.filename})


        

    return 'done'
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/profile/<username>')
def profile(username):
    user= mongo.db.users.find_one_or_404({'username': username})
    return f'''
    <h1>{username}</h1>
    <img src ="{url_for('file',filename =user['lab_test_name'])}>'''
