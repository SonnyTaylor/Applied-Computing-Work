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
from rich.align import Align
from rich.style import Style
from rich.live import Live
from rich.spinner import Spinner

# Create a global inventory manager instance
inventory_manager = InventoryManager()
console = Console()


def print_header():
    """Print the application header with enhanced styling"""
    clear_terminal()
    # Create a more sophisticated header with multiple panels
    header_text = Text("INVENTORY MANAGER", style="bold blue")
    subtitle = Text("Professional Inventory Management System", style="italic dim")

    # Create a main header panel
    header_panel = Panel(
        Align.center(Text.assemble(header_text, "\n", subtitle)),
        style="bold white",
        border_style="blue",
        padding=(1, 2),
        title="[bold blue]v1.0[/]",
        subtitle="[dim]Press Ctrl+C to exit[/]",
    )

    console.print(header_panel)
    console.print()


def print_menu_header(title):
    """Print a section header with enhanced styling"""
    console.print(
        Panel(
            Align.center(title),
            style="bold green",
            border_style="green",
            padding=(0, 2),
            box=None,
        )
    )


def create_menu_table():
    """Create a table for the main menu with enhanced styling"""
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2),
        row_styles=["", "dim"],
        style="bold",
    )

    # Add menu items with emojis and better spacing
    table.add_row("1. 📋", "View/Open Inventory")
    table.add_row("2. ➕", "Add New Item")
    table.add_row("3. ❌", "Remove Item")
    table.add_row("4. 🔍", "Search Inventory")
    table.add_row("5. 📊", "Sort Inventory")
    table.add_row("6. 🚪", "Exit")

    return Panel(
        table, title="[bold blue]Main Menu[/]", border_style="blue", padding=(1, 2)
    )


def create_section_table(options):
    """Create a generic section table with consistent styling"""
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2),
        row_styles=["", "dim"],
        style="bold",
    )

    for option in options:
        table.add_row(option[0], option[1])

    return Panel(table, border_style="blue", padding=(1, 2))


def show_loading_spinner(message="Processing..."):
    """Show a loading spinner for operations"""
    with Live(Spinner("dots", text=message), refresh_per_second=10) as live:
        live.update()


def show_success_message(message):
    """Show a success message with consistent styling"""
    console.print(
        Panel(f"✅ {message}", style="bold green", border_style="green", padding=(0, 2))
    )


def show_error_message(message):
    """Show an error message with consistent styling"""
    console.print(
        Panel(f"❌ {message}", style="bold red", border_style="red", padding=(0, 2))
    )


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

        options = [
            ("1. 📱", "View in Console"),
            ("2. 💻", "Open in External Editor"),
            ("3. 🔙", "Back"),
        ]
        console.print(create_section_table(options))

        choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3"])

        if choice == "1":
            # Ask if user wants to sort first
            if Confirm.ask("\nWould you like to sort the inventory before viewing?"):
                print_header()
                print_menu_header("SORT INVENTORY")

                sort_options = [
                    ("1. 📝", "Sort by Name"),
                    ("2. 🔢", "Sort by Quantity"),
                    ("3. 📅", "Sort by Date Added"),
                    ("4. 💰", "Sort by Price"),
                ]
                console.print(create_section_table(sort_options))

                try:
                    sort_option = Prompt.ask(
                        "\nEnter your choice", choices=["1", "2", "3", "4"]
                    )

                    show_loading_spinner("Sorting inventory...")
                    if sort_option == "1":
                        inventory_manager.sort_by_name()
                    elif sort_option == "2":
                        inventory_manager.sort_by_quantity()
                    elif sort_option == "3":
                        inventory_manager.sort_by_date_added()
                    elif sort_option == "4":
                        inventory_manager.sort_by_price()
                    show_success_message("Inventory sorted successfully!")
                except Exception as e:
                    show_error_message(f"Error sorting inventory: {e}")
                    if not Confirm.ask(
                        "\nWould you like to continue viewing unsorted inventory?"
                    ):
                        continue

            console.print("\n📋 Current Inventory:", style="bold")
            items = inventory_manager.get_all_items()

            if not items:
                console.print(
                    Panel(
                        "📭 Inventory is empty", style="yellow", border_style="yellow"
                    )
                )
            else:
                # Calculate summary information
                total_items = sum(item.quantity for item in items)
                total_value = sum(item.quantity * item.price for item in items)

                # Create summary panel with enhanced styling
                summary_table = Table(show_header=False, box=None, padding=(0, 2))
                summary_table.add_row("📦 Total Items:", str(total_items))
                summary_table.add_row("💰 Total Value:", f"${total_value:,.2f}")
                console.print(
                    Panel(
                        summary_table,
                        title="[bold green]Summary[/]",
                        border_style="green",
                        padding=(1, 2),
                    )
                )

                # Create main inventory table with enhanced styling
                table = Table(
                    show_header=True,
                    header_style="bold magenta",
                    border_style="blue",
                    box=None,
                    padding=(0, 2),
                    row_styles=["", "dim"],
                    title="[bold blue]Inventory List[/]",
                )

                # Add columns with consistent styling
                table.add_column("#", style="dim", justify="right", width=4)
                table.add_column("Name", style="cyan", width=30)
                table.add_column("Quantity", style="green", justify="right")
                table.add_column("Price", style="yellow", justify="right")
                table.add_column("Total", style="blue", justify="right")
                table.add_column("Date Added", style="dim", width=20)

                # Add rows with alternating styles
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

                console.print(Panel(table, border_style="blue", padding=(1, 2)))
        elif choice == "2":
            try:
                webbrowser.open(inventory_manager.filename)
                show_success_message("File opened in external editor")
            except OSError:
                show_error_message(
                    "Error opening file externally. Please try viewing in console instead."
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
        console.print(
            Panel(
                "Please enter the following information:",
                style="bold",
                border_style="blue",
                padding=(1, 2),
            )
        )

        name = Prompt.ask("\n📝 Enter item name").strip()
        while not name:
            show_error_message("Item name cannot be empty. Please try again.")
            name = Prompt.ask("📝 Enter item name").strip()

        while True:
            try:
                quantity = int(Prompt.ask("🔢 Enter quantity"))
                if quantity < 0:
                    show_error_message("Quantity cannot be negative. Please try again.")
                    continue
                if quantity > 1000000:
                    show_error_message("Quantity seems too large. Please try again.")
                    continue
                break
            except ValueError:
                show_error_message("Please enter a valid number.")

        while True:
            try:
                price = float(Prompt.ask("💰 Enter price"))
                if price < 0:
                    show_error_message("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                show_error_message("Please enter a valid number.")

        show_loading_spinner("Adding item to inventory...")
        if inventory_manager.add_item(name, quantity, price):
            show_success_message("Item added successfully!")
        else:
            show_error_message("Failed to add item. Please try again.")

        if not Confirm.ask("\nWould you like to add another item?"):
            break

    main_menu()


def remove_inventory():
    print_header()
    print_menu_header("REMOVE ITEM")
    console.print(
        Panel(
            "Enter the name of the item you want to remove:",
            style="bold",
            border_style="blue",
            padding=(1, 2),
        )
    )

    name = Prompt.ask("\n📝 Enter item name")
    show_loading_spinner("Removing item from inventory...")
    if inventory_manager.remove_item(name):
        show_success_message("Item removed successfully!")
    else:
        show_error_message("Failed to remove item. Please try again.")
    main_menu()


def search_inventory():
    while True:
        print_header()
        print_menu_header("SEARCH INVENTORY")

        # Create search field selection table
        search_options = [
            ("1. 📝", "Search by Name"),
            ("2. 🔢", "Search by Quantity"),
            ("3. 💰", "Search by Price"),
            ("4. 🔙", "Back to Main Menu"),
        ]
        console.print(create_section_table(search_options))

        try:
            field_choice = Prompt.ask(
                "\nSelect search field", choices=["1", "2", "3", "4"]
            )

            if field_choice == "4":
                break

            search_term = Prompt.ask("\n🔍 Enter search term").strip()
            if not search_term:
                show_error_message("Search term cannot be empty.")
                if not Confirm.ask("\nWould you like to try another search?"):
                    break
                continue

            show_loading_spinner("Searching inventory...")
            items = []
            if field_choice == "1":
                # Search by name
                items = [
                    item
                    for item in inventory_manager.items
                    if search_term.lower() in item.name.lower()
                ]
            elif field_choice == "2":
                # Search by quantity
                try:
                    search_quantity = int(search_term)
                    items = [
                        item
                        for item in inventory_manager.items
                        if item.quantity == search_quantity
                    ]
                except ValueError:
                    show_error_message("Please enter a valid number for quantity.")
                    if not Confirm.ask("\nWould you like to try another search?"):
                        break
                    continue
            elif field_choice == "3":
                # Search by price
                try:
                    search_price = float(search_term)
                    items = [
                        item
                        for item in inventory_manager.items
                        if item.price == search_price
                    ]
                except ValueError:
                    show_error_message("Please enter a valid number for price.")
                    if not Confirm.ask("\nWould you like to try another search?"):
                        break
                    continue

            if not items:
                console.print(
                    Panel(
                        "No items found matching your search.",
                        style="yellow",
                        border_style="yellow",
                        padding=(1, 2),
                    )
                )
                if not Confirm.ask("\nWould you like to try another search?"):
                    break
                continue

            # Create a table for search results with enhanced styling
            table = Table(
                show_header=True,
                header_style="bold magenta",
                border_style="blue",
                box=None,
                padding=(0, 2),
                row_styles=["", "dim"],
                title="[bold blue]Search Results[/]",
            )

            # Add columns with consistent styling
            table.add_column("#", style="dim", justify="right", width=4)
            table.add_column("Name", style="cyan", width=30)
            table.add_column("Quantity", style="green", justify="right")
            table.add_column("Price", style="yellow", justify="right")
            table.add_column("Total", style="blue", justify="right")

            # Add rows with alternating styles
            for idx, item in enumerate(items, 1):
                total = item.quantity * item.price
                table.add_row(
                    str(idx),
                    item.name,
                    str(item.quantity),
                    f"${item.price:.2f}",
                    f"${total:,.2f}",
                )

            show_success_message(
                f"Found {len(items)} matching item{'s' if len(items) != 1 else ''}"
            )
            console.print(Panel(table, border_style="blue", padding=(1, 2)))

            if not Confirm.ask("\nWould you like to try another search?"):
                break

        except Exception as e:
            show_error_message(f"An error occurred: {e}")
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
