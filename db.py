# Contains all table ORM + engine to sqlite

# Local sqlite DB
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import PrimaryKeyConstraint

engine = create_engine('sqlite:///database.sqlite',echo=True)

base = declarative_base()

# Tables for login/signup
class user(base):
    __tablename__='user'
    u_id=Column(Integer,primary_key=True)
    name=Column(String(50))
    email=Column(String(100))
    password=Column(String(4))
    type=Column(String(10))

    def __init__(self,u_id,name,email,password,type):
        self.u_id=u_id
        self.name=name
        self.email=email
        self.password=password
        self.type=type

class student(base):
    __tablename__='student'
    s_id=Column(Integer,primary_key=True)
    regno=Column(Integer)

    def __init__(self,s_id,regno):
        self.s_id=s_id
        self.regno=regno

class faculty(base):
    __tablename__='faculty'
    f_id=Column(Integer,primary_key=True)
    course=Column(String(6))

    def __init__(self,f_id,course):
        self.f_id=f_id
        self.course=course

# Table for feedback
class feedback(base):
    __tablename__="feedback"

    u_id=Column(Integer)
    f_id=Column(Integer)
    course=Column(String(6))
    q1=Column(Integer)
    q2=Column(Integer)
    q3=Column(Integer)
    q4=Column(Integer)
    q5=Column(Integer)
    q6=Column(Integer)
    q7=Column(Integer)
    q8=Column(Integer)
    q9=Column(Integer)
    q10=Column(Integer)
    q11=Column(Integer)
    rating=Column(Integer)
    comment=Column(String(500))

    __table_args__=(PrimaryKeyConstraint(u_id,f_id),{})

    def __init__(self,u_id,f_id,course,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,rating,comment):
        self.u_id=u_id
        self.f_id=f_id
        self.course=course
        self.q1=q1
        self.q2=q2
        self.q3=q3
        self.q4=q4
        self.q5=q5
        self.q6=q6
        self.q7=q7
        self.q8=q8
        self.q9=q9
        self.q10=q10
        self.q11=q11
        self.rating=rating
        self.comment=comment

# Table for averages
class average(base):
    __tablename__="average"

    f_id=Column(Integer,primary_key=True)
    q1=Column(Integer)
    q2=Column(Integer)
    q3=Column(Integer)
    q4=Column(Integer)
    q5=Column(Integer)
    q6=Column(Integer)
    q7=Column(Integer)
    q8=Column(Integer)
    q9=Column(Integer)
    q10=Column(Integer)
    q11=Column(Integer)
    rating=Column(Integer)
    def __init__(self,f_id,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,rating):
        self.f_id=f_id
        self.q1=q1
        self.q2=q2
        self.q3=q3
        self.q4=q4
        self.q5=q5
        self.q6=q6
        self.q7=q7
        self.q8=q8
        self.q9=q9
        self.q10=q10
        self.q11=q11
        self.rating=rating

# Session to enter data into DB

# Session=sessionmaker(bind=engine)
# session=Session()

# # Print all users
# for x in session.query(user).all():
#     print(x.name,x.email)

## Add admin user
# tr=user(0,'admin','admin@giki.edu.pk','0000','admin')

# session.add(tr)
# session.commit()

base.metadata.create_all(engine)

