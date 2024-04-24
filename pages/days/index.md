---
title: Days
queries:
   - days: days.sql
---

Click on an item to see more detail


```sql days_with_link
select *, '/days/' || day as link
from ${days}
```

<DataTable data={days_with_link} link=link/>
