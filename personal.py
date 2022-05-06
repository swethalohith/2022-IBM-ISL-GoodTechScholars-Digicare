from flask import request, url_for
from flask_pymongo import PyMongo
import pymongo
from app import app


@app.route('/')
def index():
    #return render_template('index.html')
    
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
    return f'''
    <h1>{username}</h1>
    <h1>{user.name}</h1>
    <img src ="{url_for('file',filename = user['lab_test_name'])}">
    '''
