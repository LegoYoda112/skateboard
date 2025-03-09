import eel
from importlib.resources import files

WEB_DIR = files('skateboard').joinpath('web')

class Skateboard():
    def __init__(self):
        eel.init(WEB_DIR)


    def start(self):
        eel.start("index.html", size=(100, 800))