select
    date_trunc('day', strptime(start, '%Y-%m-%d %H:%M') + interval '4 hours') as day,
    count(*) as count
from events
GROUP BY all
order by 1