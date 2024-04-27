select
    date_trunc('day', strptime(start, '%Y-%m-%d %H:%M') + interval '4 hours') as day,
    day + interval '1 day' as next_day,
    count(*) as count
from events
GROUP BY all
order by 1