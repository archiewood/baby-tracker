---
title: Feeds
queries:
- events.sql
---

```sql feed_events
select
    *,
    --extract the ml from the "End Condition" field, could be up to 999ml
    regexp_replace("End Condition", '\\D', '', 'g') as ml
from ${events}
where type = 'Feed'
```

```sql nursing_per_day
select
    date_trunc('day', start_at) as day,
    sum(duration) as total_minutes,
    sum(duration) / 60 as total_hours,
    count(*) as count
from ${feed_events}
group by day
```

```sql bottle_feeds_per_day
select
    date_trunc('day', start_at) as day,
    sum(ml::int) as total_ml
from ${feed_events}
where "Start Condition" = 'Breast Milk'
group by day
```

```sql nursing_and_bottle
select
    nursing.day,
    nursing.total_hours as nursing_hours,
    bottle.total_ml as bottle_ml
from ${nursing_per_day} as nursing
left join ${bottle_feeds_per_day} as bottle
on nursing.day = bottle.day
```

<LineChart
    data={nursing_and_bottle}
    x=day
    y=nursing_hours
    yAxisTitle=false
    yGridlines=false
    yFmt=num1
    yAxisLabels=false
    y2=bottle_ml
    y2AxisTitle=false
    y2Gridlines=false
    y2AxisLabels=false
    labels
/>

