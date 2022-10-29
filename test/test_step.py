import pytest
from menusteps.step import Step

# Step(0, "Step 1:", "Type the option number: ")

def test_id():
    assert Step(0, "Title", "Input text").id == 0
    with pytest.raises(ValueError):
        Step("id", "Title", "Input text")
    with pytest.raises(ValueError):
        Step(None, "Title", "Input text")


def test_title():
    assert Step(0, "").title == ""
    assert Step(0).title == ""
    assert Step(0, None).title == ""


def test_input():
    assert Step(0, "Title", input_text="").input_text == ""
    assert Step(0, "Title").input_text == "Type the option number: "
    assert Step(0, "Title", input_text="").input_text == ""


def test_color():
    #colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    assert Step(0, color="purple").color == "white"
    assert Step(0, color="").color == "white"
    assert Step(0, color=1).color == "white"
    assert Step(0, color=None).color == "white"
    assert Step(0, color="black").color == "black"
    assert Step(0, color="red").color == "red"
    assert Step(0, color="green").color == "green"
    assert Step(0, color="yellow").color == "yellow"
    assert Step(0, color="blue").color == "blue"
    assert Step(0, color="magenta").color == "magenta"
    assert Step(0, color="cyan").color == "cyan"
    assert Step(0, color="white").color == "white"
    


