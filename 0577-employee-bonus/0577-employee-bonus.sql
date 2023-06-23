select x.name,y.bonus from employee x
left join bonus y on y.empid=x.empid
where y.bonus<1000 or y.bonus is null