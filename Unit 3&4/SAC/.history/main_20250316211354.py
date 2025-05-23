import os
import sys
import webbrowser  # i dunno why its called webbrowser, but it opens files up so i dont mind.
from datetime import datetime

import inventory_management as inventory


def main_menu():
    """Displays primary options to the user and asks for input"""
    print("1. View inventory")
    print("2. Add inventory")
    print("3. Remove inventory")
    print("4. Search inventory")
    print("5. Exit")

    while True:
        try:
            main_option = input("Pick an option (1-5): ")

            # Check if input is empty
            if not main_option:
                print("Please enter a number between 1 and 4")
                continue

            # Convert to integer and check range
            main_option = int(main_option)
            if main_option < 1 or main_option > 5:
                print("Please enter a number between 1 and 4")
                continue

            break
        except ValueError:
            print("Please enter a valid number between 1 and 4")

    match main_option:
        case 1:
            view_inventory()
        case 2:
            add_inventory()
        case 3:
            remove_inventory()
        case 4:
            pass
        case 5:
            print("Goodbye!")


def view_inventory():
    """Asks the user if they want to either view inventory database in either terminal or externally"""
    while True:
        clear_terminal()
        print("\nWould you like to view the inventory:")
        print("1. In console")
        print("2. Open externally")

        choice = input("Enter the number of your choice (1 or 2): ")
        if choice == "1":
            print(inventory.view_inventory())
        elif choice == "2":
            try:
                webbrowser.open("inventory.csv")
            except OSError:
                print(
                    "Error opening file externally. Please try viewing in console instead.\n"
                )
        else:
            print("Invalid input. Please enter 1 or 2.\n")
            continue

        view_again = input(
            "\nWould you like to view the inventory again? (y/n): "
        ).lower()
        if view_again != "y":
            break

    main_menu()


def add_inventory():
    while True:
        print("\nAdd new item")

        # Get and validate name
        while True:
            name = input("Enter item name: ").strip()
            if not name:
                print("Item name cannot be empty. Please try again.")
                continue
            # Remove the item_exists check since it doesn't exist
            break

        # Get and validate quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                    continue
                if quantity > 1000000:  # Reasonable upper limit
                    print("Quantity seems too large. Please try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        date_added = datetime.today().strftime("%Y-%m-%d")
        inventory.add_inventory(name, quantity, date_added)
        print("Item added successfully!")

        add_another = input("\nWould you like to add another item? (y/n): ").lower()
        if add_another != "y":
            break

    main_menu()


def remove_inventory():
    print("\nRemove item")
    name = input("Enter item name: ")
    inventory.remove_inventory(name)


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    inventory.make_inventory_file()
    main_menu()


if __name__ == "__main__":
    try:
        print("Welcome to Inventory Manager")
        main()
    # Exit if user presses Ctrl+C or Ctrl+Q
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
