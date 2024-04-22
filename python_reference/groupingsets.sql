drop table salaries;

create table salaries(
	employee varchar(40),
	department varchar(40),
	salary int
);


insert into salaries(employee, department, salary)
values('chris', 'IT', 55000);
insert into salaries(employee, department, salary)
values('abhishek', 'IT', 110000);
insert into salaries(employee, department, salary)
values('sarah', 'HR', 5000);
insert into salaries(employee, department, salary)
values('john', 'HR', 32500);
insert into salaries(employee, department, salary)
values('john', 'Accounting', 20000);
insert into salaries(employee, department, salary)
values('john', 'Accounting', 25000);


select department,
sum(salary) as dept_salaries
from salaries
group by department
union all
select '', sum(salary)
from salaries;


select department,
sum(salary) as dept_salaries
from salaries
group by
	grouping sets(
		(department),
		()
	)
order by department nulls last;
