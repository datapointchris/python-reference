create table users (
    user_id int,
    product_id int,
    transaction_date text
);


insert into users (user_id, product_id, transaction_date) values
(1, 101, '2-12-20'),
(2, 105, '2-13-20'),
(1, 111, '2-14-20'),
(3, 121, '2-15-20'),
(1, 101, '2-16-20'),
(2, 105, '2-17-20'),
(4, 101, '2-16-20'),
(3, 105, '2-15-20');


with ordered as(
select user_id, transaction_date,
row_number() over(partition by user_id order by user_id, transaction_date) as rownum
from users
order by user_id, transaction_date),

filtered as(
select user_id, transaction_date as superuser_date
	from ordered
	where rownum = 2),

du as (select distinct user_id from users)

select du.user_id, filtered.superuser_date
from du
left join filtered on du.user_id = filtered.user_id
order by superuser_date;
