from menusteps import menu
from menusteps.item import Item
from menusteps.option import Option
from menusteps.step import Step
from colorama import Fore, Style

# Options items lists:
# Item(text, next, value=""),
# where next = next option id and value = value to return (defaut value is the text)

main_menu = [
        Item("Length", 1), 
        Item("Temperature", 2), 
        Item("Volume", 3), 
        Item("Mass", 4)
]


length_menu = [
    Item("Feet", 1), 
    Item("Inches", 1), 
    Item("Miles", 1), 
    Item("Yards", 1), 
    Item("Kilometers", 1), 
    Item("Meters", 1), 
    Item("Centimeter", 1), 
    Item("Millimeter", 1)
]


temperature_menu = [
    Item("Celcius", 2), 
    Item("Fahrenheit", 2)
]


volume_menu = [
    Item("Gallon", 3), 
    Item("Liter", 3), 
    Item("Mililliter", 3), 
    Item("Ounce", 3)
]


weight_menu = [
    Item("Pound", 4), 
    Item("Ounce", 4), 
    Item("Kilogram", 4), 
    Item("Gram", 4)
]


# List of options for the menu steps
options = [
    # step 1 (id=0)
    Option(0, main_menu),
    # step 2 (id=1) and step 3 (id=2)
    Option(1, length_menu),
    Option(2, temperature_menu),
    Option(3, volume_menu),
    Option(4, weight_menu),
]


# List of steps:
steps = [
    Step(0, "What would you like to convert?", color="cyan"),
    Step(1, "Convert from:", color="magenta"),
    Step(2, "Convert to:", color="green"),
]

def main():
    print_welcome()

    # start multi-step menu
    # "Back" and "Cancel" will be added automatically
    # returns a list with the chosen items from each step
    choices = menu.start(options, steps)
    print(choices)


def print_welcome():
    print(Fore.YELLOW + "\n-------------------------------------------")
    print("       Welcome to Metrics Converter!")
    print("-------------------------------------------\n" + Style.RESET_ALL)


if __name__ == "__main__":
    main()