import eel
from importlib.resources import files

WEB_DIR = files('skateboard').joinpath('web')

class Skateboard():
    def __init__(self):
        # Start eel
        eel.init(WEB_DIR, allowed_extensions=['.js', '.html', '.css'])

    def add_header(self, text, node_id = None, options = {}):
        eel.addHeader(text, node_id, options)

    def add_paragraph(self, text, node_id = None, options = {}):
        eel.addParagraph(text, node_id, options)

    def start(self):
        eel.start("index.html", size=(800, 800))