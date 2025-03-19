import unittest
from datetime import datetime
from inventory_classes import InventoryItem


class TestInventoryItem(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.test_name = "Test Item"
        self.test_quantity = 10
        self.test_price = 99.99
        self.test_date = "2024-03-19 12:00:00"

    def test_create_inventory_item(self):
        """Test creating a new inventory item"""
        item = InventoryItem(self.test_name, self.test_quantity, self.test_price)
        self.assertEqual(item.name, self.test_name)
        self.assertEqual(item.quantity, self.test_quantity)
        self.assertEqual(item.price, self.test_price)
        self.assertIsNotNone(item.date_added)

    def test_create_inventory_item_with_date(self):
        """Test creating an inventory item with a specific date"""
        item = InventoryItem(
            self.test_name, self.test_quantity, self.test_price, self.test_date
        )
        self.assertEqual(item.name, self.test_name)
        self.assertEqual(item.quantity, self.test_quantity)
        self.assertEqual(item.price, self.test_price)
        self.assertEqual(item.date_added, self.test_date)

    def test_to_dict(self):
        """Test converting inventory item to dictionary"""
        item = InventoryItem(
            self.test_name, self.test_quantity, self.test_price, self.test_date
        )
        item_dict = item.to_dict()
        self.assertEqual(item_dict["name"], self.test_name)
        self.assertEqual(item_dict["quantity"], self.test_quantity)
        self.assertEqual(item_dict["price"], self.test_price)
        self.assertEqual(item_dict["date added"], self.test_date)

    def test_from_dict(self):
        """Test creating inventory item from dictionary"""
        item_dict = {
            "name": self.test_name,
            "quantity": str(self.test_quantity),
            "price": str(self.test_price),
            "date added": self.test_date,
        }
        item = InventoryItem.from_dict(item_dict)
        self.assertEqual(item.name, self.test_name)
        self.assertEqual(item.quantity, self.test_quantity)
        self.assertEqual(item.price, self.test_price)
        self.assertEqual(item.date_added, self.test_date)


if __name__ == "__main__":
    unittest.main()
