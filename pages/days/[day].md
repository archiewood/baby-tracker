---
queries:
   - days: days.sql
---

# {params.day}

# <Value data={events_today} value=start_at fmt="ddd DD mmm"/>

```sql events_today
select 
  type,
  strptime(start, '%Y-%m-%d %H:%M') as "start_at",
  strptime("end", '%Y-%m-%d %H:%M') as "end_at",
  date_diff('minute', "start_at", "end_at") as "duration",
  "Start Condition",
  "End Condition",
  notes
from events
where start like '${params.day}%'
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


<Timeline data={events_today} height=80 legend/>



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



