from flask import Flask, render_template
from flask_pymongo import PyMongo
from personal import User

app = Flask(__name__)

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/dbtestmongo"
#connector
mongo = PyMongo(app)
db = mongo.db


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload')
def index():
    return User().upload()

@app.route('/medicaldetails')
def medicaldetails():
    return render_template('medicaldetails.html')
    
@app.route('/medicalhistory')
def medicalhistory():
    return render_template('medicalhistory.html')
