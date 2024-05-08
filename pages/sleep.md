---
title: Sleep
description: Sleep tracking and analysis for my newborn baby.
queries:
  - events.sql
---

The National Sleep Foundation recommends [11-19 hours of sleep per day for newborns](https://www.sleepfoundation.org/baby-sleep), dropping to 12-16 hours per day for infants aged 4-6 months

```sql sleep_by_day
select
    date_trunc('day', start_at) as day,
    sum(duration) as total_minutes,
    sum(duration) / 60 as total_hours,
from ${events}
where type = 'Sleep'
group by day
```

```sql sleep_targets
select 
    date_trunc('day',strptime(target_date, '%Y-%m-%d %H:%M')) as day,
    target_mins::int / 60 as target_hours
from targets
where Type = 'Sleep'
```

```sql sleep_actual_vs_target
select
    actual.day,
    actual.total_hours as sleep,
    target.target_hours as target
from ${sleep_by_day} as actual
left join ${sleep_targets} as target
on actual.day = target.day
```

<LineChart
    data={sleep_by_day}
    x=day
    y=total_hours
    yMax=20
    --y2=target
    title="Sleep Hours vs Target"
    labels
    markers
    yAxisTitle=false
    yAxisLabels=false
    yGridlines=false
    --y2AxisLabels=false
    --y2Gridlines=false
    --y2SeriesType=line
    --y2AxisTitle=false
    --legend
>
<ReferenceArea yMin=11 yMax=19 label="NSF Target" labelPosition=topRight/>
</LineChart>

## Average Sleep Duration and Count

```sql sleep_kpis
select
    date_trunc('day', start_at) as day,
    sum(duration) as total_minutes,
    sum(duration) / 60 as total_hours,
    count(*) as number_of_sleeps,
    --daily average
    total_minutes / number_of_sleeps as avg_minutes_per_sleep
from ${events}
where type = 'Sleep'
and day>='2024-04-21'
group by day
```

<LineChart
    data={sleep_kpis}
    x=day
    y=avg_minutes_per_sleep
    yGridlines=false
    yAxisLabels=false
    yAxisTitle=false
    yFmt=num0
    labels
    y2=number_of_sleeps
    y2Max=30
    y2Gridlines=false
    y2AxisLabels=false
    y2AxisTitle=false
/>

## Sleep Night vs Day

```sql sleep_night_vs_day
select
    date_trunc('day', start_at) as day,
    sum(duration) as total_minutes,
    sum(duration) / 60 as total_hours,
    sleep_type
from ${events}
where type = 'Sleep'
group by all
```

<BarChart
    data={sleep_night_vs_day}
    x=day
    y=total_hours
    series=sleep_type
    labels
    yGridlines=false
    yAxisLabels=false
    yAxisTitle=false
    yFmt=num0
/>