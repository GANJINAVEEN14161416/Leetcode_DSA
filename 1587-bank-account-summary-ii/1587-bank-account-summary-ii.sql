select name,sum(transactions.amount) as balance
from users left join transactions
on users.account=transactions.account
group by transactions.account
having balance>10000