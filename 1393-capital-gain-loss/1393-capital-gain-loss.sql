select stock_name,sum(if(operation='Sell',price,0))-sum(if(operation='Buy',price,0)) as capital_gain_loss
from stocks
group by stock_name