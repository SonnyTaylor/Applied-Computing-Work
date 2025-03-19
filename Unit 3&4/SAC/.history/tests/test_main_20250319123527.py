import pytest
from unittest.mock import patch, MagicMock
from main import (
    print_header,
    print_menu_header,
    create_menu_table,
    view_inventory,
    add_inventory,
    remove_inventory,
    search_inventory,
    sort_inventory,
    InventoryManager,
)


@pytest.fixture
def mock_console():
    """Mock the rich console"""
    with patch("main.console") as mock:
        yield mock


@pytest.fixture
def mock_inventory_manager():
    """Mock the inventory manager"""
    with patch("main.inventory_manager") as mock:
        yield mock


def test_print_header(mock_console):
    """Test printing the header"""
    print_header()
    mock_console.print.assert_called_once()
    # Verify the panel contains the title
    call_args = mock_console.print.call_args[0][0]
    assert "INVENTORY MANAGER" in str(call_args)


def test_print_menu_header(mock_console):
    """Test printing menu header"""
    print_menu_header("TEST MENU")
    mock_console.print.assert_called_once()
    # Verify the panel contains the title
    call_args = mock_console.print.call_args[0][0]
    assert "TEST MENU" in str(call_args)


def test_create_menu_table():
    """Test creating the menu table"""
    table = create_menu_table()
    assert table is not None
    # Verify table contains all menu options
    table_str = str(table)
    assert "View Inventory" in table_str
    assert "Add New Item" in table_str
    assert "Remove Item" in table_str
    assert "Search Inventory" in table_str
    assert "Sort Inventory" in table_str
    assert "Exit" in table_str


def test_view_inventory_console(mock_console, mock_inventory_manager):
    """Test viewing inventory in console"""
    # Mock the inventory data
    mock_inventory_manager.view_inventory.return_value = "Test Item,10,9.99,2024-01-01"

    # Mock user input to choose console view and then back
    with patch("main.Prompt.ask", side_effect=["1", "3"]):
        view_inventory()

    # Verify console prints
    assert mock_console.print.call_count >= 2
    # Verify inventory was viewed
    mock_inventory_manager.view_inventory.assert_called_once()


def test_add_inventory_success(mock_console, mock_inventory_manager):
    """Test successfully adding an item"""
    # Mock user inputs
    with patch("main.Prompt.ask", side_effect=["Test Item", "10", "9.99"]):
        # Mock confirm to add one item
        with patch("main.Confirm.ask", return_value=False):
            add_inventory()

    # Verify item was added
    mock_inventory_manager.add_item.assert_called_once_with("Test Item", 10, 9.99)
    # Verify success message was printed
    mock_console.print.assert_any_call("\n✅ Item added successfully!", style="green")


def test_add_inventory_invalid_input(mock_console, mock_inventory_manager):
    """Test adding item with invalid input"""
    # Mock user inputs with invalid quantity
    with patch("main.Prompt.ask", side_effect=["Test Item", "invalid", "10", "9.99"]):
        # Mock confirm to add one item
        with patch("main.Confirm.ask", return_value=False):
            add_inventory()

    # Verify error message was printed
    mock_console.print.assert_any_call("❌ Please enter a valid number.", style="red")
    # Verify item was not added
    mock_inventory_manager.add_item.assert_not_called()


def test_remove_inventory_success(mock_console, mock_inventory_manager):
    """Test successfully removing an item"""
    # Mock user input
    with patch("main.Prompt.ask", return_value="Test Item"):
        remove_inventory()

    # Verify item was removed
    mock_inventory_manager.remove_item.assert_called_once_with("Test Item")
    # Verify success message was printed
    mock_console.print.assert_any_call("\n✅ Item removed successfully!", style="green")


def test_search_inventory_found(mock_console, mock_inventory_manager):
    """Test searching for an existing item"""
    # Mock the search result
    mock_item = MagicMock()
    mock_item.name = "Test Item"
    mock_item.quantity = 10
    mock_item.price = 9.99
    mock_item.date_added = "2024-01-01"
    mock_inventory_manager.search_item.return_value = mock_item

    # Mock user input
    with patch("main.Prompt.ask", return_value="Test Item"):
        search_inventory()

    # Verify search was performed
    mock_inventory_manager.search_item.assert_called_once_with("Test Item")
    # Verify item details were displayed
    mock_console.print.assert_any_call("\n✅ Found item:", style="green")


def test_search_inventory_not_found(mock_console, mock_inventory_manager):
    """Test searching for a non-existent item"""
    # Mock the search result
    mock_inventory_manager.search_item.return_value = None

    # Mock user input
    with patch("main.Prompt.ask", return_value="Nonexistent Item"):
        search_inventory()

    # Verify search was performed
    mock_inventory_manager.search_item.assert_called_once_with("Nonexistent Item")
    # Verify not found message was displayed
    mock_console.print.assert_any_call("\n❌ Item not found.", style="red")


def test_sort_inventory(mock_console, mock_inventory_manager):
    """Test sorting inventory"""
    # Mock user input to sort by name
    with patch("main.Prompt.ask", return_value="1"):
        # Mock confirm to sort once
        with patch("main.Confirm.ask", return_value=False):
            sort_inventory()

    # Verify sort was performed
    mock_inventory_manager.sort_by_name.assert_called_once()
    # Verify success message was printed
    mock_console.print.assert_any_call(
        "\n✅ Inventory sorted successfully!", style="green"
    )


def test_sort_inventory_empty(mock_console, mock_inventory_manager):
    """Test sorting empty inventory"""
    # Mock empty inventory
    mock_inventory_manager.items = []

    # Mock user input to sort by name
    with patch("main.Prompt.ask", return_value="1"):
        sort_inventory()

    # Verify empty message was printed
    mock_console.print.assert_any_call(
        "\n❌ Inventory is empty. Nothing to sort.", style="red"
    )
    # Verify sort was not performed
    mock_inventory_manager.sort_by_name.assert_not_called()
