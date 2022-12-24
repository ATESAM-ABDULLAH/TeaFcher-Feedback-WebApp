# Imports
# import db #File with database config

from flask import Flask, render_template, url_for, request, redirect, session

# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import random
#-------------------------------------------------------------------------------------------------------

# main app 
app=Flask(__name__)
app.secret_key="hello"

# Routes to diff pages
@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'POST': #if form is submitted

        session['email']=request.form.get('email')
        session['password']=request.form.get('password')
        session['type']=request.form.get('type')

        return redirect(url_for('valid_login'))#redirect to validation func

    else: #if viewing page
        if 'email' in session:#session still going
            return redirect(url_for('valid_login'))#redirect to validation func

        return render_template('login.html')

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == 'POST': #if form is submitted

        session['email']=request.form.get('email')
        session['password']=request.form.get('password')
        session['type']=request.form.get('type')

        return redirect(url_for('valid_signup'))#redirect to validation func

    else: #if viewing page
        if 'email' in session:#session still going
            return redirect(url_for('valid_signup'))#redirect to validation func

        return render_template('signup.html')

@app.route("/student",methods=["GET","POST"])
def student():
    print(request.form)
    return render_template('feedback.html')

@app.route("/faculty",methods=["GET","POST"])
def faculty():
    print(request.form)
    return render_template('control.html')

@app.route("/admin",methods=["GET","POST"])
def admin():
    print(request.form)
    return render_template('view.html')

#-----------------------------------------------------------------------------------------------------
@app.route("/valid-login")
def valid_login():
    if 'email' in session:

        # use db auth here
        valid = True # make sure user is valid

        email=session['email']
        password=session['password']
        type=session['type']

        # redirect to 
        if(type =='student' and valid):
            return redirect('/student')
        if (type =='faculty' and valid) :
            return redirect('/faculty')
        if(type =='admin' and valid):
            return redirect('/admin')

        # if no page works / is down
        return f"{email} , {password} , {type}"

    else:
        return redirect("/login")

@app.route("/valid-signup")
def valid_signup():
    if 'email' in session:

        # use db auth here
        valid = True # make sure user is valid

        email=session['email']
        password=session['password']
        type=session['type']


        # if no page works / is down
        return redirect("/login")

    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()#clear session
    return redirect("/login")#redirect to login
# -----------------------------------------------------------------------------------------

# Run using python instead of flask
if(__name__ == '__main__'):
    app.run(debug=True)