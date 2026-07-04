create database prime;
use prime;

create table user (
 id int primary key,
 age int,
 name varchar(30) not null,
 email varchar(50) unique,
 follower int default 0, 
 following int default 0,
 constraint check (age >= 13)
 );
 
 create table post(
  id int primary key,
  content varchar(50),
  user_id int ,
  foreign key (user_id) references user(id)
 );
 
 
 insert into user 
 (id,age,name,email,follower,following)
 values
 (1,32,"kalpesh","kp32@gmail.com",32,23),
 (2,23,"jenish"," jb42@gmail.com",443,34),
 (3,42,"hardev","hf328@gmail.com",43,43),
 (4,43,"kuldip","kuldip42@gmail.com",53,53);
 
 select * from user;
 
 delete from user 
 where age = 43;
 
update user 
set follower  = 600
where age = 32;


set sql_safe_updates = 0;

use college;

create table teacher_to_store(
id int primary key,
name varchar (30) unique,
subject varchar(30) default "math",
salary int default 10000 not null
);

insert into teacher_to_store values
(23, "ajay", "math", 50000),

(47, "bharat", "english", 60000),

(18, "chetan", "chemistry", 45000),

(9, "divya", "physics", 75000);

select *from teacher_to_store;


select * from teacher_to_store
where salary > 55000;



alter table teacher_to_store 
change column salary ctc int not null;


update  teacher_to_store
set ctc = ctc * 0.25;


alter table teacher_to_store
add column city varchar(50) default "gurgaon";


alter table teacher_to_store 
drop column ctc;



create table student(
roll_no int primary key,
name varchar (30) not null,
city varchar(50) default "home",
marks int 
);



insert into student values

(110, "adam", "Delhi", 76),

(108, "bob", "Mumbai", 65),

(124, "casey", "Pune", 94),

(112, "duke", "Pune", 80);


select * from student ;







select max(marks) from student
group by city;


select distinct city from student;


select avg(marks) from student;

update student set grade = "o"
where marks >= 80;


update student set grade = "a"
where marks >= 70  and marks < 80;


update student set grade = "b"
where marks >= 60 and marks < 70;

alter table student 
add column grade varchar(3);


select * from student;