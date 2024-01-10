SELECT Player_Id ,Event_Date AS first_login from 
(
    SELECT Player_id,Event_Date,ROW_NUMBER() OVER(PARTITION BY player_id order by event_date) as Row_No
    from activity
)as t
where Row_No=1;
