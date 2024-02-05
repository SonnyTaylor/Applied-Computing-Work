# By Sonny Taylor for my Applied Computer class
# Find me and this git repo at https://github.com/SonnyTaylor/Applied-Computing-Work

# OS import used for clearing the terminal
import os

# Initialize store_inventory dictionary with a few items for an example
store_inventory = {
    "Bananas": {"quantity": 6, "price": 1.5},
    "Apples": {"quantity": 0, "price": 1.00},
    "Oranges": {"quantity": 32, "price": 1.5},
}

# Define terminal colors constants cause i dont wanna use a pip module for this like colorama
TGREEN = "\033[32m"
TWHITE = "\033[37m"
TBLUE = "\033[34m"
TRED = "\033[31m"
TBOLD = "\033[1m"
TUNDERLINE = "\033[4m"
TREVERSE = "\033[7m"

# Logo used upon opening the program
# make the logo raw dog so that theres no errors
epic_logo_i_definintly_made_myself_lol = r"""
    ____                      __                      __  ___                                 
   /  _/___ _   _____  ____  / /_____  _______  __   /  |/  /___ _____  ____ _____ ____  _____
   / // __ \ | / / _ \/ __ \/ __/ __ \/ ___/ / / /  / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 _/ // / / / |/ /  __/ / / / /_/ /_/ / /  / /_/ /  / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
/___/_/ /_/|___/\___/_/ /_/\__/\____/_/   \__, /  /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
By Sonny Taylor                          /____/                            /____/
---------------------------------------------------------------------------------------------
"""


def clear_terminal():
    """
    Clears the terminal screen.
    """
    if os.name == "nt":  # Windows
        os.system("cls")
    elif os.name == "posix":  # Sigma Linux or macOS
        os.system("clear")
    else:
        # Super niche message that most people should never see, only occurs if user doesnt run Windows, Linux or MacOS. Like seriously though, who uses anything else besides Windows, Linux, or macOS? maybe if this were in some kind of embedded program but like really though.
        print("Unsupported operating system, clearing terminal is not supported")


def user_options(clear_term_on_startup):
    """Clears the terminal of everything creating a blank terminal.

    Args:
        clear_term_on_startup (boolean): If true, clear the terminal upon being called; if false, pass.
    """
    if clear_term_on_startup:
        clear_terminal()
    print(TBLUE + "What would you like to do?" + TWHITE)
    print("1. View inventory")
    print("2. Add to inventory")
    print("3. Remove from inventory")
    print("4. Edit inventory")
    print("5. Exit")
    user_input = input("Enter number> ")
    if user_input == "1":
        view_inventory()
    elif user_input == "2":
        add_inventory()
    elif user_input == "3":
        remove_inventory()
    elif user_input == "4":
        edit_inventory()
    elif user_input == "5":
        print("Goodbye!")
        exit()
    else:
        print(TRED + "Invalid input. Please try again." + TWHITE)
        user_options(True)


def print_inventory():
    print("Current inventory: ")
    for item, details in store_inventory.items():
        quantity = details["quantity"]
        price = details["price"]
        print(f"{item}: Quantity: {quantity}, Price: {price}")
        print(TBLUE + "-------------------------------" + TWHITE)


def view_inventory():
    """
    Displays the current inventory items, their quantities, and prices.
    """
    clear_terminal()

    print_inventory()

    view_inventory_finished = input("Press enter to continue")
    if view_inventory_finished is not None:
        # return to the options
        user_options(True)


def add_inventory():
    """
    Adds a new item, its quantity, and price to the inventory.
    """
    clear_terminal()
    print("What would you like to add?")
    item = input("Enter item> ")

    # Check if item is empty
    if not item:
        print("Item cannot be empty.")
        input("Press enter to continue")
        add_inventory()
        return

    # Check if item already exists in inventory
    if item in store_inventory:
        print(f"{item} already exists in the inventory.")
        input("Press enter to continue")
        add_inventory()
        return

    print("How many would you like to add?")
    quantity = input("Enter quantity> ")

    # Check if quantity is a positive integer
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Quantity must be a positive integer.")
        input("Press enter to continue")
        add_inventory()
        return

    print("What is the price of the item?")
    price = input("Enter price> ")

    try:
        # Convert price to a float
        price = float(price)
        # Add item to store_inventory dictionary
        store_inventory[item] = {"quantity": quantity, "price": price}
        print(
            TBLUE
            + f"{item} added to inventory with quantity {quantity} and price ${price}"
            + TWHITE
        )
        input("Press enter to continue")
        user_options(True)

    # TODO - Add a way to exit from an input so that the user doesnt need to exit the whole program if they make a mistake
    except ValueError:
        print("Price must be a number.")
        input("Press enter to continue")
        add_inventory()
        return


def edit_inventory():
    """Allows the user to edit the quantity and/or price of an item in the inventory."""
    clear_terminal()
    # If there are not items in inventory, return to the options
    if not store_inventory:
        print(TRED + "Warning: No items in inventory." + TWHITE)
        no_items_continue = input("Press enter to continue")
        if no_items_continue is not None:
            user_options(True)
        else:
            user_options(True)
    else:
        for item, details in store_inventory.items():
            quantity = details["quantity"]
            price = details["price"]
            print(f"{item}: Quantity: {quantity}, Price: {price}")
            print(TBLUE + "-------------------------------" + TWHITE)
    print("What would you like to edit?")
    item = input("Enter item> ")

    # Check if item is in inventory
    if item not in store_inventory:
        print(f"{item} does not exist in the inventory.")
        print(TBLUE + "-------------------------------" + TWHITE)
        item_dont_exist = input("Press enter to continue")
        if item_dont_exist is not None:
            edit_inventory()
        return

    print("What is the new quantity?")
    quantity = int(input("Enter quantity> "))
    print("What is the new price?")
    price = float(input("Enter price> "))
    # if the price is not a float, convert it to a float
    if not isinstance(price, float):
        price = float(price)

    # Update the item in the inventory
    store_inventory[item]["quantity"] = quantity
    store_inventory[item]["price"] = price
    print(f"{item} quantity updated to {quantity}")
    print(f"{item} price updated to {price}")
    print(TBLUE + "-------------------------------" + TWHITE)
    # Return to the options
    user_options(True)


def remove_inventory():
    """
    Removes an item from inventory
    """
    clear_terminal()

    print_inventory()

    print("What would you like to remove?")
    item = input("Enter item> ")

    # Check if item is in inventory
    if item not in store_inventory:
        print(f"{item} does not exist in the inventory.")
        print(TBLUE + "-------------------------------" + TWHITE)
        item_dont_exist = input("Press enter to continue")
        if item_dont_exist is not None:
            remove_inventory()
        return

    # Delete item from inventory
    store_inventory.pop(item, None)
    print(f"{item} removed from inventory")
    print(TBLUE + "-------------------------------" + TWHITE)
    view_inventory_finished = input("Press enter to continue")
    if view_inventory_finished is not None:
        # Return to the options
        user_options(True)

    # Return to options
    user_options(True)


# Print starting message
print(TGREEN + epic_logo_i_definintly_made_myself_lol + TWHITE)

# Start the program
if __name__ == "__main__":
    try:
        # Show option, false shows the unicode art on startup because it doesnt clear the terminal
        user_options(False)

    # if user does like ctrl+c exit the program, just prevent showing errors and stuff
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
