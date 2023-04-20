# Write your MySQL query statement below
SELECT salesperson.name
FROM salesperson
WHERE salesperson.sales_id NOT IN
(SELECT salesperson.sales_id FROM salesperson
JOIN orders ON salesperson.sales_id = orders.sales_id
JOIN company ON orders.com_id = company.com_id
WHERE company.name = 'RED')
