---
title: Diapers
queries:
- events.sql
---

```sql diaper_events
select
    start_at,
    "End Condition" as condition,
    case 
        when condition ilike '%both%' then 'Both' 
        when condition ilike '%pee%' then '💧' 
        when condition ilike '%poo%' then '💩' 
        else 'Unknown'
    end as type
from ${events}
where type = 'Diaper'
```


It's important to ensure your baby is eating enough. 

However, if breastfeeding, you can't track what's going in. You can track what's coming out, though 💩.

In the first few days, a healthy baby will increase the number of diaper changes they need each day. The below values are from [Health Link BC](https://www.healthlinkbc.ca/sites/default/files/documents/BBC_diapering.pdf).

```sql daily_diapers
select
    date_trunc('day', start_at) as day,
    count(*) as count
from ${diaper_events}
group by all
```

```sql diapers_target
select 
    date_trunc('day',strptime(target_date, '%Y-%m-%d %H:%M')) as day,
    target_count as count
from targets
where Type = 'Diaper'
```

```sql actual_vs_target
select
    actual.day,
    actual.count as diapers,
    target.count as target
from ${daily_diapers} as actual
left join ${diapers_target} as target
on actual.day = target.day
```
    

<BarChart
    data={actual_vs_target}
    x=day
    y=diapers
    y2=target
    title="Diapers vs Target"
    labels
    yGridlines=false
    yAxisLabels=false
    yAxisTitle=false
    y2AxisLabels=false
    y2Gridlines=false
    y2SeriesType=line
    y2AxisTitle=false
    legend
/>

## Unneccessary Detail

```sql daily_diapers_by_type
select
    date_trunc('day', start_at) as day,
    type,
    count(*) as count
from ${diaper_events}
group by day, type
```

<BarChart
    data={daily_diapers_by_type}
    x=day
    y=count
    series=type
    colorPalette={['#FFD700', '#8B4513', '#008000']}
    title="Diapers by Type"
    labels
    yGridlines=false
    yAxisLabels=false   
/>

