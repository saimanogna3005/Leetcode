# Write your MySQL query statement below
Select(select distinct(salary) SecondHighestSalary from employee
order by salary desc
limit 1 offset 1) as SecondHighestSalary;