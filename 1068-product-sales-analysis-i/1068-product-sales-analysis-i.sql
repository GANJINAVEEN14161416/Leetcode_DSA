select y.product_name,x.year,x.price from sales x
left join product y on x.product_id=y.product_id