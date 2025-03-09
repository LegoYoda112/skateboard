from src.skateboard import Skateboard
import eel
import time

board = Skateboard()

board.header("Hello!")
board.paragraph("lol", "test_paragraph")
board.divider()
board.paragraph("More text!")

board.start(block = False)

for i in range(1000):
    board.paragraph(i, "test_paragraph")
    print(i)
    eel.sleep(0.05)

board.close()