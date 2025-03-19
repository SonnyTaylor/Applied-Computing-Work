import os
import sys
import webbrowser
from datetime import datetime
from inventory_classes import InventoryManager

# Create a global inventory manager instance
inventory_manager = InventoryManager()


def main_menu():
    """Displays primary options to the user and asks for input"""
    print("1. View inventory")
    print("2. Add inventory")
    print("3. Remove inventory")
    print("4. Search inventory")
    print("5. Sort inventory")
    print("6. Exit")

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
            search_inventory()
        case 5:
            sort_inventory()
        case 6:
            print("Goodbye!")
            sys.exit(0)


def view_inventory():
    """Asks the user if they want to either view inventory database in either terminal or externally"""
    while True:
        clear_terminal()
        print("\nWould you like to view the inventory:")
        print("1. In console")
        print("2. Open externally")

        choice = input("Enter the number of your choice (1 or 2): ")
        if choice == "1":
            print(inventory_manager.view_inventory())
        elif choice == "2":
            try:
                webbrowser.open(inventory_manager.filename)
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


def sort_inventory():
    while True:
        # Check if inventory exists
        if not inventory_manager.items:
            print("\nInventory is empty. Nothing to sort.")
            break

        print("\nSort inventory")
        print("1. Sort by name")
        print("2. Sort by quantity")
        print("3. Sort by date added")
        print("4. Sort by price")

        try:
            sort_option = input("Enter the number of your choice (1-4): ")

            # Type check and validate input
            if not sort_option.isdigit():
                print("Please enter a number between 1 and 4.")
                continue

            sort_option = int(sort_option)
            if sort_option not in [1, 2, 3, 4]:
                print("Please enter a number between 1 and 4.")
                continue

            # Try to sort based on option
            try:
                if sort_option == 1:
                    inventory_manager.sort_by_name()
                elif sort_option == 2:
                    inventory_manager.sort_by_quantity()
                elif sort_option == 3:
                    inventory_manager.sort_by_date_added()
                elif sort_option == 4:
                    inventory_manager.sort_by_price()
                print("Inventory sorted successfully!")
            except Exception as e:
                print(f"Error sorting inventory: {e}")
                continue

        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        # Validate sort again input
        while True:
            sort_again = input("\nWould you like to sort again? (y/n): ").lower()
            if sort_again in ["y", "n"]:
                break
            print("Please enter 'y' or 'n'")

        if sort_again != "y":
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
                
        # Get and validate price
        while True:
            try:
                price = float(input("Enter price: "))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break

        if inventory_manager.add_item(name, quantity):
            print("Item added successfully!")
        else:
            print("Failed to add item. Please try again.")

        add_another = input("\nWould you like to add another item? (y/n): ").lower()
        if add_another != "y":
            break

    main_menu()


def remove_inventory():
    print("\nRemove item")
    name = input("Enter item name: ")
    if inventory_manager.remove_item(name):
        print("Item removed successfully!")
    else:
        print("Failed to remove item. Please try again.")
    main_menu()


def search_inventory():
    print("\nSearch inventory")
    name = input("Enter item name to search: ")
    item = inventory_manager.search_item(name)
    if item:
        print(f"\nFound item:")
        print(f"Name: {item.name}")
        print(f"Quantity: {item.quantity}")
        print(f"Date Added: {item.date_added}")
    else:
        print("Item not found.")
    main_menu()


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    main_menu()


if __name__ == "__main__":
    try:
        print("Welcome to Inventory Manager")
        main()
    # Exit if user presses Ctrl+C or Ctrl+Q
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)
