import eel
from importlib.resources import files

WEB_DIR = files('skateboard').joinpath('web')

class Skateboard():
    def __init__(self):
        self.chart_options = {}

        # Start eel
        eel.init(WEB_DIR, allowed_extensions=['.js', '.html', '.css'])

    def header(self, text, node_id = "", options = {}):
        eel.updateHeader(text, node_id, options)

    def paragraph(self, text, node_id = "", options = {}):
        eel.updateParagraph(text, node_id, options)

    def divider(self, node_id = "", options = {}):
        eel.updateDivider(node_id, options)

    def value_chart(self, chart_data, node_id, options = None):
        if(options):
            self.chart_options = options

        eel.updateValueChart(chart_data, node_id, self.chart_options)

    def start(self, block = True):
        eel.start("index.html", size=(800, 800), block = block)


    def close(self):
        pass