from src.skateboard import Skateboard
import eel
import math
import time

board = Skateboard()

board.header("Hello!")
board.paragraph("lol", "test_paragraph")
board.divider()
board.paragraph("More text!")

main_chart_options = {
    "yUnit": "A",
    "xUnit": "s",
    "tooltip": False,
    "showSymbol": False,
    "filled": True,
    "zoom": True,
    "color": "#85ffa5",
    "gaugeValue": False
}
board.value_chart([], "value_chart", options=main_chart_options)
board.value_chart([], "value_chart_2", options=main_chart_options)
board.value_chart([], "value_chart_3", options=main_chart_options)
board.value_chart([], "value_chart_4", options=main_chart_options)
board.value_chart([], "value_chart_5", options=main_chart_options)

board.start(block = False)

chart_data = []
chart_data_2 = []

for i in range(10000):
    board.paragraph(i, "test_paragraph")
    print(i)

    if(len(chart_data) > 200):
        chart_data.pop(0)
    
    if(len(chart_data_2) > 200):
        chart_data_2.pop(0)

    chart_data.append([i/50, math.sin(i/30)])
    board.value_chart(chart_data, "value_chart")

    chart_data_2.append([i/50, math.cos(i/10)])
    board.value_chart(chart_data_2, "value_chart_2")
    board.value_chart(chart_data_2, "value_chart_3")
    board.value_chart(chart_data_2, "value_chart_4")
    board.value_chart(chart_data_2, "value_chart_5")


    eel.sleep(0.02)

# board.close()