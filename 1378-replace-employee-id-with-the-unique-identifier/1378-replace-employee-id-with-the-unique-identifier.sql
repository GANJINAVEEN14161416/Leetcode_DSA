select y.unique_id as unique_id,x.name as name from employees x 
left join employeeuni y on x.id=y.id