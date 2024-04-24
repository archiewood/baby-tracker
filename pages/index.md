# Baby Tracker

This project ingests a csv from the [Huckleberry App](https://huckleberrycare.com/) and displays the data from it.

```sql events
select 
  type,
  strptime(start, '%Y-%m-%d %H:%M') as "start_at",
  strptime("end", '%Y-%m-%d %H:%M') as "end_at",
  date_diff('minute', "start_at", "end_at") as "duration",
  "Start Condition",
  "End Condition",
  notes
from events
```

## Most Recent Events

<DataTable data={events}/>

```sql event_counts
select
  type,
  count(*) as count
from events
group by type
order by count desc
```

## Event Counts

<DataTable data={event_counts}/>

