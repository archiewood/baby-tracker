<script>
    export let data = undefined;
    export let height = 80;
    export let title = '';
    export let legend = false;
    export let link = undefined;
    export let min = undefined;
    export let max = undefined;
    export let yAxisLabels = true;
    import { ECharts } from "@evidence-dev/core-components";
</script>

{#if legend}
    <div class="flex justify-end">
        <div class="bg-[#bfdbf7] text-white font-semibold mr-2 px-2">Sleep</div>
        <div class="bg-[#488f96] text-white font-semibold mr-2 px-2">Feed</div>
        <div class="bg-[#ffc857] text-white font-semibold mr-2 px-2">Diaper</div>
        <div class="bg-[#923d59] text-white font-semibold mr-2 px-2">Tummy time</div>
    </div>
{/if} 

<ECharts 
    config={{
        title: {
            show: title !== "",  // Only show the title if it's not an empty string
            text: title,  // Text from the prop
            left: 'left',  // Align it to the left
            top: yAxisLabels ? '30%' : 'middle',
            link: link
        },
        xAxis: {
            type: 'time',
            boundaryGap: false,
            min: min,
            max: max
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
            containLabel: false,  // If true, the labels will be contained within the grid
            borderWidth: 0,  // Optionally remove border if not needed
            right: 0,
            bottom: yAxisLabels ? 20 : 0,
            top: 0,   
            // if title add left padding
            left: title !== "" ? title.length * 10 : 0
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                // Display date and weight/height value  
                var date = new Date(params.value[0]).toLocaleString();
                var value = params.value[1];
                return `<b>${params.name}</b><br/>Date: ${date}<br/>Value: ${value}`;
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
            data: [...data].map(item => ({
                value: [
                    new Date(item.date).getTime(), // Date in milliseconds
                    item.weight_kg || item.height_cm, // Weight or height value  
                    0 // Category index
                ],
                itemStyle: {
                    color: '#488f96'  
                },
                name: item.weight_kg ? 'Weight (kg)' : 'Height (cm)'
            }))  
        }]
    }}
    height="{height}px"
    renderer=svg
 />