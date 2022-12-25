# Imports
import db #File with database config

from flask import Flask, render_template, url_for, request, redirect
from flask import session , session as session2 

from sqlalchemy.orm import sessionmaker
import oracledb
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

        session2['name']=request.form.get('name')
        session2['email']=request.form.get('email')
        session2['password']=request.form.get('password')
        session2['type']=request.form.get('type') #can be student/teacher
        session2['course']=request.form.get('course')
        session2['regno']=request.form.get('regno')

        return redirect(url_for('valid_signup'))#redirect to validation func

    else: #if viewing page
        if 'email' in session2:#session still going
            return redirect(url_for('valid_signup'))#redirect to validation func

        return render_template('signup.html')
2
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
        if(not valid):
            return redirect("/login")
        # if no page works / is down
        return f"{email} , {password} , {type}"

    else:
        return redirect("/login")

@app.route("/valid-signup")
def valid_signup():
    if 'email' in session:#data is submitted from signup
        
        valid =False
        id=random.randint(1,1000)
        name=session2['name']
        email=session2['email']
        password=session2['password']
        type=session2['type']
        course=session2['course']
        regno=session2['regno']
        
        # if (not valid):
            # return redirect('/signup')

        # insert into db
        Session=sessionmaker(bind=db.engine)
        dbsession=Session()

        tr1=db.user(id,name,email,password,type)

        if(type=='student'):
            tr2=db.student(id,regno)
        elif(type=='faculty'):
            tr2=db.faculty(id,course)
        

        dbsession.add_all({tr1,tr2})
        dbsession.commit()
        
        # if no page works / is down
        return redirect("/login")

    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    #clear session
    session.clear()
    session2.clear()
    return redirect("/login")#redirect to login
# -----------------------------------------------------------------------------------------

# Run using python instead of flask
if(__name__ == '__main__'):
    app.run(debug=True)