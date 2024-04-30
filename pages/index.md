---
title: The Data Driven Dad 👶🏼
description: A newborn tracker that ingests data from the Huckleberry App and compares to various health guidelines.
queries:
  - events.sql
---

This project ingests and displays data from the [Huckleberry App](https://huckleberrycare.com/). It compares the data to targets and guidelines recommended by health professionals.

```sql total_days
select 
  count(distinct date_trunc('day', strptime(start, '%Y-%m-%d %H:%M'))) as count
from events
```

<BigValue
  data={total_days}
  value=count
  title="Current Age"
  fmt='0 "days old"'
/>

```sql all_time_daily_kpis
select
  type,
  sum(duration) as total_minutes,
  sum(duration) / 60 as total_hours,
  count(*) as count,
  --daily average
  sum(duration) / count(distinct date_trunc('day',start_at)) as daily_avg_minutes,
  daily_avg_minutes / 60 as daily_avg_hours,
  count /   count(distinct date_trunc('day',start_at)) as daily_avg_count
from ${events}
group by type
```

{#each all_time_daily_kpis as row}

{#if row.total_hours !== null} 

{#if row.total_hours < 1}
<BigValue
  data={row}
  value=daily_avg_minutes
  title="Avg. {row.Type}"
  fmt='0 "minutes"'
/>
{:else}

<BigValue
  data={row}
  value=daily_avg_hours
  title="Avg. {row.Type}"
  fmt='0.0 "hours"'
/>

{/if}

{:else}

<BigValue
  data={row}
  value=daily_avg_count
  title="Avg. {row.Type}s"
  fmt='0 "{row.Type}s"'
/>

{/if}

{/each}




```sql last_3_days
select 
  date_trunc('day',start_at) as day,
  day + interval '1 day' as next_day,
from ${events}
group by day
order by day desc
limit ${inputs.days_limit.value}
```




## Daily Timelines, Last 3 Days

<Dropdown name=days_limit value=3 title="Data Range">
  <DropdownOption value=3 valueLabel="Last 3 days"/>
  <DropdownOption value=7 valueLabel="Last 7 days"/>
  <DropdownOption value=14 valueLabel="Last 14 days"/>
</Dropdown>
  
  






{#each last_3_days as row, i}

<Timeline   
  data={events.where(`start_at between '${fmt(row.day, "YYYY-MM-DD")} 04:00:00' and '${fmt(row.next_day, "YYYY-MM-DD")} 04:00:00'`)} 
  height={inputs.days_limit.value < 4 ? 80 : 40}
  title={fmt(row.day, "ddd dd")} 
  link="days/{fmt(row.day, 'YYYY-MM-DD')}"
  legend={i === 0}
  min={fmt(row.day, "YYYY-MM-DD")}
  max={fmt(row.next_day, "YYYY-MM-DD")}
  yAxisLabels={inputs.days_limit.value < 4}
/>

{/each}