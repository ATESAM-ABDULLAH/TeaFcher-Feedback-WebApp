# Imports
import db #File with database config

from flask import Flask , render_template , url_for , request 

# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
#-------------------------------------------------------------------------------------------------------

# main app 
app=Flask(__name__)

# Routes to diff pages
@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    print(request.form)
    return render_template('login.html')

@app.route("/signup",methods=["GET","POST"])
def signup():
    print(request.form)
    return render_template('signup.html')

@app.route("/student",methods=["GET","POST"])
def student():
    print(request.form)
    return render_template('feedback.html')

@app.route("/faculty",methods=["GET","POST"])
def teacher():
    print(request.form)
    return render_template('control.html')

@app.route("/admin",methods=["GET","POST"])
def faculty():
    print(request.form)
    return render_template('view.html')

@app.route("/valid",methods=["GET","POST"])
def valid():

    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')
    type=request.form.get('type')
    course=request.form.get('course')
    regno=request.form.get('regno')

    Session=sessionmaker(bind=db.engine)
    session=Session()

    tr=db.user()
    
    if (type=='student') :

    


# Run using python instead of flask
if(__name__ == '__main__'):
    app.run(debug=True)