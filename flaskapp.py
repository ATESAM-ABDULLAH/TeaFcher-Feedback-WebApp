# Imports
import db #File with database config

from flask import Flask, render_template, url_for, request, redirect ,flash
# from flask import session , session as session2 

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random
#-------------------------------------------------------------------------------------------------------

# main app 
app=Flask(__name__)
app.secret_key="hello" #used to encrypt sessions



# Routes to diff pages
@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'POST': #if form is submitted

        email=request.form.get('email')
        password=request.form.get('password')
        type=request.form.get('type')

        session =sessionmaker(bind=db.engine)
        dbsession=session()

        res =dbsession.query(db.user).filter(db.user.email==email ,db.user.password==password,db.user.type==type)
        x=[x for x in res]

        if(x):#if user valid
            name =x[0].name #user name
            id=x[0].u_id    #user id

            if(type =='student'):
                ## fetch list of enrolled courses from feedback table
                course=[] 
                ## fetch regno of student
                regno= dbsession.query(db.student.regno).filter(db.student.s_id == id)
                regno=regno[0].regno
                return render_template('feedback.html',name=name,regno=regno)

            if (type =='faculty') :
                ## fetch course of teacher
                course =dbsession.query(db.faculty).filter(db.faculty.f_id == id)
                course=course[0].course
                return render_template('control.html',name=name,course=course)

            if(type =='admin'):
                ## pass in list of distinct courses
                course=dbsession.query(db.faculty.course).distinct()#distinct courses
                course=[x for x in course] #convert to tuple list
                course=list(map(''.join,course)) #convert to normal list

                return render_template('view.html',name=name,email=email,course=course)
            
            dbsession.commit()#end session
        else:
            return redirect("/login")

    else: #if viewing page
        return render_template('login.html')

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == 'POST': #if form is submitted

        id=random.randint(1,1000)
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        type=request.form.get('type') #can be student/teacher
        course=request.form.get('course')
        regno=request.form.get('regno')

        session=sessionmaker(bind=db.engine)
        dbsession =session()

        res =dbsession.query(db.user).filter(db.user.email==email)
        x=[x for x in res]

        if(x):#already exists
            return redirect('/signup')
        else:
            #Super class
            tr1=db.user(id,name,email,password,type)
            
            #child classes
            if(type=='student'):
                tr2=db.student(id,regno)
            elif(type=='faculty'):
                tr2=db.faculty(id,course)

            dbsession.add_all({tr1,tr2})
            dbsession.commit()
        return redirect("/login")
    else: #if viewing page
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

@app.route("/logout")
def logout():
    #clear sessions
    # session.clear()
    # session2.clear()
    return redirect("/login")#redirect to login

# -----------------------------------------------------------------------------------------

# Run using python instead of flask
if(__name__ == '__main__'):
    app.run(debug=True)