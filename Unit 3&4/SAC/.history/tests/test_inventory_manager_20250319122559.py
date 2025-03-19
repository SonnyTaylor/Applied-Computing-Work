import unittest
import os
import csv
from datetime import datetime
from inventory_classes import InventoryManager, InventoryItem


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.test_filename = "test_inventory.csv"
        self.inventory_manager = InventoryManager(self.test_filename)
        self.test_item = InventoryItem("Test Item", 10, 99.99)

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_initialize_inventory_manager(self):
        """Test initializing inventory manager"""
        self.assertEqual(self.inventory_manager.filename, self.test_filename)
        self.assertEqual(len(self.inventory_manager.items), 0)
        self.assertTrue(os.path.exists(self.test_filename))

    def test_add_item(self):
        """Test adding an item to inventory"""
        success = self.inventory_manager.add_item(
            self.test_item.name, self.test_item.quantity, self.test_item.price
        )
        self.assertTrue(success)
        self.assertEqual(len(self.inventory_manager.items), 1)
        self.assertEqual(self.inventory_manager.items[0].name, self.test_item.name)

    def test_remove_item(self):
        """Test removing an item from inventory"""
        self.inventory_manager.add_item(
            self.test_item.name, self.test_item.quantity, self.test_item.price
        )
        success = self.inventory_manager.remove_item(self.test_item.name)
        self.assertTrue(success)
        self.assertEqual(len(self.inventory_manager.items), 0)

    def test_search_item(self):
        """Test searching for an item"""
        self.inventory_manager.add_item(
            self.test_item.name, self.test_item.quantity, self.test_item.price
        )
        found_item = self.inventory_manager.search_item(self.test_item.name)
        self.assertIsNotNone(found_item)
        self.assertEqual(found_item.name, self.test_item.name)

    def test_search_nonexistent_item(self):
        """Test searching for a non-existent item"""
        found_item = self.inventory_manager.search_item("Nonexistent Item")
        self.assertIsNone(found_item)

    def test_sort_by_name(self):
        """Test sorting inventory by name"""
        items = [("C Item", 10, 99.99), ("A Item", 5, 49.99), ("B Item", 8, 79.99)]
        for name, quantity, price in items:
            self.inventory_manager.add_item(name, quantity, price)

        self.inventory_manager.sort_by_name()
        sorted_names = [item.name for item in self.inventory_manager.items]
        self.assertEqual(sorted_names, ["A Item", "B Item", "C Item"])

    def test_sort_by_quantity(self):
        """Test sorting inventory by quantity"""
        items = [("Item 1", 10, 99.99), ("Item 2", 5, 49.99), ("Item 3", 8, 79.99)]
        for name, quantity, price in items:
            self.inventory_manager.add_item(name, quantity, price)

        self.inventory_manager.sort_by_quantity()
        sorted_quantities = [item.quantity for item in self.inventory_manager.items]
        self.assertEqual(sorted_quantities, [5, 8, 10])

    def test_sort_by_price(self):
        """Test sorting inventory by price"""
        items = [("Item 1", 10, 99.99), ("Item 2", 5, 49.99), ("Item 3", 8, 79.99)]
        for name, quantity, price in items:
            self.inventory_manager.add_item(name, quantity, price)

        self.inventory_manager.sort_by_price()
        sorted_prices = [item.price for item in self.inventory_manager.items]
        self.assertEqual(sorted_prices, [49.99, 79.99, 99.99])

    def test_view_inventory_empty(self):
        """Test viewing empty inventory"""
        view_output = self.inventory_manager.view_inventory()
        self.assertEqual(view_output, "Inventory is empty")

    def test_view_inventory_with_items(self):
        """Test viewing inventory with items"""
        self.inventory_manager.add_item(
            self.test_item.name, self.test_item.quantity, self.test_item.price
        )
        view_output = self.inventory_manager.view_inventory()
        self.assertIn(self.test_item.name, view_output)
        self.assertIn(str(self.test_item.quantity), view_output)
        self.assertIn(str(self.test_item.price), view_output)


if __name__ == "__main__":
    unittest.main()
