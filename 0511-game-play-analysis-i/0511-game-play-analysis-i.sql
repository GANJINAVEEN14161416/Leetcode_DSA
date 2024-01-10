select player_id ,event_date as first_login from (select player_id,event_date,row_number() over (partition by player_id order by event_date) as row_num from activity ) as t
where row_num=1