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
    table.add_row("1. 📋", "View/Open Inventory")
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
        table.add_row("3. 🔙", "Back")
        console.print(table)

        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3"])

        if choice == "1":
            # Ask if user wants to sort first
            if Confirm.ask("\nWould you like to sort the inventory before viewing?"):
                print_header()
                print_menu_header("SORT INVENTORY")

                sort_table = Table(show_header=False, box=None, padding=(0, 2))
                sort_table.add_row("1. 📝", "Sort by Name")
                sort_table.add_row("2. 🔢", "Sort by Quantity")
                sort_table.add_row("3. 📅", "Sort by Date Added")
                sort_table.add_row("4. 💰", "Sort by Price")
                console.print(sort_table)

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
                    if not Confirm.ask(
                        "\nWould you like to continue viewing unsorted inventory?"
                    ):
                        continue

            console.print("\n📋 Current Inventory:", style="bold")
            items = inventory_manager.get_all_items()

            if not items:
                console.print("\n📭 Inventory is empty", style="yellow")
            else:
                # Calculate summary information
                total_items = sum(item.quantity for item in items)
                total_value = sum(item.quantity * item.price for item in items)

                # Create summary panel
                summary_table = Table(show_header=False, box=None, padding=(0, 2))
                summary_table.add_row("📦 Total Items:", str(total_items))
                summary_table.add_row("💰 Total Value:", f"${total_value:,.2f}")
                console.print(
                    Panel(summary_table, title="Summary", border_style="green")
                )

                # Create main inventory table
                table = Table(
                    show_header=True,
                    header_style="bold magenta",
                    border_style="blue",
                    box=None,
                    padding=(0, 2),
                    row_styles=["", "dim"],
                )

                # Add columns
                table.add_column("#", style="dim", justify="right", width=4)
                table.add_column("Name", style="cyan", width=30)
                table.add_column("Quantity", style="green", justify="right")
                table.add_column("Price", style="yellow", justify="right")
                table.add_column("Total", style="blue", justify="right")
                table.add_column("Date Added", style="dim", width=20)

                # Add rows
                for idx, item in enumerate(items, 1):
                    total = item.quantity * item.price
                    table.add_row(
                        str(idx),
                        item.name,
                        str(item.quantity),
                        f"${item.price:.2f}",
                        f"${total:,.2f}",
                        item.date_added,
                    )

                console.print(Panel(table, title="Inventory List", border_style="blue"))
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

    name = Prompt.ask("\n📝 Enter item name")
    if inventory_manager.remove_item(name):
        console.print("\n✅ Item removed successfully!", style="green")
    else:
        console.print("\n❌ Failed to remove item. Please try again.", style="red")
    main_menu()


def search_inventory():
    while True:
        print_header()
        print_menu_header("SEARCH INVENTORY")

        # Create search field selection table
        field_table = Table(show_header=False, box=None, padding=(0, 2))
        field_table.add_row("1. 📝", "Search by Name")
        field_table.add_row("2. 🔢", "Search by Quantity")
        field_table.add_row("3. 💰", "Search by Price")
        field_table.add_row("4. 📅", "Search by Date Added")
        field_table.add_row("5. 🔍", "Advanced Search (Multiple Criteria)")
        field_table.add_row("6. 🔙", "Back to Main Menu")
        console.print(field_table)

        try:
            field_choice = Prompt.ask(
                "\nSelect search field", choices=["1", "2", "3", "4", "5", "6"]
            )

            if field_choice == "6":
                break

            items = []
            if field_choice == "1":
                # Search by name
                search_term = Prompt.ask("\n🔍 Enter search term").strip()
                if not search_term:
                    console.print("\n❌ Search term cannot be empty.", style="red")
                    if not Confirm.ask("\nWould you like to try another search?"):
                        break
                    continue
                items = [
                    item
                    for item in inventory_manager.items
                    if search_term.lower() in item.name.lower()
                ]
            elif field_choice == "2":
                # Search by quantity
                try:
                    search_type = Prompt.ask(
                        "\nSelect search type", choices=["1", "2"], default="1"
                    )
                    if search_type == "1":
                        # Exact quantity
                        search_quantity = int(Prompt.ask("Enter quantity"))
                        items = [
                            item
                            for item in inventory_manager.items
                            if item.quantity == search_quantity
                        ]
                    else:
                        # Quantity range
                        min_qty = int(Prompt.ask("Enter minimum quantity"))
                        max_qty = int(Prompt.ask("Enter maximum quantity"))
                        items = inventory_manager.search_by_quantity_range(
                            min_qty, max_qty
                        )
                except ValueError:
                    console.print("\n❌ Please enter valid numbers.", style="red")
                    if not Confirm.ask("\nWould you like to try another search?"):
                        break
                    continue
            elif field_choice == "3":
                # Search by price
                try:
                    search_type = Prompt.ask(
                        "\nSelect search type", choices=["1", "2"], default="1"
                    )
                    if search_type == "1":
                        # Exact price
                        search_price = float(Prompt.ask("Enter price"))
                        items = [
                            item
                            for item in inventory_manager.items
                            if item.price == search_price
                        ]
                    else:
                        # Price range
                        min_price = float(Prompt.ask("Enter minimum price"))
                        max_price = float(Prompt.ask("Enter maximum price"))
                        items = inventory_manager.search_by_price_range(
                            min_price, max_price
                        )
                except ValueError:
                    console.print("\n❌ Please enter valid numbers.", style="red")
                    if not Confirm.ask("\nWould you like to try another search?"):
                        break
                    continue
            elif field_choice == "4":
                # Search by date
                try:
                    start_date = Prompt.ask("Enter start date (YYYY-MM-DD)")
                    end_date = Prompt.ask("Enter end date (YYYY-MM-DD)")
                    items = inventory_manager.search_by_date_range(start_date, end_date)
                except ValueError:
                    console.print(
                        "\n❌ Please enter valid dates in YYYY-MM-DD format.",
                        style="red",
                    )
                    if not Confirm.ask("\nWould you like to try another search?"):
                        break
                    continue
            elif field_choice == "5":
                # Advanced search with multiple criteria
                criteria = {}
                console.print("\n🔍 Advanced Search Options:", style="bold")
                console.print(
                    "This feature allows you to combine multiple search criteria to find items that match ALL specified conditions."
                )
                console.print("\nAvailable search criteria:", style="bold")

                while True:
                    # Create criteria selection table with descriptions
                    criteria_table = Table(show_header=False, box=None, padding=(0, 2))
                    criteria_table.add_row("1. 📝", "Name Search")
                    criteria_table.add_row(
                        "   ", "Find items with names containing your search term"
                    )
                    criteria_table.add_row("2. 🔢", "Quantity Search")
                    criteria_table.add_row(
                        "   ", "Find items with specific quantities or within a range"
                    )
                    criteria_table.add_row("3. 💰", "Price Search")
                    criteria_table.add_row(
                        "   ", "Find items with specific prices or within a range"
                    )
                    criteria_table.add_row("4. 📅", "Date Search")
                    criteria_table.add_row(
                        "   ", "Find items added within a specific date range"
                    )
                    criteria_table.add_row(
                        "5. ✅", "Done - Search with current criteria"
                    )
                    criteria_table.add_row("6. 🔄", "Clear all criteria and start over")
                    console.print(criteria_table)

                    criterion = Prompt.ask(
                        "\nSelect criterion to add",
                        choices=["1", "2", "3", "4", "5", "6"],
                        default="5",
                    )

                    if criterion == "5":
                        break
                    elif criterion == "6":
                        criteria = {}
                        console.print("\n✅ All criteria cleared.", style="green")
                        continue

                    if criterion == "1":
                        # Name criterion
                        name_term = Prompt.ask("Enter name to search for")
                        criteria["name"] = name_term
                        console.print(
                            f"\n✅ Added name criterion: '{name_term}'", style="green"
                        )
                    elif criterion == "2":
                        # Quantity criterion
                        try:
                            search_type = Prompt.ask(
                                "Select search type", choices=["1", "2"], default="1"
                            )
                            if search_type == "1":
                                qty = int(Prompt.ask("Enter exact quantity"))
                                criteria["quantity"] = qty
                                console.print(
                                    f"\n✅ Added quantity criterion: exactly {qty}",
                                    style="green",
                                )
                            else:
                                min_qty = int(Prompt.ask("Enter minimum quantity"))
                                max_qty = int(Prompt.ask("Enter maximum quantity"))
                                criteria["quantity"] = (min_qty, max_qty)
                                console.print(
                                    f"\n✅ Added quantity criterion: between {min_qty} and {max_qty}",
                                    style="green",
                                )
                        except ValueError:
                            console.print(
                                "\n❌ Please enter valid numbers.", style="red"
                            )
                            continue
                    elif criterion == "3":
                        # Price criterion
                        try:
                            search_type = Prompt.ask(
                                "Select search type", choices=["1", "2"], default="1"
                            )
                            if search_type == "1":
                                price = float(Prompt.ask("Enter exact price"))
                                criteria["price"] = price
                                console.print(
                                    f"\n✅ Added price criterion: exactly ${price:.2f}",
                                    style="green",
                                )
                            else:
                                min_price = float(Prompt.ask("Enter minimum price"))
                                max_price = float(Prompt.ask("Enter maximum price"))
                                criteria["price"] = (min_price, max_price)
                                console.print(
                                    f"\n✅ Added price criterion: between ${min_price:.2f} and ${max_price:.2f}",
                                    style="green",
                                )
                        except ValueError:
                            console.print(
                                "\n❌ Please enter valid numbers.", style="red"
                            )
                            continue
                    elif criterion == "4":
                        # Date criterion
                        start_date = Prompt.ask("Enter start date (YYYY-MM-DD)")
                        end_date = Prompt.ask("Enter end date (YYYY-MM-DD)")
                        criteria["date"] = (start_date, end_date)
                        console.print(
                            f"\n✅ Added date criterion: between {start_date} and {end_date}",
                            style="green",
                        )

                    # Show current criteria
                    if criteria:
                        console.print("\nCurrent search criteria:", style="bold")
                        for field, value in criteria.items():
                            if isinstance(value, tuple):
                                if field == "quantity":
                                    console.print(
                                        f"• Quantity: between {value[0]} and {value[1]}"
                                    )
                                elif field == "price":
                                    console.print(
                                        f"• Price: between ${value[0]:.2f} and ${value[1]:.2f}"
                                    )
                                elif field == "date":
                                    console.print(
                                        f"• Date: between {value[0]} and {value[1]}"
                                    )
                            else:
                                if field == "name":
                                    console.print(f"• Name: contains '{value}'")
                                else:
                                    console.print(f"• {field.capitalize()}: {value}")

                    if not Confirm.ask("\nWould you like to add another criterion?"):
                        break

                if not criteria:
                    console.print("\n❌ No criteria selected.", style="red")
                    if not Confirm.ask("\nWould you like to try another search?"):
                        break
                    continue

                items = inventory_manager.search_by_multiple_criteria(criteria)

            if not items:
                console.print(
                    "\n❌ No items found matching your search.", style="yellow"
                )
                if not Confirm.ask("\nWould you like to try another search?"):
                    break
                continue

            # Create a table for search results
            table = Table(
                show_header=True,
                header_style="bold magenta",
                border_style="blue",
                box=None,
                padding=(0, 2),
                row_styles=["", "dim"],
            )

            # Add columns
            table.add_column("#", style="dim", justify="right", width=4)
            table.add_column("Name", style="cyan", width=30)
            table.add_column("Quantity", style="green", justify="right")
            table.add_column("Price", style="yellow", justify="right")
            table.add_column("Total", style="blue", justify="right")
            table.add_column("Date Added", style="dim", width=20)

            # Add rows
            for idx, item in enumerate(items, 1):
                total = item.quantity * item.price
                table.add_row(
                    str(idx),
                    item.name,
                    str(item.quantity),
                    f"${item.price:.2f}",
                    f"${total:,.2f}",
                    item.date_added,
                )

            console.print(
                f"\n✅ Found {len(items)} matching item{'s' if len(items) != 1 else ''}:",
                style="green",
            )
            console.print(Panel(table, title="Search Results", border_style="blue"))

            if not Confirm.ask("\nWould you like to try another search?"):
                break

        except Exception as e:
            console.print(f"\n❌ An error occurred: {e}", style="red")
            if not Confirm.ask("\nWould you like to try another search?"):
                break
            continue

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
