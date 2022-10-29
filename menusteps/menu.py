from .option import Option
from .step import Step
from .item import Item
from colorama import Fore, Style


def start(menu, steps):

    # init list object
    options = create_options_list(menu)

    # vars to track menu choices
    step_count = len(steps)
    current_step = 0
    prev_step = 0
    track = [0]
    current_menu = 0
    choices = []

    while True: 
        # If last step, end loop       
        if current_step == step_count:
            break

        # vars
        step = steps[current_step]
        items = options[current_menu].items
        color = get_color(step.color)

        # print current menu
        print_menu(step, items, color)

        # handle user input
        choice = get_user_choice(steps, current_step, items, color)
        item = items[choice - 1]

        # Get next step and update track and choices lists
        next_step, choices, track = handle_step(item, choices, track)

        # update step 
        if next_step == 1:
            prev_step += 1
            current_step += 1
        else:
            prev_step -= 1
            current_step -= 1  

        # update step menu
        current_menu = track[len(track) - 1]

        # handle exit option
        if item.value == "cancel":
            return

    return choices


def create_options_list(options, back="Back", cancel="Cancel"):
    # Check if ids are valid (in order, starting from 0)
    for i in range(len(options)):
        # Check ids
        id = options[i].id
        if id != i:
            raise ValueError(f"Item id:{id} should be {i}")
        
        # Check items
        for item in options[i].items:
            if not isinstance(item, Item):
                raise ValueError("Invalid option item. Use class Item")
    
    # Add exit and back options
    for option in options:
        if not option.id == 0:
            option.items.append(Item(back, 0, "back"))
        option.items.append(Item(cancel, 0, "cancel"))

    return options


def get_color(name):
    match name:
        case "black":
            return Fore.BLACK
        case "red":
            return Fore.RED
        case "green":
            return Fore.GREEN
        case "yellow":
            return Fore.YELLOW
        case "blue":
            return Fore.BLUE
        case "magenta":
            return Fore.MAGENTA
        case "cyan":
            return Fore.CYAN
        case _:
            return Fore.WHITE


def print_menu(step, items, color):

    # print step title
    print(color + step.title)

    # print step options
    for i in range(len(items)):
        print(f"{color}{i + 1}.{Style.RESET_ALL}{items[i].text}")


def get_user_choice(steps, index, items, color):
    print()
    while True: 
        try:
            choice = int(input(f"{steps[index].input_text}"))
            if not 0 < choice <= len(items):
                raise ValueError
            break
        except ValueError:
            print(f"{Fore.RED}Input should be a number from 1 to {len(items)}")

    print(f"{color}=> {items[choice - 1].text}{Style.RESET_ALL}")
    print("")

    return choice


def handle_step(item, choices, track):
    if item.value == "back":
        next_step = -1  
        choices.pop()
        track.pop()
    else:
        next_step = 1
        choices.append(item.value)
        track.append(item.next)

    return (next_step, choices, track)


'''
if __name__ == "__main__":
    main()
'''