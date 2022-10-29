# item = {"text": "option text", "value": "value to return", "next": int}

class Item:
    def __init__(self, text, next, value=""):
        self.text = text
        self.next = next
        self.value = value         

    # Getter text
    @property
    def text(self):
        return self._text

    # Setter for text
    @text.setter
    def text(self, text):
        # Check if text is not empty
        if not text:
            raise ValueError("Text is missing")
        self._text = text     

    # Getter next
    @property
    def next(self):
        return self._next

    # Setter for next
    @next.setter
    def next(self, next):
        # Check if next is a integer
        if not isinstance(next, int):
            raise ValueError("'next' should be an integer.")
        self._next = next

    # Getter value
    @property
    def value(self):
        return self._value

    # Setter for value
    @value.setter
    def value(self, value):
        self._value = value  
        # if value is empty, value = text
        if not value:
            self._value = self.text