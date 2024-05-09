select 
  type,
  strptime(start, '%Y-%m-%d %H:%M') + interval '4 hours' as "start_at",
  strptime("end", '%Y-%m-%d %H:%M') + interval '4 hours' as "end_at",
  date_diff('minute', "start_at", "end_at") as "duration",
  case 
    when "Type" = 'Sleep' and date_part('hour', "start_at") >= 8 and date_part('hour', "end_at") <= 20 then 'Day'
    when "Type" = 'Sleep' then 'Night'
    else null
  end as sleep_type,
  "Start Condition",
  "End Condition",
  notes
from events
where "Type" != 'Growth' 
  and "Type" != 'Pump'
GROUP BY all