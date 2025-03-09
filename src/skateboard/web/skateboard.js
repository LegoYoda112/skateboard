

document.addEventListener("DOMContentLoaded", function () {

});

charts = {}

eel.expose(updateHeader);
function updateHeader(header_text, node_id, options) {
    const {node: node, is_template: is_template} = findTemplateOrCreate("headerTemplate", node_id);

    node.querySelector("h2").textContent = header_text;

    if(is_template)
        document.getElementById("mainContainer").appendChild(node);
}

eel.expose(updateParagraph);
function updateParagraph(paragraph_text, node_id, options) {
    const {node: node, is_template: is_template} = findTemplateOrCreate("paragraphTemplate", node_id);

    node.querySelector("p").textContent = paragraph_text;

    if(is_template)
        document.getElementById("mainContainer").appendChild(node);
}

eel.expose(updateDivider);
function updateDivider(node_id, options) {
    const {node: node, is_template: is_template} = findTemplateOrCreate("dividerTemplate", node_id);

    if(is_template)
        document.getElementById("mainContainer").appendChild(node);
}

eel.expose(updateValueChart);
function updateValueChart(chart_data, node_id, options){
    const {node: node, is_template: is_template} = findTemplateOrCreate("valueChartTemplate", node_id);


    min_x = chart_data[0][0];
    max_x = chart_data[chart_data.length - 1][0]

    var chart_options = {
        xAxis: {
            type: "value",
            min: min_x,
            max: max_x
        },
        yAxis: {
            type: "value"
        },
        series: [
            {
                data: chart_data,
                type: "line",
                showSymbol: option_or(options, "showSymbol", false),
                itemStyle: {

                }
            }
        ]
    }

    if(options.gaugeValue){
        latestValue = chart_data[chart_data.length - 1][1];
        chart_options.graphic = [
            {
                type: 'text',
                left: 'center',
                top: "center",
                style: {
                    text: `${latestValue.toFixed(2)} ${option_or(options, "yUnit", "")}`, // Display last value
                    font: 'bold 48px Arial',
                    fill: option_or(options, "color", "#ffffff"), // Dark color for visibility
                    textAlign: 'center'
                },
                silent: true,
                zlevel: 1,
            }
        ];
    }

    if(options.tooltip){
        chart_options.tooltip = {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            }
        }
    }

    if(options.yUnit){
        chart_options.yAxis.axisLabel = {
            formatter: '{value} ' + options.yUnit
        }
    }

    if(options.xUnit){
        chart_options.xAxis.axisLabel = {
            formatter: '{value} ' + options.xUnit
        }
    }

    if(options.filled == true){
        chart_options.series[0].areaStyle ={};
    }

    if(options.zoom){
        chart_options.dataZoom = [
            {
              type: 'inside',
            },
            {

            }
          ]
    }

    if(options.color){
        chart_options.series[0].itemStyle.color = options.color;
    }

    var chart;

    if(is_template){
        chart = echarts.init(node.querySelector(".valueChart"));
        charts[node_id] = chart;
    } else {
        chart = charts[node_id]
    }
    chart.setOption(chart_options);

    if(is_template)
        document.getElementById("mainContainer").appendChild(node);

    chart.resize();
}

function findTemplateOrCreate(template_id, node_id){
    
    // Check if element exists
    if(node_id != "" && document.getElementById(node_id) ){
        console.log("updating existing element");
        // Return existing element
        const existingNode = document.getElementById(node_id)
        return {node: existingNode, is_template: false};
    } else {
        console.log("adding new element");
        // otherwise, make new element
        const template = document.getElementById(template_id);
        const newNode = template.content.cloneNode(true);
        if(node_id != "")
            newNode.querySelector('div').id = node_id;
        return {node: newNode, is_template: true}
    }
}

function option_or(options, key, default_value){
    if(options[key]){
        return options[key]
    } else {
        return default_value
    }
}