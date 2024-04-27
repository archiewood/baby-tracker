---
title: The Data Driven Newborn 👶🏼
description: A data driven tracker for newborns that ingests data from the Huckleberry App and compares it to various targets and guidelines.
queries:
  - events.sql
---

This project ingests a csv from the [Huckleberry App](https://huckleberrycare.com/) and displays the data from it.

It also compares the data to various targets and guideline values recommended by health professionals.

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
limit 3
```




## Daily Timelines, Last 3 Days

{#each last_3_days as row, i}

<Timeline   
  data={events.where(`start_at between '${fmt(row.day, "YYYY-MM-DD")} 04:00:00' and '${fmt(row.next_day, "YYYY-MM-DD")} 04:00:00'`)} 
  height=80 
  title={fmt(row.day, "ddd dd")} 
  link="days/{fmt(row.day, 'YYYY-MM-DD')}"
  legend={i === 0}
  min={fmt(row.day, "YYYY-MM-DD")}
  max={fmt(row.next_day, "YYYY-MM-DD")}
  yAxisLabels={false}
/>

{/each}