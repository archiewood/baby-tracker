<script>
    export let data=undefined;
</script>

<ECharts 
   config={
      {
         xAxis: {
            type: 'time',
            boundaryGap: false
         },
         yAxis: {
            type: 'category',
            data: ['Event Timeline'],
            axisLine: { onZero: false }
         },
         series: data.map(item => ({
            name: item.Type,
            type: 'bar',
            stack: 'total',  // Important: this ensures all bars are stacked on the same line
            data: [{
                  value: [
                     new Date(item.start_at).getTime(), // Start time in milliseconds
                     (item.end_at ? new Date(item.end_at).getTime() : new Date(item.start_at).getTime() + 600000), // End time or start time + 10 min default
                     0  // Keeps them on the same line (y-axis index 0)
                  ],
                  itemStyle: {
                     color: item.Type === 'Sleep' ? '#5470C6' : 
                           item.Type === 'Feed' ? '#91CC75' : '#EE6666'
                  }
            }]
         })),
         tooltip: {
            formatter: function (params) {
                  return `${params.seriesName}<br/>Duration: ${params.value[0] / 1000 / 60} minutes`;
            }
         }
      }
   }
/>