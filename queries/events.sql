select 
  type,
  strptime(start, '%Y-%m-%d %H:%M') + interval '4 hours' as "start_at",
  strptime("end", '%Y-%m-%d %H:%M') + interval '4 hours' as "end_at",
  date_diff('minute', "start_at", "end_at") as "duration",
  case 
    when "Type" = 'Sleep' and date_part('hour', "start_at") >= 12 and date_part('hour', "end_at") <= 24 then 'Day'
    when "Type" = 'Sleep' then 'Night'
    else null
  end as sleep_type,
  case when "Type" = 'Growth' then "Start Condition" else null end as weight,
  case when "Type" = 'Growth' then "End Condition" else null end as height,
  "Start Condition",
  "End Condition",
  notes
from events
where 
  --"Type" != 'Growth' and 
  "Type" != 'Pump'
GROUP BY all