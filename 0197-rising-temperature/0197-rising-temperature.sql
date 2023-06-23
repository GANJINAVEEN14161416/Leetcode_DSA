select x.id from weather x,weather y
where x.temperature >y.temperature and datediff(x.recorddate,y.recorddate)=1