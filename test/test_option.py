import pytest
from item import Item
from option import Option


options = [
    Option(0, [Item("option 1", 1), Item("option 2", 2)]),
    Option(1, [Item("option 3", 3), Item("option 4", 3)]),
    Option(2, [Item("option 5", 3), Item("option 6", 3)]),
    Option(3, [Item("option 6", 0), Item("option 7", 0)]),
]


def test_option_id():
    with pytest.raises(ValueError):
        Option(None, [])
    with pytest.raises(ValueError):
        Option("id", [])
    assert Option(0, []).id == 0


def test_option_first_item():
    with pytest.raises(ValueError):
        Option(0, ["Item"])
    