# Write your MySQL query statement below
SELECT max(salary) AS SecondHighestSalary  FROM EMPLOYEE WHERE salary not in (SELECT max(SALARY) FROM EMPLOYEE);
