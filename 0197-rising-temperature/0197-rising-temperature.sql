# # Write your MySQL query statement below
# SELECT DISTINCT a.Id
# FROM Weather a,Weather b
# WHERE a.Temperature > b.Temperature
# AND DATEDIFF(a.Recorddate,b.Recorddate) = 1
select x.id from weather x,weather y
where x.temperature>y.temperature and DATEDIFF(x.recordDate,y.recordDate)=1