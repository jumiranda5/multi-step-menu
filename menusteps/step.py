# Create class for menu step
class Step():
    def __init__(self, id, title="", input_text="Type the option number: ", color="white"):
        self.id = id
        self.title = title
        self.input_text = input_text
        self.color = color

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        # id must be an integer
        if not isinstance(id, int):
            raise ValueError("'id' should be an integer.")
        
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title == None:
            self._title = ""
        else:
            self._title = title

    @property
    def input_text(self):
        return self._input_text

    @input_text.setter
    def input_text(self, input_text):
        if input_text == None:
            self._input_text = ""
        else:
            self._input_text = input_text

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        if not color in colors:
            self._color = "white"
        else:
            self._color = color