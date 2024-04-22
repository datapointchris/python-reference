drop table employees;

create table employees(
	employee_id int,
	name varchar(40),
	manager_id int
);

insert into employees(employee_id, name, manager_id)
values(1, 'boss', null);
insert into employees(employee_id, name, manager_id)
values(2, 'abhishek', 1);
insert into employees(employee_id, name, manager_id)
values(3, 'chris', 1);
insert into employees(employee_id, name, manager_id)
values(4, 'sarah', 2);
insert into employees(employee_id, name, manager_id)
values(5, 'bob', 2);
insert into employees(employee_id, name, manager_id)
values(6, 'jim', 3);

select e.name,
count(m.employee_id) as num_reports
from employees e
left join employees m on e.employee_id = m.manager_id
group by e.name;

SELECT e1.emp_Id EmployeeId, e1.emp_name EmployeeName,
       e1.emp_mgr_id ManagerId, e2.emp_name AS ManagerName
FROM   tblEmployeeDetails e1
       LEFT JOIN tblEmployeeDetails e2
       ON e1.emp_mgr_id = e2.emp_id
