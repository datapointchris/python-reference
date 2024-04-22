drop table orders;
drop table transactions;
drop table returns;
drop table customers;
drop table vendors;
drop table orders;

create table if not exists customers(
	customer_id int primary key not null,
	customer_email varchar(255),
	customer_name varchar(255),
	segment varchar(255),
	country varchar(255),
	city varchar(255),
	state varchar(255),
	postal_code int,
	region varchar(255)
);

create table if not exists vendors(
	vendor_id varchar(255) primary key,
	vendor_name varchar(255)
);

create table if not exists orders(
	order_id int primary key,
	customer_id int,
 	foreign key(customer_id) references customers(customer_id),
	vendor_id varchar(255),
	foreign key(vendor_id) references vendors(vendor_id),
	ship_mode varchar(255),
	order_status varchar(255),
	order_purchase_date timestamp,
	order_approved_at timestamp,
	order_delivered_carrier_date timestamp,
	order_delivered_customer_date timestamp,
	order_estimated_delivery_date date
);

create table if not exists transactions(
	transaction_id int primary key,
	order_id int,
	foreign key(order_id) references orders(order_id),
	ship_date date,
	ship_mode varchar(255),
	product_id int,
	category varchar(255),
	sub_category varchar(255),
	product_name varchar(255),
	sales float,
	quantity int,
	discount float,
	profit float
);

create table if not exists returns(
	order_id int,
	foreign key(order_id) references orders(order_id),
	return_reason varchar(255)
);


select * from transactions limit 10;
select * from vendors limit 10;
select * from orders limit 10;
select * from returns limit 10;
select * from customers limit 10;
