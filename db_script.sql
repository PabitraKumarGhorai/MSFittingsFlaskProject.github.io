create database ms_database;
use ms_database;

create table order_details
(
	Client_code varchar(50) not null primary key,
    Client_name varchar(90) not null,
    Consignee varchar(100) not null,
    Order_quantity int(60) not null,
    Order_status varchar(10) not null,
    Order_date varchar(20) not null
    
);

insert into order_details 
(Client_code, Client_name, Consignee, Order_quantity, Order_status, Order_date)
value
('T001','Test_Client','Test_add',5,'Test_yes','dd-mm-yyyy');

select * from order_details;
