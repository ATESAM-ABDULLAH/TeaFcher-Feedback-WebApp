----TABLES

create table users(
    u_id number,
    name varchar2(50),
    email varchar2(100),
    password varchar2(4),
    type varchar2(10),
    constraint users_p_key primary key (u_id),
    constraint users_email unique (email)
);
create table students(
    s_id number,
    regno number(7),
    constraint student_p_key primary key (s_id),
    constraint student_regno unique (regno)
);
create table faculty(
    f_id number,
    course varchar(10),
    constraint faculty_p_key primary key (f_id),
    constraint course_course unique (course)
);
create table feedback(
    s_id number,
    f_id number,
    q1 number(1),
    q2 number(1),
    q3 number(1),
    q4 number(1),
    q5 number(1), 
    q6 number(1),
    q7 number(1),
    q8 number(1),
    q9 number(1),
    q10 number(1),
    q11 number(1),
    rating number(1),
    comments number(1),
    constraint feedback_p_key primary key (s_id,f_id)
);
create table average(
    f_id number,
    q1 number(1),
    q2 number(1),
    q3 number(1),
    q4 number(1),
    q5 number(1), 
    q6 number(1),
    q7 number(1),
    q8 number(1),
    q9 number(1),
    q10 number(1),
    q11 number(1),
    rating number(1),
    constraint average_p_key primary key (f_id)
);





