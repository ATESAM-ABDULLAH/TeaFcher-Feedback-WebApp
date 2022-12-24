# Shifted to sqlite

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.sqlite',echo=True)

base = declarative_base()

# Tables for login/signup
class user(base):
    __tablename__='user'
    u_id=Column(Integer,primary_key=True)
    name=Column(String(50))
    email=Column(String(100))
    password=Column(String(4))

    def __init__(self,u_id,name,email,password):
        self.u_id=u_id
        self.name=name
        self.email=email
        self.password=password

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
    

base.metadata.create_all(engine)
