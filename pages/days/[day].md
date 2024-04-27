---
queries:
   - days: days.sql
   - events.sql
---

# <Value data={today} value=day fmt="ddd DD mmm"/>

```sql today
select * from ${days}
where day = '${params.day}'
```


```sql events_today
select * from ${events}
where start_at between '${params.day} 04:00:00' and '${fmt(today[0].next_day, "YYYY-MM-DD")} 04:00:00'
order by start_at
```

```sql minutes_per_event_type
select
  type,
  sum(duration) as total_minutes,
  sum(duration) / 60 as total_hours,
  count(*) as count
from ${events_today}
group by type
```

<Timeline 
   data={events_today} 
   height=80 
   legend
   min={params.day}
   max={fmt(today[0].next_day, "YYYY-MM-DD")}
/>



{#each minutes_per_event_type as row}

{#if row.total_hours !== null} 
   
   <BigValue
      data={row}
      value=total_hours
      title={row.Type}
      fmt='0.0 "hours"'
   />

{:else}

   <BigValue
      data={row}
      value=count
      title={row.Type}
      fmt='0 "{row.Type}s"'
   />
{/if}
   
   

{/each}



