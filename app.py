from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/medicaldetails')
def medicaldetails():
    return render_template('medicaldetails.html')
    
@app.route('/medicalhistory')
def medicalhistory():
    return render_template('medicalhistory.html')
