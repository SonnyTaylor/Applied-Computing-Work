import sys
import inventory_management as inventory
import webbrowser  # i dunno why its called webbrowser, but it opens files up so i dont mind.
from datetime import datetime


def main_menu():
    """Displays primary options to the user and asks for input"""
    print("1. View inventory")
    print("2. Add inventory")
    print("3. Remove inventory")
    print("4. Search inventory")

    main_option = int(input("Pick an option (1-4): "))

    match main_option:
        case 1:
            view_inventory()
        case 2:
            add_inventory()
        case 3:
            remove_inventory()
        case 4:
            pass


def view_inventory():
    """Asks the user if they want to either view inventory database in either terminal or externally"""
    print("\nWould you like to view the inventory:")
    print("1. In console")
    print("2. Open externally")

    choice = input("Enter the number of your choice (1 or 2): ")
    if choice == "1":
        print(inventory.view_inventory())
    elif choice == "2":
        webbrowser.open("inventory.csv")
    else:
        print("Invalid input. Please enter 1 or 2.\n")


def add_inventory():
    print("\nAdd new item")
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    date_added = datetime.today().strftime("%Y-%m-%d")  # Got this off stackoverflow
    inventory.add_inventory(name, quantity, date_added)
    print("Item added!")


def remove_inventory():
    print("\nRemove item")
    name = input("Enter item name: ")
    inventory.remove_inventory


def main():
    inventory.make_inventory_file()
    main_menu()


if __name__ == "__main__":
    try:
        print("Welcome to Inventory Manager")
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
