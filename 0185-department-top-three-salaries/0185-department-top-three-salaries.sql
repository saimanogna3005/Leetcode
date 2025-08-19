# Write your MySQL query statement below
select d.name Department,e.name Employee,e.salary Salary
from Employee as e,Department as d
where e.departmentId = d.id and
(select count(distinct salary) from Employee
where salary>e.salary and departmentId = e.departmentId)<3
order by d.name,e.salary desc; 