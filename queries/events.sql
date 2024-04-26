select 
  type,
  strptime(start, '%Y-%m-%d %H:%M') as "start_at",
  strptime("end", '%Y-%m-%d %H:%M') as "end_at",
  date_diff('minute', "start_at", "end_at") as "duration",
  "Start Condition",
  "End Condition",
  notes
from events