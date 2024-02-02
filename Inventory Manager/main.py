# OS import used for clearing the terminal
import os

# Initialize store_inventory dictionary with a few items
store_inventory = {
    "Bananas": {"quantity": 6, "price": 1.5},
    "Apples": {"quantity": 0, "price": 1.00},
    "Oranges": {"quantity": 32, "price": 1.5},
}

# Define terminal colors
# TODO Make the logo green
TGREEN = '\033[32m' 

epic_logo_i_definintly_made_myself_lol = """
    ____                      __                      __  ___                                 
   /  _/___ _   _____  ____  / /_____  _______  __   /  |/  /___ _____  ____ _____ ____  _____
   / // __ \ | / / _ \/ __ \/ __/ __ \/ ___/ / / /  / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 _/ // / / / |/ /  __/ / / / /_/ /_/ / /  / /_/ /  / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
/___/_/ /_/|___/\___/_/ /_/\__/\____/_/   \__, /  /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                         /____/                            /____/
---------------------------------------------------------------------------------------------
"""

def clear_terminal():
    """
    Clears the terminal screen.
    """
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux or macOS
        os.system("clear")

def user_options(clear_term):
    """Clears the terminal of everthing creating a blank terminal

    Args:
        clear_term (boolean): If true, clear the terminal upon being called, if false pass
    """
    if clear_term == True:
        clear_terminal()
    print("What would you like to do?")
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
        print("Invalid input. Please try again.")

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
        print("-------------------------------")
    user_options(True)

def add_inventory():
    """
    Adds a new item, its quantity, and price to the inventory.
    """
    clear_terminal()
    print("What would you like to add?")
    item = input("Enter item> ")
    print("How many would you like to add?")
    quantity = input("Enter quantity> ")
    print("What is the price of the item?")
    price = input("Enter price> ")
    store_inventory[item] = {"quantity": quantity, "price": price}
    print(f"{quantity} {item} added to inventory")
    print("-------------------------------")
    user_options(True)
    
def edit_inventory():
    """Allows the user to edit the quantity and/or price of an item in the inventory."""
    clear_terminal()
    print("What would you like to edit?")
    item = input("Enter item> ")
    print("What is the new quantity?")
    quantity = input("Enter quantity> ")
    print("What is the new price?")
    price = input("Enter price> ")
    store_inventory[item]["quantity"] = quantity
    store_inventory[item]["price"] = price
    print(f"{item} quantity updated to {quantity}")
    print(f"{item} price updated to {price}")
    print("-------------------------------")
    user_options(True)

def remove_inventory():
    """
    Removes a specified quantity of an item from the inventory.
    """
    clear_terminal()
    print("What would you like to remove?")
    item = input("Enter item> ")
    print("How many would you like to remove?")
    quantity = input("Enter quantity> ")
    store_inventory[item] = quantity
    print(f"{quantity} {item} removed from inventory")
    print("-------------------------------")
    user_options(True)

# print starting message and ask user what they want to do
print("Welcome to the generic store Inventory Manager!")
print(epic_logo_i_definintly_made_myself_lol)
user_options(False)