import pytest
from datetime import datetime
from pathlib import Path
from inventory_classes import InventoryItem, InventoryManager
import csv
import os


@pytest.fixture
def temp_inventory_file(tmp_path):
    """Create a temporary inventory file for testing"""
    inventory_file = tmp_path / "test_inventory.csv"
    with open(inventory_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "quantity", "price", "date added"])
    return inventory_file


@pytest.fixture
def inventory_manager(temp_inventory_file):
    """Create an InventoryManager instance with a temporary file"""
    return InventoryManager(filename=str(temp_inventory_file))


def test_inventory_item_creation():
    """Test creating an InventoryItem"""
    item = InventoryItem("Test Item", 10, 9.99)
    assert item.name == "Test Item"
    assert item.quantity == 10
    assert item.price == 9.99
    assert isinstance(item.date_added, str)


def test_inventory_item_to_dict():
    """Test converting InventoryItem to dictionary"""
    item = InventoryItem("Test Item", 10, 9.99)
    item_dict = item.to_dict()
    assert item_dict["name"] == "Test Item"
    assert item_dict["quantity"] == 10
    assert item_dict["price"] == 9.99
    assert "date added" in item_dict


def test_inventory_item_from_dict():
    """Test creating InventoryItem from dictionary"""
    data = {
        "name": "Test Item",
        "quantity": "10",
        "price": "9.99",
        "date added": "2024-01-01 12:00:00",
    }
    item = InventoryItem.from_dict(data)
    assert item.name == "Test Item"
    assert item.quantity == 10
    assert item.price == 9.99
    assert item.date_added == "2024-01-01 12:00:00"


def test_add_item(inventory_manager):
    """Test adding an item to inventory"""
    assert inventory_manager.add_item("Test Item", 10, 9.99)
    assert len(inventory_manager.items) == 1
    assert inventory_manager.items[0].name == "Test Item"
    assert inventory_manager.items[0].quantity == 10
    assert inventory_manager.items[0].price == 9.99


def test_remove_item(inventory_manager):
    """Test removing an item from inventory"""
    inventory_manager.add_item("Test Item", 10, 9.99)
    assert inventory_manager.remove_item("Test Item")
    assert len(inventory_manager.items) == 0


def test_remove_nonexistent_item(inventory_manager):
    """Test removing an item that doesn't exist"""
    assert not inventory_manager.remove_item("Nonexistent Item")


def test_search_item(inventory_manager):
    """Test searching for an item"""
    inventory_manager.add_item("Test Item", 10, 9.99)
    item = inventory_manager.search_item("Test Item")
    assert item is not None
    assert item.name == "Test Item"
    assert item.quantity == 10
    assert item.price == 9.99


def test_search_nonexistent_item(inventory_manager):
    """Test searching for an item that doesn't exist"""
    assert inventory_manager.search_item("Nonexistent Item") is None


def test_sort_by_name(inventory_manager):
    """Test sorting inventory by name"""
    inventory_manager.add_item("C Item", 10, 9.99)
    inventory_manager.add_item("A Item", 5, 4.99)
    inventory_manager.add_item("B Item", 7, 7.99)

    inventory_manager.sort_by_name()
    assert [item.name for item in inventory_manager.items] == [
        "A Item",
        "B Item",
        "C Item",
    ]


def test_sort_by_quantity(inventory_manager):
    """Test sorting inventory by quantity"""
    inventory_manager.add_item("Item 1", 10, 9.99)
    inventory_manager.add_item("Item 2", 5, 4.99)
    inventory_manager.add_item("Item 3", 7, 7.99)

    inventory_manager.sort_by_quantity()
    assert [item.quantity for item in inventory_manager.items] == [5, 7, 10]


def test_sort_by_price(inventory_manager):
    """Test sorting inventory by price"""
    inventory_manager.add_item("Item 1", 10, 9.99)
    inventory_manager.add_item("Item 2", 5, 4.99)
    inventory_manager.add_item("Item 3", 7, 7.99)

    inventory_manager.sort_by_price()
    assert [item.price for item in inventory_manager.items] == [4.99, 7.99, 9.99]


def test_sort_by_date_added(inventory_manager):
    """Test sorting inventory by date added"""
    # Add items with different dates
    item1 = InventoryItem("Item 1", 10, 9.99, "2024-01-01 12:00:00")
    item2 = InventoryItem("Item 2", 5, 4.99, "2024-01-02 12:00:00")
    item3 = InventoryItem("Item 3", 7, 7.99, "2024-01-03 12:00:00")

    inventory_manager.items = [item1, item2, item3]
    inventory_manager.sort_by_date_added()
    assert [item.date_added for item in inventory_manager.items] == [
        "2024-01-01 12:00:00",
        "2024-01-02 12:00:00",
        "2024-01-03 12:00:00",
    ]


def test_view_inventory_empty(inventory_manager):
    """Test viewing empty inventory"""
    assert inventory_manager.view_inventory() == "Inventory is empty"


def test_view_inventory_with_items(inventory_manager):
    """Test viewing inventory with items"""
    inventory_manager.add_item("Test Item", 10, 9.99)
    view_output = inventory_manager.view_inventory()
    assert "Test Item" in view_output
    assert "10" in view_output
    assert "9.99" in view_output


def test_get_all_items(inventory_manager):
    """Test getting all items from inventory"""
    inventory_manager.add_item("Item 1", 10, 9.99)
    inventory_manager.add_item("Item 2", 5, 4.99)
    items = inventory_manager.get_all_items()
    assert len(items) == 2
    assert items[0].name == "Item 1"
    assert items[1].name == "Item 2"


def test_remove_item_case_sensitivity(inventory_manager):
    """Test removing an item with different case"""
    inventory_manager.add_item("Test Item", 10, 9.99)
    assert inventory_manager.remove_item("TEST ITEM")
    assert len(inventory_manager.items) == 0


def test_add_item_error_handling(inventory_manager, monkeypatch):
    """Test error handling when adding an item"""

    def mock_save(*args, **kwargs):
        raise Exception("Save error")

    monkeypatch.setattr(inventory_manager, "_save_inventory", mock_save)
    assert not inventory_manager.add_item("Test Item", 10, 9.99)


def test_load_inventory_error_handling(inventory_manager, monkeypatch):
    """Test error handling when loading inventory"""

    def mock_open(*args, **kwargs):
        raise Exception("Load error")

    monkeypatch.setattr("builtins.open", mock_open)
    inventory_manager._load_inventory()
    assert len(inventory_manager.items) == 0


def test_save_inventory_error_handling(inventory_manager, monkeypatch):
    """Test error handling when saving inventory"""

    def mock_open(*args, **kwargs):
        raise Exception("Save error")

    monkeypatch.setattr("builtins.open", mock_open)
    # Should not raise an exception
    inventory_manager._save_inventory()
