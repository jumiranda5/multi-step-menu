# Multi-Step Menu

Multi-step menu is a Python package to use in command-line applications that needs menus with multiple steps.

## Installation

This package has not been uploaded to PyPI (at least not yet).

Therefore, you need to download the menusteps folder and place it on your project.


## Usage

```python
from menusteps import menu
from menusteps.item import Item
from menusteps.option import Option
from menusteps.step import Step


# List of steps
# menusteps uses the main Fore colors of the library Colorama
# Step(id, title, input_text="Type the option number: ", color="white")
steps = [
    Step(0, "What would you like for lunch today?", color="cyan"),
    Step(1, "What would you like to drink?", color="magenta"),
    Step(2, "Would you like dessert?", color="green"),
]


# List of options for the menu steps
# Each option contains a list of items
# Item(text, next, value=""), where next = next option id and value = value to return (defaut value is the text)
options = [
    Option(0, [Item("Cheeseburger and fries", 1), Item("Pizza", 1), Item("Spaghetti", 1)]),
    Option(1, [Item("Coke", 2), Item("Orange juice", 2), Item("Nothing", 2)]),
    Option(2, [Item("Icecream", 0), Item("Cheesecake", 0), Item("Chocolate cake", 0)]),
]


def main():
    # start multi-step menu
    # "Back" and "Cancel" will be added automatically
    # returns a list with the chosen items from each step
    choices = menu.start(options, steps)
    print(f"Choices: {choices}\n")


if __name__ == "__main__":
    main()
```

## License
[MIT](https://github.com/jumiranda5/multi-step-menu/blob/main/LICENSE.md)
