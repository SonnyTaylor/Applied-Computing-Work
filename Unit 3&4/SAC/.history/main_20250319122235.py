import os
import sys
import webbrowser
from datetime import datetime
from inventory_classes import InventoryManager
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.layout import Layout
from rich.text import Text
from rich import print as rprint

# Create a global inventory manager instance
inventory_manager = InventoryManager()
console = Console()


def print_header():
    """Print the application header"""
    clear_terminal()
    title = Text("INVENTORY MANAGER", style="bold blue")
    console.print(Panel(title, style="bold white", border_style="blue"))


def print_menu_header(title):
    """Print a section header"""
    console.print(Panel(title, style="bold green", border_style="green"))


def create_menu_table():
    """Create a table for the main menu"""
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_row("1. 📋", "View Inventory")
    table.add_row("2. ➕", "Add New Item")
    table.add_row("3. ❌", "Remove Item")
    table.add_row("4. 🔍", "Search Inventory")
    table.add_row("5. 📊", "Sort Inventory")
    table.add_row("6. 🚪", "Exit")
    return table


def main_menu():
    """Displays primary options to the user and asks for input"""
    print_header()
    print_menu_header("MAIN MENU")
    console.print(create_menu_table())

    while True:
        try:
            main_option = Prompt.ask(
                "\nEnter your choice", choices=["1", "2", "3", "4", "5", "6"]
            )
            break
        except ValueError:
            console.print("❌ Please enter a valid number between 1 and 6", style="red")

    match main_option:
        case "1":
            view_inventory()
        case "2":
            add_inventory()
        case "3":
            remove_inventory()
        case "4":
            search_inventory()
        case "5":
            sort_inventory()
        case "6":
            console.print(
                "\n👋 Thank you for using Inventory Manager! Goodbye!",
                style="bold green",
            )
            sys.exit(0)


def view_inventory():
    """Asks the user if they want to either view inventory database in either terminal or externally"""
    while True:
        print_header()
        print_menu_header("VIEW INVENTORY")

        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_row("1. 📱", "View in Console")
        table.add_row("2. 💻", "Open in External Editor")
        table.add_row("3. ❌", "Exit")
        console.print(table)

        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3"])

        if choice == "1":
            console.print("\n📋 Current Inventory:", style="bold")
            inventory_data = inventory_manager.view_inventory()
            console.print(
                Panel(inventory_data, title="Inventory List", border_style="blue")
            )
        elif choice == "2":
            try:
                webbrowser.open(inventory_manager.filename)
                console.print("\n✅ File opened in external editor", style="green")
            except OSError:
                console.print(
                    "\n❌ Error opening file externally. Please try viewing in console instead.",
                    style="red",
                )

        elif choice == "3":
            break

        if not Confirm.ask("\nWould you like to view the inventory again?"):
            break

    main_menu()


def sort_inventory():
    while True:
        print_header()
        print_menu_header("SORT INVENTORY")

        if not inventory_manager.items:
            console.print("\n❌ Inventory is empty. Nothing to sort.", style="red")
            break

        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_row("1. 📝", "Sort by Name")
        table.add_row("2. 🔢", "Sort by Quantity")
        table.add_row("3. 📅", "Sort by Date Added")
        table.add_row("4. 💰", "Sort by Price")
        console.print(table)

        try:
            sort_option = Prompt.ask(
                "\nEnter your choice", choices=["1", "2", "3", "4"]
            )

            if sort_option == "1":
                inventory_manager.sort_by_name()
            elif sort_option == "2":
                inventory_manager.sort_by_quantity()
            elif sort_option == "3":
                inventory_manager.sort_by_date_added()
            elif sort_option == "4":
                inventory_manager.sort_by_price()
            console.print("\n✅ Inventory sorted successfully!", style="green")

        except Exception as e:
            console.print(f"\n❌ Error sorting inventory: {e}", style="red")
            continue

        if not Confirm.ask("\nWould you like to sort again?"):
            break

    main_menu()


def add_inventory():
    while True:
        print_header()
        print_menu_header("ADD NEW ITEM")
        console.print(Panel("Please enter the following information:", style="bold"))

        name = Prompt.ask("\n📝 Enter item name").strip()
        while not name:
            console.print(
                "❌ Item name cannot be empty. Please try again.", style="red"
            )
            name = Prompt.ask("📝 Enter item name").strip()

        while True:
            try:
                quantity = int(Prompt.ask("🔢 Enter quantity"))
                if quantity < 0:
                    console.print(
                        "❌ Quantity cannot be negative. Please try again.", style="red"
                    )
                    continue
                if quantity > 1000000:
                    console.print(
                        "❌ Quantity seems too large. Please try again.", style="red"
                    )
                    continue
                break
            except ValueError:
                console.print("❌ Please enter a valid number.", style="red")

        while True:
            try:
                price = float(Prompt.ask("💰 Enter price"))
                if price < 0:
                    console.print(
                        "❌ Price cannot be negative. Please try again.", style="red"
                    )
                    continue
                break
            except ValueError:
                console.print("❌ Please enter a valid number.", style="red")

        if inventory_manager.add_item(name, quantity, price):
            console.print("\n✅ Item added successfully!", style="green")
        else:
            console.print("\n❌ Failed to add item. Please try again.", style="red")

        if not Confirm.ask("\nWould you like to add another item?"):
            break

    main_menu()


def remove_inventory():
    print_header()
    print_menu_header("REMOVE ITEM")
    console.print(Panel("Enter the name of the item you want to remove:", style="bold"))

    name = Prompt.ask("\n�� Enter item name")
    if inventory_manager.remove_item(name):
        console.print("\n✅ Item removed successfully!", style="green")
    else:
        console.print("\n❌ Failed to remove item. Please try again.", style="red")
    main_menu()


def search_inventory():
    print_header()
    print_menu_header("SEARCH INVENTORY")
    console.print(Panel("Enter the name of the item you want to search:", style="bold"))

    name = Prompt.ask("\n🔍 Enter item name to search")
    item = inventory_manager.search_item(name)
    if item:
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_row("📝 Name:", item.name)
        table.add_row("🔢 Quantity:", str(item.quantity))
        table.add_row("💰 Price:", f"${item.price:.2f}")
        table.add_row("📅 Date Added:", item.date_added)
        console.print("\n✅ Found item:", style="green")
        console.print(Panel(table, title="Item Details", border_style="blue"))
    else:
        console.print("\n❌ Item not found.", style="red")
    main_menu()


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        console.print(
            "\n👋 Thank you for using Inventory Manager! Goodbye!", style="bold green"
        )
        sys.exit(0)
