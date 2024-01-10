select id, case 
when p_id is null then 'Root'
when id not in (select id from tree where id in (select p_id from tree)) then 'Leaf'
else 'Inner' 
end as type 
from tree