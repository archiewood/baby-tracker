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
  notes,
  case
    when "Type" = 'Growth' then cast(split_part("Start Condition", 'kg', 1) as decimal)
    else null 
  end as weight_kg,
  case
    when "Type" = 'Growth' then cast(split_part(split_part("Start Condition", 'kg', 2), 'cm', 1) as decimal)
    else null
  end as length_cm,
  case
    when "Type" = 'Growth' then cast(split_part(split_part("Start Condition", 'cm', 2), 'cm', 1) as decimal) 
    else null
  end as head_circumference_cm  
from events
GROUP BY all