---
title: Growth Tracker
description: Track your baby's growth over time, including weight and height.
---

```sql weight_data
select
  date_trunc('day', recorded_at) as date,
  weight_kg
from growth 
where metric = 'weight'
order by date
```

```sql height_data 
select
  date_trunc('day', recorded_at) as date, 
  height_cm
from growth
where metric = 'height'  
order by date
```

<h1>Growth Tracker</h1>

<h2>Weight</h2>

<InternalTimeline
  data={weight_data}
  title="Weight (kg)"
  min={fmt(weight_data[0].date, "YYYY-MM-DD")}  
  max={fmt(weight_data[weight_data.length-1].date, "YYYY-MM-DD")}
  yAxisLabels={true}
/>

<h2>Height</h2>

<InternalTimeline
  data={height_data}
  title="Height (cm)"  
  min={fmt(height_data[0].date, "YYYY-MM-DD")}
  max={fmt(height_data[height_data.length-1].date, "YYYY-MM-DD")}
  yAxisLabels={true}  
/>