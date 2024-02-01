# Initialize store_inventory dictionary with a few items
store_inventory = {
    "Bananas": 6,
    "Apples": 0,
    "Oranges": 32,
}

def user_options():
    """
    Displays the available options to the user and performs the selected action.
    """
    print("What would you like to do?")
    print("1. View inventory")
    print("2. Add to inventory")
    print("3. Remove from inventory")
    print("4. Exit")
    user_input = input("Enter number> ")
    if user_input == "1":
        view_inventory()
    elif user_input == "2":
        add_inventory()
    elif user_input == "3":
        remove_inventory()
    elif user_input == "4":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input. Please try again.")

def view_inventory():
    """
    Displays the current inventory items and their quantities.
    """
    for item in store_inventory:
        print(f"{item}: {store_inventory[item]}")

def add_inventory():
    """
    Adds a new item and its quantity to the inventory.
    """
    print("What would you like to add?")
    item = input("Enter item> ")
    print("How many would you like to add?")
    quantity = input("Enter quantity> ")
    store_inventory[item] = quantity
    print(f"{quantity} {item} added to inventory")

def remove_inventory():
    """
    Removes a specified quantity of an item from the inventory.
    """
    print("What would you like to remove?")
    item = input("Enter item> ")
    print("How many would you like to remove?")
    quantity = input("Enter quantity> ")
    store_inventory[item] = quantity
    print(f"{quantity} {item} removed from inventory")

# Ask user what they want to do
print("Welcome to the generic store Inventory Manager!")
user_options()