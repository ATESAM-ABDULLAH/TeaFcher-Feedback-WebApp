--Check if user is signedin
select * from users where email='admin@giki.edu.pk' and password='0000' and type='admin' ;

--list of courses student enrolled in
select course from feedback 
inner join faculty on faculty.f_id=feedback.f_id
where s_id = 5;

--regno of student
select regno from student where s_id=5;

--fetch course taught by teacher
select course from faculty where f_id=2;

--distinct courses in feedback
select distinct course from feedback
inner join faculty on faculty.f_id=feedback.f_id;

--get f_id for a course
select f_id from faculty where course ='MT 201';

--check if student has been granted access
select case 
            when exists (select * from feedback where s_id = 5 and f_id = 2) 
            then 'Yes' 
            else 'No' 
        end 
from dual;

--update feedbcak b/c s_id,f_id were already inserted
update feedback set q1=5,q2=3,q3=5,q4=3,q5=5,q6=3,q7=5,q8=3,q9=5,q10=3,q11=5,rating=3,comments='Good' 
where s_id=5 and f_id=2;

----register student if not registered
--find s_id from reg
select s_id from student where regno =2021114;
--check if student has been granted access
select * from feedback where s_id = 5 and f_id = 2;
--insert if not prsent
insert into feedback(s_id,f_id) values(5,2);



----Function to update course average
create or replace procedure update_average(Tcourse faculty.course%type) 
AS    
    Tf_id faculty.f_id%type;
    temp number;
    
    Tq1 number:=0;
    Tq2 number:=0;
    Tq3 number:=0;
    Tq4 number:=0;
    Tq5 number:=0;
    Tq6 number:=0;
    Tq7 number:=0;
    Tq8 number:=0;
    Tq9 number:=0;
    Tq10 number:=0;
    Tq11 number:=0;
    Trating number:=0;
BEGIN
    --find f_id for course
    select f_id into Tf_id from faculty where course = Tcourse;
    
    --find averages for course
    select avg(q1),avg(q2),avg(q3),avg(q4),avg(q5),avg(q6),avg(q7),avg(q8),avg(q9),avg(q10),avg(q11),avg(rating)
    into Tq1,Tq2,Tq3,Tq4,Tq5,Tq6,Tq7,Tq8,Tq9,Tq10,Tq11,Trating 
    from feedback 
    where f_id = Tf_id;
    
    --check if f_id/course already in 
    select case 
            when exists (select 1 
                         from average
                         where f_id = Tf_id) 
            then 1 
            else 0
            end into temp
    from dual;
    
    --if not exist create record
    if(temp=0) then
        insert into average(f_id) values(Tf_id);
    end if;
    
    --update average table
    update average 
    set q1=Tq1,q2=Tq2,q3=Tq3,q4=Tq4,q5=Tq5,q6=Tq6,q7=Tq7,q8=Tq8,q9=Tq9,q10=Tq10,q11=Tq11,rating=Trating
    where f_id=Tf_id;
    
END;
/

--Call update_average when admin requests data
begin
    update_average('CS 221');
end;
/

--fetch average from table to show admin
create view admin_view as (select * from average where f_id=3);
