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
    else:  # Sigma Linux or macOS
        os.system("clear")


def user_options(clear_term_on_startup):
    """Clears the terminal of everthing creating a blank terminal

    Args:
        clear_term (boolean): If true, clear the terminal upon being called, if false pass
    """
    if clear_term_on_startup == True:
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


def view_inventory():
    """
    Displays the current inventory items, their quantities, and prices.
    """
    clear_terminal()
    print("Current inventory:")
    for item, details in store_inventory.items():
        quantity = details["quantity"]
        price = details["price"]
        print(f"{item}: Quantity: {quantity}, Price: {price}")
        print(TBLUE + "-------------------------------" + TWHITE)
    view_inventory_finished = input("Press enter to continue")
    if view_inventory_finished == "":
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
        add_inventory_item_error = input("Press enter to continue")
        if add_inventory_item_error == "":
            # Return to the start
            add_inventory()
        add_inventory()
        return

    print("How many would you like to add?")
    quantity = input("Enter quantity> ")

    # Check if quantity is a positive integer
    if not quantity.isdigit():
        print("Quantity must be a positive integer.")
        add_inventory_quantity_error = input("Press enter to continue")
        if add_inventory_quantity_error == "":
            # Return to the start
            add_inventory()
        add_inventory()
        return
    quantity = int(quantity)

    print("What is the price of the item?")
    price = input("Enter price> ")

    try:
        price = float(price)
    except ValueError:
        print("Price must be a number.")
        add_inventory_price_error = input("Press enter to continue")
        if add_inventory_price_error == "":
            # Return to the start
            add_inventory()
        add_inventory()
        return


def edit_inventory():
    """Allows the user to edit the quantity and/or price of an item in the inventory."""
    clear_terminal()
    for item, details in store_inventory.items():
        quantity = details["quantity"]
        price = details["price"]
        print(f"{item}: Quantity: {quantity}, Price: {price}")
        print("-------------------------------")
    print("What would you like to edit?")
    item = input("Enter item> ")

    # Check if item is in inventory
    if item not in store_inventory:
        print(f"{item} does not exist in the inventory.")
        print("-------------------------------")
        item_dont_exist = input("Press enter to continue")
        if item_dont_exist == "":
            edit_inventory()
        return

    print("What is the new quantity?")
    quantity = int(input("Enter quantity> "))
    print("What is the new price?")
    price = float(input("Enter price> "))
    # if the price is not a float, convert it to a float
    if not isinstance(price, float):
        price = float(price)

    # update the item in the inventory
    store_inventory[item]["quantity"] = quantity
    store_inventory[item]["price"] = price
    print(f"{item} quantity updated to {quantity}")
    print(f"{item} price updated to {price}")
    print("-------------------------------")
    # return to the options
    user_options(True)


def remove_inventory():
    """
    Removes an item from inventory
    """
    clear_terminal()
    # print the current inventory
    for item, details in store_inventory.items():
        quantity = details["quantity"]
        price = details["price"]
        print(f"{item}: Quantity: {quantity}, Price: {price}")
        print("-------------------------------")
    print("What would you like to remove?")
    item = input("Enter item> ")

    # Check if item is in inventory
    if item not in store_inventory:
        print(f"{item} does not exist in the inventory.")
        print("-------------------------------")
        item_dont_exist = input("Press enter to continue")
        if item_dont_exist == "":
            remove_inventory()
        return

    # delete item from inventory
    store_inventory.pop(item, None)
    print(f"{item} removed from inventory")
    print("-------------------------------")
    view_inventory_finished = input("Press enter to continue")
    if view_inventory_finished == "":
        # return to the options
        user_options(True)

    # return to options
    user_options(True)


# print starting message
print(TGREEN + epic_logo_i_definintly_made_myself_lol + TWHITE)

# start the program
if __name__ == "__main__":
    try:
        user_options(False)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
