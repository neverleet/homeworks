-- SQL-команды для создания таблиц
CREATE TABLE customers
(
customer_id varchar(10) PRIMARY KEY,
company_name varchar (100),
contact_name varchar (50)
);

CREATE TABLE employees
(
employee_id int PRIMARY KEY,
first_name varchar (20),
last_name varchar (20),
title varchar (50),
birth_date date,
notes text
);

CREATE TABLE orders
(
order_id int,
customer_id varchar(10),
employee_id int,
order_date date,
ship_city varchar (40)
);