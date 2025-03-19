import os
import sys
import webbrowser
from datetime import datetime
from inventory_classes import InventoryManager

# Create a global inventory manager instance
inventory_manager = InventoryManager()


def print_header():
    """Print the application header"""
    clear_terminal()
    HEADER_ASCII = """
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║  ██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ██╗   ██╗   ║
║  ██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝   ║
║  ██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝ ╚████╔╝    ║
║  ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝     ║
║  ██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║   ██║      ║
║  ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝"""
    print(HEADER_ASCII)


def print_menu_header(title):
    """Print a section header"""
    print(f"\n{'=' * 50}")
    print(f"{title:^50}")
    print(f"{'=' * 50}\n")


def main_menu():
    """Displays primary options to the user and asks for input"""
    print_header()
    print_menu_header("MAIN MENU")
    print(
        "╔════════════════════════════════════════════════════════════════════════════════╗"
    )
    print(
        "║                                                                                ║"
    )
    print(
        "║  1. 📋 View Inventory                                                          ║"
    )
    print(
        "║  2. ➕ Add New Item                                                            ║"
    )
    print(
        "║  3. ❌ Remove Item                                                             ║"
    )
    print(
        "║  4. 🔍 Search Inventory                                                        ║"
    )
    print(
        "║  5. 📊 Sort Inventory                                                          ║"
    )
    print(
        "║  6. 🚪 Exit                                                                    ║"
    )
    print(
        "║                                                                                ║"
    )
    print(
        "╚════════════════════════════════════════════════════════════════════════════════╝"
    )

    while True:
        try:
            main_option = input("\nEnter your choice (1-6): ")

            if not main_option:
                print("❌ Please enter a number between 1 and 6")
                continue

            main_option = int(main_option)
            if main_option < 1 or main_option > 6:
                print("❌ Please enter a number between 1 and 6")
                continue

            break
        except ValueError:
            print("❌ Please enter a valid number between 1 and 6")

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
            print("\n👋 Thank you for using Inventory Manager! Goodbye!")
            sys.exit(0)


def view_inventory():
    """Asks the user if they want to either view inventory database in either terminal or externally"""
    while True:
        print_header()
        print_menu_header("VIEW INVENTORY")
        print(
            "╔════════════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            "║                                                                                ║"
        )
        print(
            "║  1. 📱 View in Console                                                       ║"
        )
        print(
            "║  2. 💻 Open in External Editor                                               ║"
        )
        print(
            "║                                                                                ║"
        )
        print(
            "╚════════════════════════════════════════════════════════════════════════════════╝"
        )

        choice = input("\nEnter your choice (1-2): ")
        if choice == "1":
            print("\n📋 Current Inventory:")
            print("=" * 50)
            print(inventory_manager.view_inventory())
        elif choice == "2":
            try:
                webbrowser.open(inventory_manager.filename)
                print("\n✅ File opened in external editor")
            except OSError:
                print(
                    "\n❌ Error opening file externally. Please try viewing in console instead."
                )
        else:
            print("\n❌ Invalid input. Please enter 1 or 2.")
            continue

        view_again = input(
            "\nWould you like to view the inventory again? (y/n): "
        ).lower()
        if view_again != "y":
            break

    main_menu()


def sort_inventory():
    while True:
        print_header()
        print_menu_header("SORT INVENTORY")

        if not inventory_manager.items:
            print("\n❌ Inventory is empty. Nothing to sort.")
            break

        print(
            "╔════════════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            "║                                                                                ║"
        )
        print(
            "║  1. 📝 Sort by Name                                                          ║"
        )
        print(
            "║  2. 🔢 Sort by Quantity                                                      ║"
        )
        print(
            "║  3. 📅 Sort by Date Added                                                    ║"
        )
        print(
            "║  4. 💰 Sort by Price                                                         ║"
        )
        print(
            "║                                                                                ║"
        )
        print(
            "╚════════════════════════════════════════════════════════════════════════════════╝"
        )

        try:
            sort_option = input("\nEnter your choice (1-4): ")

            if not sort_option.isdigit():
                print("\n❌ Please enter a number between 1 and 4.")
                continue

            sort_option = int(sort_option)
            if sort_option not in [1, 2, 3, 4]:
                print("\n❌ Please enter a number between 1 and 4.")
                continue

            try:
                if sort_option == 1:
                    inventory_manager.sort_by_name()
                elif sort_option == 2:
                    inventory_manager.sort_by_quantity()
                elif sort_option == 3:
                    inventory_manager.sort_by_date_added()
                elif sort_option == 4:
                    inventory_manager.sort_by_price()
                print("\n✅ Inventory sorted successfully!")
            except Exception as e:
                print(f"\n❌ Error sorting inventory: {e}")
                continue

        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            continue

        while True:
            sort_again = input("\nWould you like to sort again? (y/n): ").lower()
            if sort_again in ["y", "n"]:
                break
            print("❌ Please enter 'y' or 'n'")

        if sort_again != "y":
            break

    main_menu()


def add_inventory():
    while True:
        print_header()
        print_menu_header("ADD NEW ITEM")
        print(
            "╔════════════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            "║                                                                                ║"
        )
        print(
            "║  Please enter the following information:                                       ║"
        )
        print(
            "║                                                                                ║"
        )
        print(
            "╚════════════════════════════════════════════════════════════════════════════════╝"
        )

        while True:
            name = input("\n📝 Enter item name: ").strip()
            if not name:
                print("❌ Item name cannot be empty. Please try again.")
                continue
            break

        while True:
            try:
                quantity = int(input("🔢 Enter quantity: "))
                if quantity < 0:
                    print("❌ Quantity cannot be negative. Please try again.")
                    continue
                if quantity > 1000000:
                    print("❌ Quantity seems too large. Please try again.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")

        while True:
            try:
                price = float(input("💰 Enter price: "))
                if price < 0:
                    print("❌ Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number.")

        if inventory_manager.add_item(name, quantity, price):
            print("\n✅ Item added successfully!")
        else:
            print("\n❌ Failed to add item. Please try again.")

        add_another = input("\nWould you like to add another item? (y/n): ").lower()
        if add_another != "y":
            break

    main_menu()


def remove_inventory():
    print_header()
    print_menu_header("REMOVE ITEM")
    print(
        "╔════════════════════════════════════════════════════════════════════════════════╗"
    )
    print(
        "║                                                                                ║"
    )
    print(
        "║  Enter the name of the item you want to remove:                                ║"
    )
    print(
        "║                                                                                ║"
    )
    print(
        "╚════════════════════════════════════════════════════════════════════════════════╝"
    )

    name = input("\n📝 Enter item name: ")
    if inventory_manager.remove_item(name):
        print("\n✅ Item removed successfully!")
    else:
        print("\n❌ Failed to remove item. Please try again.")
    main_menu()


def search_inventory():
    print_header()
    print_menu_header("SEARCH INVENTORY")
    print(
        "╔════════════════════════════════════════════════════════════════════════════════╗"
    )
    print(
        "║                                                                                ║"
    )
    print(
        "║  Enter the name of the item you want to search:                                ║"
    )
    print(
        "║                                                                                ║"
    )
    print(
        "╚════════════════════════════════════════════════════════════════════════════════╝"
    )

    name = input("\n🔍 Enter item name to search: ")
    item = inventory_manager.search_item(name)
    if item:
        print("\n✅ Found item:")
        print("=" * 50)
        print(f"📝 Name: {item.name}")
        print(f"🔢 Quantity: {item.quantity}")
        print(f"💰 Price: ${item.price:.2f}")
        print(f"📅 Date Added: {item.date_added}")
    else:
        print("\n❌ Item not found.")
    main_menu()


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n👋 Thank you for using Inventory Manager! Goodbye!")
        sys.exit(0)
