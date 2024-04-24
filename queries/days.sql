select
    date_trunc('day', strptime(start, '%Y-%m-%d %H:%M')) as day,
    count(*) as count
from events
GROUP BY all
order by 1