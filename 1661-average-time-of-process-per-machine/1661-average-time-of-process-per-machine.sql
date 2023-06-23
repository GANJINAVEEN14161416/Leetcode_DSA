select x.machine_id,round(avg(y.timestamp-x.timestamp),3) as processing_time
from activity x,activity y where x.machine_id=y.machine_id and x.process_id=y.process_id and x.activity_type="start" and y.activity_type="end"
group by machine_id