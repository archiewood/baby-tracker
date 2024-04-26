---
title: Diapers
---

It's important to ensure your baby is eating enough. 

However, if nursing, you can't track what's going in 🍼. You can track what's coming out, though 💩.

In the first few days, a healthy baby will increase the number of diaper changes they need each day. The below values are from [Health Link BC](https://www.healthlinkbc.ca/sites/default/files/documents/BBC_diapering.pdf).

```sql diapers
select
    date_trunc('day', strptime(start, '%Y-%m-%d %H:%M')) as day,
    count(*) as count
from events
where "Type" = 'Diaper'
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
from ${diapers} as actual
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



