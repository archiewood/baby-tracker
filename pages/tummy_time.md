---
title: Tummy Time
queries:
  - events.sql
---

Tummy time helps babies develop their neck and back muscles, as well as preventing flat spots on their heads. Our doctor recommended 30 minutes a day.


```sql tt_by_day
select
    strptime(date_trunc('day', start_at), '%x') + interval '4 hours' as day,
    sum(duration) as total_minutes,
    sum(duration) / 60 as total_hours,
from ${events}
where type = 'Tummy time'
group by day
```

<BarChart
    data={tt_by_day}
    x=day
    y=total_minutes
    title="Tummy Time vs Target"
    labels
    markers
    yGridlines=false
    yAxisLabels=false
    handleMissing=zero
>
<ReferenceLine y=30 label="Recommended Level" />
</BarChart>

