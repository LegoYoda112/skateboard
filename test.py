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
    "tooltip": True,
    "showSymbol": False,
    "filled": False
}
board.value_chart([], "value_chart", options=main_chart_options)
board.value_chart([], "value_chart_2", options=main_chart_options)

board.start(block = False)

chart_data = []
chart_data_2 = []

for i in range(1000):
    board.paragraph(i, "test_paragraph")
    print(i)

    chart_data.append([i/50, math.sin(i/10)])
    board.value_chart(chart_data, "value_chart")

    chart_data_2.append([i/50, math.cos(i/10)])
    board.value_chart(chart_data_2, "value_chart_2")


    eel.sleep(0.02)

# board.close()