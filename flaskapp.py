# Imports
import db #File with database config

from flask import Flask, render_template, url_for, request, redirect
from flask import session as student_data, session as faculty_data ,session as admin_data

from sqlalchemy.orm import sessionmaker
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
                course=dbsession.query(db.feedback.course).filter(db.feedback.s_id == id)#.filter(db.feedback.s_id == id)
                course=[x for x in course]
                course = list(map(''.join,course)) 
                ## fetch regno of student
                regno= dbsession.query(db.student.regno).filter(db.student.s_id == id)
                regno=regno[0].regno
                ##pass data into session
                student_data['id']=id
                student_data['name']=name
                student_data['regno']=regno
                student_data['course']=course
                ##redirect to student view
                return redirect('/student')

            if (type =='faculty') :
                ## fetch course of teacher
                course =dbsession.query(db.faculty).filter(db.faculty.f_id == id)
                course=course[0].course
                ##pass data into session
                faculty_data['id']=id
                faculty_data['name']=name
                faculty_data['course']=course
                ##redirect to faculty view
                return redirect('/faculty')

            if(type =='admin'):
                ## pass in list of distinct courses
                course=dbsession.query(db.feedback.course).distinct()#distinct courses
                course=[x for x in course] #convert to tuple list
                course=list(map(''.join,course)) #convert to normal list
                ##pass data into session
                admin_data['id']=id
                admin_data['name']=name
                admin_data['email']=email
                admin_data['course']=course
                ##redirect to admin view
                return redirect('/admin')

            dbsession.commit()
        else:
            return redirect('/logout')

    else: #if viewing page
        return render_template('login.html')

#DONE
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
        return redirect("/logout")
    else: #if viewing page
        return render_template('signup.html')

# DONE
@app.route("/student",methods=["GET","POST"])
def student():
    ##fetch data from session
    id=student_data['id']
    name=student_data['name']
    regno=student_data['regno']

    print(request.form)

    if (request.method =='POST'):
        #get info from form
        course=request.form.get('course-no')
        q1=request.form.get('q1')
        q2=request.form.get('q2')
        q3=request.form.get('q3')
        q4=request.form.get('q4')
        q5=request.form.get('q5')
        q6=request.form.get('q6')
        q7=request.form.get('q7')
        q8=request.form.get('q8')
        q9=request.form.get('q9')
        q10=request.form.get('q10')
        q11=request.form.get('q11')
        rating=request.form.get('rating')
        comment=request.form.get('comment')
        
        #make db session
        session=sessionmaker(bind=db.engine)
        dbsession=session()

        #get f_id for course
        f_id=dbsession.query(db.faculty.f_id).filter(db.faculty.course == course)
        f_id=[x for x in f_id]
        f_id=f_id[0][0]

        #check if user is in feedback
        x=dbsession.query(db.feedback).filter(db.feedback.s_id==id , db.feedback.f_id==f_id)
        x=[x for x in x]

        if(x):#if exists
            dbsession.query(db.feedback).filter(db.feedback.s_id==id, db.feedback.f_id==f_id \
                ,db.feedback.course == course)\
                .update({'q1':q1,'q2':q2,'q3':q3,'q4':q4,'q5':q5,'q6':q6,'q7':q7,'q8':q8\
                    ,'q9':q9,'q10':q10,'q11':q11,'rating':rating,'comment':comment})
            
        dbsession.commit()

        return redirect('/logout')
    else:#if viewing page only
        return render_template('feedback.html',name=name,regno=regno,course=course)

# DONE
@app.route("/faculty",methods=["GET","POST"])
def faculty():

    ##fetch data from session
    id=faculty_data['id']
    name=faculty_data['name']
    course=faculty_data['course']

    print(request.form)

    if(request.method == 'POST'):#form submitted
        #get info from form
        std1=request.form.get('std-1')
        std2=request.form.get('std-2')
        std3=request.form.get('std-3')
        std4=request.form.get('std-4')
        std5=request.form.get('std-5')
        std6=request.form.get('std-6')
        std7=request.form.get('std-7')
        std8=request.form.get('std-8')
        std9=request.form.get('std-9')
        std10=request.form.get('std-10')

        list_students=[std1,std2,std3,std4,std5,std6,std7,std8,std9,std10]#used for looping over

        #make db session
        session=sessionmaker(bind=db.engine)
        dbsession=session()

        #if (s_id,f_id) pair not in table ->add
        #else : ignore

        for regno in list_students:
            if(regno != ''):#record not empty
                
                try:
                    #find s_id for reg -> already signedup
                    s_id=dbsession.query(db.student.s_id).filter(db.student.regno == regno)
                    s_id=[x for x in s_id]#turn into list of tuples
                    s_id=s_id[0][0]#unpack tuple

                    #check if s_id,f_id pair exists
                    x = dbsession.query(db.feedback).filter(db.feedback.s_id == s_id , db.feedback.f_id == id)
                    x=[x for x in x]#turn into list

                    if(not x):#not exists
                        print(regno,s_id,id,course)
                        tr=db.feedback(s_id,id,course)
                        dbsession.add(tr)
                except:
                    continue

        dbsession.commit()
        return redirect('/logout')
    else:#viewing html page
        return render_template('control.html',name=name,course=course)

#add function to pull data from averages
@app.route("/admin",methods=["GET","POST"])
def admin():
    print(request.form)
    ## fetch data from session
    id=admin_data['id']
    name=admin_data['name']
    email=admin_data['email']
    course=admin_data['course']
    ##render html
    return render_template('view.html',name=name,email=email,course=course)

#-----------------------------------------------------------------------------------------------------

@app.route("/logout")
def logout():
    #clear sessions
    student_data.clear()
    faculty_data.clear()
    admin_data.clear()
    return redirect("/login")#redirect to login

# -----------------------------------------------------------------------------------------

# Run using python instead of flask
if(__name__ == '__main__'):
    app.run(debug=True)