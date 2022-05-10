from flask import request, url_for, jsonify
from app import db, mongo, app
from unicodedata import name
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbtestmongo'
mongo = PyMongo(app)



todos = mongo.db.todos

@app.route('/')
def index():
    saved_todos = todos.find()
    return render_template('index.html', todos=saved_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    username = request.form.get('username')
    name = request.form.get('name')
    dob = request.form.get('dob')
    address = request.form.get('address')
    mobile = request.form.get('mobile')
    gender = request.form.get('gender')
    todos.insert_one({'text' : username, 'complete' : False})
    todos.insert_one({'text' : name, 'complete' : False})
    todos.insert_one({'text' : dob, 'complete' : False})
    todos.insert_one({'text' : address, 'complete' : False})
    todos.insert_one({'text' : mobile, 'complete' : False})
    todos.insert_one({'text' : gender, 'complete' : False})
    return redirect(url_for('index'))

@app.route('/complete/<oid>')
def complete(oid):
    todo_item = todos.find_one({'_id': ObjectId(oid)})
    todo_item['complete'] = True
    todos.save(todo_item)
    return redirect(url_for('index'))

@app.route('/delete_completed')
def delete_completed():
    todos.delete_many({'complete' : True})
    return redirect(url_for('index'))

@app.route('/delete_all')
def delete_all():
    todos.delete_many({})
    return redirect(url_for('index'))




<!--class User:
  def upload():
    
    return '''
    <form method = 'POST' action="/create" enctype="multipart/form-data">
      <input type= "text" name = "username" placeholder="Username"><br>
      <input type= "text" name = "name" placeholder="Name"><br>
      <input type= "text" name = "dob" placeholder="DOB"><br>
      <input type= "text" name = "address" placeholder="Address"><br>
      <input type= "number" name = "mobile" placeholder="Mobile"><br>
      <input type= "text" name = "gender" placeholder="Gender"><br>
      <input type= "file" name = "lab_test" placeholder="Upload"><br>
      <input type= "submit">
      </form>
      '''

  @app.route('/create',methods=['POST'])
  def create():
    #db = pymongo.MongoClient("localhost:27017")
    if 'lab_test' in request.files:
        lab_test = request.files['lab_test']
        mongo.save_file(lab_test.filename,lab_test)
        mongo.db.user.insert_one({'username' : request.form.get('username'),'name' : request.form.get('name'),'dob' : request.form.get('dob'),'address' : request.form.get('address'),'mobile' : request.form.get('mobile'),'gender' : request.form.get('gender'), 'lab_test_name' : lab_test.filename})
    return 'done'
    
  @app.route('/file/<filename>')
  def file(filename):
    return mongo.send_file(filename)

  @app.route('/profile/<username>')
  def profile(username):
    user= mongo.db.user.find_one({'username': username})
    return jsonify(user)
    return f'''
    <h1>{username}</h1>
    <h1>{user.name}</h1>
    <img src ="{url_for('file',filename = user['lab_test_name'])}">
    '''
-->
