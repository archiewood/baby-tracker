---
title: Feeds
queries:
- events.sql
---

The NCT [recommends](https://www.nct.org.uk/baby-toddler/feeding/early-days/how-often-should-i-breastfeed-my-baby) newborns feed every 2-3 hours (8-12 times a day). 

If nursing, they recommend 20-30 min feeds.

The range of feeding time recommended is therefore:
- **Min:** 8 x 20 mins = 160 min = **2.7 hours / day**
- **Max:** 12 x 30 mins = 360 mins = **6.0 hours / day**


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
    bottle.total_ml as bottle_feed_ml
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
    yMax=6
    y2=bottle_feed_ml
    y2AxisTitle=false
    y2Gridlines=false
    y2AxisLabels=false
    labels
>
    <ReferenceArea yMin=2.666 yMax=6 label="Recommended Nursing Hours" labelPosition=topRight/>
</LineChart>

If you are supplementing with bottle feeds, you will be feeding for fewer hours.