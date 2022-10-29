from colorama import Fore, Style
from menusteps import menu
from menusteps.item import Item
from menusteps.option import Option
from menusteps.step import Step
from colorama import Fore, Style


options = [
    Option(0, [Item("Cheeseburger and fries", 1), Item("Pizza", 1), Item("Spaghetti", 1)]),
    Option(1, [Item("Coke", 2), Item("Orange juice", 2), Item("Nothing", 2)]),
    Option(2, [Item("Icecream", 0), Item("Cheesecake", 0), Item("Chocolate cake", 0)]),
]


steps = [
    Step(0, "What would you like for lunch today?", color="cyan"),
    Step(1, "What would you like to drink?", color="magenta"),
    Step(2, "Would you like dessert?", color="green"),
]


def main():
    print_welcome()
    choices = menu.start(options, steps)
    print(f"Choices: {choices}\n")


def print_welcome():
    print(Fore.YELLOW + "\n-------------------------------------------")
    print("       Welcome to Multi Step Menu!")
    print("-------------------------------------------\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
    