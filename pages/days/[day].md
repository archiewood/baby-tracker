---
queries:
   - days: days.sql
---

# {params.day}

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
<div class=flex>
   <div class="bg-[#5470C6] text-white font-semibold mr-2 px-2">Sleep</div>
   <div class="bg-[#91CC75] text-white font-semibold mr-2 px-2">Feed</div>
   <div class="bg-[#aba321] text-white font-semibold mr-2 px-2">Diaper</div>
   <div class="bg-[#EE6666] text-white font-semibold mr-2 px-2">Tummy time</div>
</div>


<ECharts config={
   {
    xAxis: {
        type: 'time',
        boundaryGap: false
    },
    yAxis: {
        show: false, // This hides the Y-axis
        type: 'category',
        data: ['Events'],
        axisLine: { onZero: false }
    },
    grid: {
        backgroundColor: '#F1F1F1',  // Light grey background within the grid
        show: true,  // Ensures the grid itself is visible
        containLabel: false,
        borderWidth: 0,  // Optionally remove border if not needed
        right: 0,
        top: 0,   
    },
    tooltip: {
        trigger: 'item',
        formatter: function (params) {
            // Convert timestamps back to more readable date strings
            var startDate = new Date(params.value[0]).toLocaleString();
            var endDate = new Date(params.value[1]).toLocaleString();
            var duration = (params.value[1] - params.value[0]) / 1000 / 60; // Duration in minutes
            return `<b>${params.name}</b><br/>Start: ${startDate}<br/>End: ${endDate}<br/>Duration: ${duration} minutes<br/>Notes: ${params.data.end_condition}`;
        }
    },
    series: [{
      name: 'Event Timeline',
      type: 'custom',
      renderItem: function (params, api) {
         var categoryIndex = api.value(2);
         var start = api.coord([api.value(0), categoryIndex]);
         var end = api.coord([api.value(1), categoryIndex]);
         var height = api.size([0, 1])[1];
         return {
               type: 'rect',
               shape: {
                  x: start[0],
                  y: start[1] - height / 2,
                  width: end[0] - start[0],
                  height: height
               },
               style: api.style()
         };
      },
      data: [...events_today].map(item => ({
         value: [
               new Date(item.start_at).getTime(), // Start time in milliseconds
               new Date(item.end_at || new Date(item.start_at).getTime() + 600000).getTime(), // End time or start time + default duration
               0 // Category index
         ],
         itemStyle: {
               color: 
                  item.Type === 'Sleep' ? '#5470C6' : 
                  item.Type === 'Feed' ? '#91CC75' : 
                  item.Type === 'Diaper' ? '#aba321' : 
                  '#EE6666'
         },
         name: item.Type,
         end_condition: item['End Condition']
      }))
    }]
}
}
   height='80px'
   renderer=svg
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




## Events Today

<DataTable data={events_today} rows=all/>


