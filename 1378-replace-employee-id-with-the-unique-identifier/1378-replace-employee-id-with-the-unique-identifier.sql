select y.unique_id,x.name from employees x 
left join employeeuni y on x.id=y.id