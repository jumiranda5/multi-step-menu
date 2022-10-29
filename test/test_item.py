import pytest
from menusteps.item import Item

def test_text():
    with pytest.raises(ValueError):
        Item("", "0")
    with pytest.raises(ValueError):
        Item(None, "0")


def test_next():
    with pytest.raises(ValueError):
        Item("text", "0")


def test_value():
    assert Item("text", 0, "value").value == "value"
    assert Item("text", 0, "").value == "text"
    assert Item("text", 0).value == "text"