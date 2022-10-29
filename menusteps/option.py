from .item import Item

# option = {"id": 0, "items": [Item("option 1", 1)]}

# Class for single option
class Option:
    def __init__(self, id, items):
        self.id = id
        self.items = items

    # Getter for id
    @property
    def id(self):
        return self._id

    # Setter for id
    @id.setter
    def id(self, id):
        # id must be an integer
        if not isinstance(id, int):
            raise ValueError("'id' should be an integer.")
        self._id = id

    # Getter for items
    @property
    def items(self):
        return self._items

    # Setter for id
    @items.setter
    def items(self, items):
        # item must be from Item class
        for item in items:
            if not isinstance(item, Item):
                raise ValueError("Invalid option item. Use class Item")

        self._items = items