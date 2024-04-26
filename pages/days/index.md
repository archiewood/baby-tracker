---
title: Days
queries:
   - days: days.sql
---

```sql days_with_link
select 
   day,
   strftime('%A %d %b', day) as day_fmt,
   '/days/' || day as link
from ${days}
order by day desc
```

<DataTable data={days_with_link} link=link>
   <Column id=day_fmt title="Day"/>
</DataTable>