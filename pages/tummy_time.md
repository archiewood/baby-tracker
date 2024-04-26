---
title: Tummy Time
queries:
  - events.sql
---

```sql tt_by_day
select
    date_trunc('day', start_at) as day,
    sum(duration) as total_minutes,
    sum(duration) / 60 as total_hours,
from ${events}
where type = 'Tummy time'
group by day
```

```sql tt_targets
select 
    date_trunc('day',strptime(target_date, '%Y-%m-%d %H:%M')) as day,
    target_mins::int as target_mins,
    target_mins::int / 60 as target_hours
from targets
where Type = 'Tummy time'
```

```sql tt_actual_vs_target
select
    day,
    total_minutes as tummy_time,
    'Tummy Time' as source
from ${tt_by_day} 
union all
select
    day,
    target_mins as target,
    'Target' as source
from ${tt_targets}
order by source desc
```

<LineChart
    data={tt_actual_vs_target}
    x=day
    y=tummy_time
    series=source
    title="Tummy Time vs Target"
    labels
    markers
    yGridlines=false
    yAxisLabels=false
/>
