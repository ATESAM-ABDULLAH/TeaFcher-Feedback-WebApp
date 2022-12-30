----                    TABLES
CREATE TABLE USERS
(
    u_id NUMBER,
    NAME VARCHAR2(50),
    email VARCHAR2(100),
    PASSWORD VARCHAR2(4),
    TYPE VARCHAR2(10),
    CONSTRAINT users_p_key PRIMARY KEY (u_id),
    CONSTRAINT users_email UNIQUE (email)
);
CREATE TABLE student
(
    s_id NUMBER,
    regno NUMBER,
    CONSTRAINT student_p_key PRIMARY KEY (s_id),
    CONSTRAINT student_f_key FOREIGN KEY (s_id) REFERENCES USERS(u_id),
    CONSTRAINT student_reg UNIQUE (regno)
);
CREATE TABLE faculty
(
    f_id NUMBER,
    course VARCHAR2(6),
    CONSTRAINT faculty_p_key PRIMARY KEY (f_id),
    CONSTRAINT faculty_f_key FOREIGN KEY (f_id) REFERENCES USERS(u_id),
    CONSTRAINT faculty_course UNIQUE (course)
);
CREATE TABLE FEEDBACK
(
    s_id NUMBER,
    f_id NUMBER,
    q1 NUMBER,
    q2 NUMBER,
    q3 NUMBER,
    q4 NUMBER,
    q5 NUMBER,
    q6 NUMBER,
    q7 NUMBER,
    q8 NUMBER,
    q9 NUMBER,
    q10 NUMBER,
    q11 NUMBER,
    rating NUMBER,
    comments VARCHAR2(500),
    CONSTRAINT feedback_p_key PRIMARY KEY (s_id,f_id),
    CONSTRAINT feedback_f_key1 FOREIGN KEY (s_id) REFERENCES USERS(u_id),
    CONSTRAINT feedback_f_key2 FOREIGN KEY (f_id) REFERENCES USERS(u_id)
);
CREATE TABLE average
(
    f_id NUMBER,
    q1 NUMBER,
    q2 NUMBER,
    q3 NUMBER,
    q4 NUMBER,
    q5 NUMBER,
    q6 NUMBER,
    q7 NUMBER,
    q8 NUMBER,
    q9 NUMBER,
    q10 NUMBER,
    q11 NUMBER,
    rating NUMBER,
    CONSTRAINT average_p_key PRIMARY KEY (f_id),
    CONSTRAINT average_f_key FOREIGN KEY (f_id) REFERENCES USERS(u_id)
);

----                    DUMMY DATA
INSERT ALL --users
    --admin
    INTO USERS VALUES(0,'admin','admin@giki.edu.pk','0000','admin')--builtin 
    
    --faculty
    INTO USERS VALUES(1,'Tom','tom@giki.com','1234','faculty')
    INTO FACULTY VALUES(1,'CS 232')
    INTO USERS VALUES(2,'Holland','holland@giki.com','1234','faculty')
    INTO FACULTY VALUES(2,'CS 221')
    INTO USERS VALUES(3,'Batman','batman@giki.com','1234','faculty')
    INTO FACULTY VALUES(3,'MT 201')
    
    --students
    INTO USERS VALUES(4,'Moosa','moosa@giki','1111','student')
    INTO STUDENT VALUES(4,2021421)
    INTO USERS VALUES(5,'Ahmed','ahmed@giki.com','1111','student')
    INTO STUDENT VALUES(5,2021123)
    INTO USERS VALUES(6,'Atesam','atesam@giki.com','1111','student')
    INTO STUDENT VALUES(6,2021114)
    INTO USERS VALUES(7,'Hamza','hamza@giki.com','1111','student')
    INTO STUDENT VALUES(7,2021197)
    INTO USERS VALUES(8,'Zulfiqar','zulfiqar@giki.com','1111','student')
    INTO STUDENT VALUES(8,2021442)
    INTO USERS VALUES(9,'Qari sahab','qari@giki.com','1111','student')
    INTO STUDENT VALUES(9,2021198)
SELECT 1 FROM DUAL;

INSERT ALL --feedback (s_id,f_id,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,rating,comments) 
    --moosa 4
    INTO FEEDBACK VALUES(4,1,3,4,5,1,2,3,4,5,1,2,3,6,'OK')
    INTO FEEDBACK VALUES(4,2,2,4,5,1,2,1,4,1,1,2,3,3,'OK')
    INTO FEEDBACK VALUES(4,3,5,5,5,1,2,3,5,5,1,2,3,9,'Good')
    
    --ahmed 5
    INTO FEEDBACK VALUES(5,1,3,4,5,1,2,3,4,5,1,2,3,6,'OK')
    INTO FEEDBACK VALUES(5,2,2,4,1,5,2,1,5,1,2,2,4,3,'OK')
    INTO FEEDBACK VALUES(5,3,5,5,5,1,2,3,5,5,1,2,3,6,'Good')
    
    --atesam 6
    INTO FEEDBACK VALUES(6,1,3,4,5,1,2,3,4,5,1,2,3,6,'OK')
    INTO FEEDBACK VALUES(6,2,2,4,5,1,2,1,4,1,1,2,3,3,'OK')
    INTO FEEDBACK VALUES(6,3,5,5,5,1,2,3,5,5,1,2,3,9,'Good')
    
    --hamza 7
    INTO FEEDBACK VALUES(7,1,3,4,5,1,2,3,4,5,1,2,3,6,'OK')
    INTO FEEDBACK VALUES(7,2,2,4,5,1,2,1,4,1,1,2,3,3,'OK')
    
    --zulfiqar 8
    INTO FEEDBACK VALUES(8,2,5,5,5,1,2,3,5,5,1,2,3,9,'Good')
    INTO FEEDBACK VALUES(8,1,3,4,5,1,2,3,4,5,1,2,3,6,'OK')
    
    --qari sahab 9
    INTO FEEDBACK VALUES(9,3,2,4,5,1,2,1,4,1,1,2,3,3,'OK')
    INTO FEEDBACK VALUES(9,2,5,5,5,1,2,3,5,5,1,2,3,9,'Good')
SELECT 1 FROM DUAL;

----                    View data
--view no of users by type
SELECT TYPE ,COUNT(*) AS no_users FROM USERS 
GROUP BY TYPE;

--View all users
select name,email,password,regno,type from users
left join student on s_id = u_id
--left join faculty on f_id = u_id
order by u_id;



