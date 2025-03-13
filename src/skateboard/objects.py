from abc import ABC, abstractmethod
import uuid
import eel

class SkateboardObject(ABC):
    def __init__(self, columns = 1, id = None, options = {}):
        if(id == None):
            self.id = str(uuid.uuid4())
        else:
            self.id = id

        print(self.id)
        


        self.options = {}
        self.columns = columns

    @abstractmethod
    def update(self):
        pass


# ========= Text objects
class SkateboardTextObject(SkateboardObject):
    def __init__(self, text, columns, id = None):
        super().__init__(columns, id)

        self.text = text
               

class SkateboardHeader(SkateboardTextObject):
    def __init__(self, text, columns = 1, id = None, options = {}):
        super().__init__(text, columns, id, options)

    def update(self):
        eel.updateHeader(self.text, self.id, self.columns, self.options)


class SkateboardParagraph(SkateboardTextObject):
    def __init__(self, text, columns = 1, id = None):
        super().__init__(text, columns, id)

    def update(self):
        eel.updateParagraph(self.text, self.id, self.columns, self.options)


# ========= Organization objects
class SkateboardDivider(SkateboardObject):
    def __init__(self, id = None, options = {}):
        super().__init__(id = id, options = options)

    def update(self):
        eel.updateDivider(self.id, self.columns, self.options)


# ========= Chart objects
class SkateboardChart(SkateboardObject):
    def __init__(self, chart_data, columns = 1, id = None, options = {}):
        super().__init__(columns, id, options)
        self.chart_data = chart_data

    def update(self, new_data = None):
        if(new_data):
            self.chart_data = new_data

        eel.updateValueChart(self.chart_data, self.id, self.columns, self.options)