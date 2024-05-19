---
title: Growth 
description: Growth tracking and analysis for my newborn baby.
queries:
  - events.sql
---

```sql dates
select
    date_trunc('day', start_at) as day 
from ${events}
where type = 'Growth'
group by day
```

<DateRange name=date_range data={dates} dates=day/>

```sql growth_by_day
select
    date_trunc('day', start_at) as day,
    cast(split_part("Start Condition", ' ', 1) as decimal) as weight_kg
from ${events}  
where type = 'Growth'
and day between '${inputs.date_range.start}' and '${inputs.date_range.end}'
group by day, "Start Condition"
```

<LineChart
    data={growth_by_day}
    x=day
    y=weight_kg
    title="Weight Over Time"
    labels
    yAxisTitle="Weight (kg)"
/>