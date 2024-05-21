---
title: Growth
description: Height and weight tracking and analysis for my newborn baby.
queries:
  - events.sql
---

Baby growth is tracked typically using height, weight, and head circumference. These can be compared to benchmarks such as [those maintained by the CDC](https://www.cdc.gov/growthcharts/html_charts/wtageinf.htm). 

```sql height
select
    start_at,
    height
from ${events}
where height is not null
order by start_at
```

```sql weight
select
    start_at,
    date_diff('day',  date '2024-04-19', start_at)/30.4 as months,
    split_part(weight, 'kg', 1)::float as weight
from ${events}
where weight is not null
order by start_at
```

```sql weight_percentiles
select 0 as months, 3 as percentile, 2.355451 as weight union all
select 0 as months, 5 as percentile, 2.526904 as weight union all
select 0 as months, 10 as percentile, 2.773802 as weight union all
select 0 as months, 25 as percentile, 3.150611 as weight union all
select 0 as months, 50 as percentile, 3.530203 as weight union all
select 0 as months, 75 as percentile, 3.879077 as weight union all
select 0 as months, 90 as percentile, 4.172493 as weight union all
select 0 as months, 95 as percentile, 4.340293 as weight union all
select 0 as months, 97 as percentile, 4.446488 as weight union all
select 0.5 as months, 3 as percentile, 2.799549 as weight union all
select 0.5 as months, 5 as percentile, 2.964656 as weight union all
select 0.5 as months, 10 as percentile, 3.20951 as weight union all
select 0.5 as months, 25 as percentile, 3.597396 as weight union all
select 0.5 as months, 50 as percentile, 4.003106 as weight union all
select 0.5 as months, 75 as percentile, 4.387423 as weight union all
select 0.5 as months, 90 as percentile, 4.718161 as weight union all
select 0.5 as months, 95 as percentile, 4.91013 as weight union all
select 0.5 as months, 97 as percentile, 5.032625 as weight union all
select 1.5 as months, 3 as percentile, 3.614688 as weight union all
select 1.5 as months, 5 as percentile, 3.774849 as weight union all
select 1.5 as months, 10 as percentile, 4.020561 as weight union all
select 1.5 as months, 25 as percentile, 4.428873 as weight union all
select 1.5 as months, 50 as percentile, 4.879525 as weight union all
select 1.5 as months, 75 as percentile, 5.327328 as weight union all
select 1.5 as months, 90 as percentile, 5.728153 as weight union all
select 1.5 as months, 95 as percentile, 5.967102 as weight union all
select 1.5 as months, 97 as percentile, 6.121929 as weight union all
select 2.5 as months, 3 as percentile, 4.342341 as weight union all
select 2.5 as months, 5 as percentile, 4.503255 as weight union all
select 2.5 as months, 10 as percentile, 4.754479 as weight union all
select 2.5 as months, 25 as percentile, 5.183378 as weight union all
select 2.5 as months, 50 as percentile, 5.672889 as weight union all
select 2.5 as months, 75 as percentile, 6.175598 as weight union all
select 2.5 as months, 90 as percentile, 6.638979 as weight union all
select 2.5 as months, 95 as percentile, 6.921119 as weight union all
select 2.5 as months, 97 as percentile, 7.10625 as weight union all
select 3.5 as months, 3 as percentile, 4.992898 as weight union all
select 3.5 as months, 5 as percentile, 5.157412 as weight union all
select 3.5 as months, 10 as percentile, 5.416803 as weight union all
select 3.5 as months, 25 as percentile, 5.866806 as weight union all
select 3.5 as months, 50 as percentile, 6.391392 as weight union all
select 3.5 as months, 75 as percentile, 6.942217 as weight union all
select 3.5 as months, 90 as percentile, 7.460702 as weight union all
select 3.5 as months, 95 as percentile, 7.781401 as weight union all
select 3.5 as months, 97 as percentile, 7.993878 as weight 
```

<LineChart
    data={weight}
    x=start_at
    y=weight
    yMax=10
    yFmt='0.0"kg"'
    title="Weight"
    labels
    markers=true
/>



```sql weight_vs_percentile
select months, weight, 'Actual' as percentile from ${weight}
union all
select months, weight, percentile from ${weight_percentiles}
```

<LineChart
    data={weight_vs_percentile}
    x=months
    xFmt='0'
    xAxisTitle="Months"
    y=weight
    yFmt='0.0"kg"'
    title="Weight vs CDC Percentiles (Boys)"
    series=percentile
    seriesColors={{
        "Actual": "black", 
        "3": "#C7E6F2",
        "5": "#A5D8F1",
        "10": "#76C7E0",
        "25": "#3CA0C3",
        "50": "#1F5D99",
        "75": "#3CA0C3",
        "90": "#76C7E0",
        "95": "#A5D8F1",
        "97": "#C7E6F2"
        }}
    renderer=svg
/>