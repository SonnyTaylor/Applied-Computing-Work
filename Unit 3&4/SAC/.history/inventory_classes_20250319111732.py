from datetime import datetime
import csv
from pathlib import Path
from search_sort import binary_search


class InventoryItem:
    def __init__(self, name: str, quantity: int, date_added: str = None):
        self.name = name
        self.quantity = quantity
        self.date_added = date_added or datetime.today().strftime("%Y-%m-%d")

    def to_dict(self) -> dict:
        """Convert the item to a dictionary for CSV storage"""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "date added": self.date_added,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "InventoryItem":
        """Create an InventoryItem from a dictionary (e.g., from CSV)"""
        return cls(
            name=data["name"],
            quantity=int(data["quantity"]),
            date_added=data["date added"],
        )


class InventoryManager:
    def __init__(self, filename: str = "inventory.csv"):
        self.filename = filename
        self.items = []
        self._ensure_file_exists()
        self._load_inventory()

    def _ensure_file_exists(self):
        """Create the inventory file if it doesn't exist"""
        try:
            with open(self.filename, "x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "quantity", "date added"])
        except FileExistsError:
            pass

    def _load_inventory(self):
        """Load inventory items from the CSV file"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                self.items = [InventoryItem.from_dict(row) for row in reader]
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.items = []

    def _save_inventory(self):
        """Save inventory items to the CSV file"""
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["name", "quantity", "date added"]
                )
                writer.writeheader()
                for item in self.items:
                    writer.writerow(item.to_dict())
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, name: str, quantity: int) -> bool:
        """Add a new item to the inventory"""
        try:
            item = InventoryItem(name, quantity)
            self.items.append(item)
            self._save_inventory()
            return True
        except Exception as e:
            print(f"Error adding item: {e}")
            return False

    def remove_item(self, name: str) -> bool:
        """Remove an item from the inventory by name"""
        try:
            self.items = [
                item for item in self.items if item.name.lower() != name.lower()
            ]
            self._save_inventory()
            return True
        except Exception as e:
            print(f"Error removing item: {e}")
            return False

    def search_item(self, name: str) -> InventoryItem:
        """Search for an item by name using binary search"""
        # Sort items by name for binary search
        sorted_items = sorted(self.items, key=lambda x: x.name)
        names = [item.name for item in sorted_items]

        index = binary_search(names, name)
        if index != -1:
            return sorted_items[index]
        return None

    def get_all_items(self) -> list[InventoryItem]:
        """Get all items in the inventory"""
        return self.items

    def view_inventory(self) -> str:
        """Get a string representation of the inventory"""
        if not self.items:
            return "Inventory is empty"

        # Create a formatted string representation
        result = "Inventory Contents:\n"
        result += "-" * 50 + "\n"
        result += f"{'Name':<30} {'Quantity':<10} {'Date Added'}\n"
        result += "-" * 50 + "\n"

        for item in self.items:
            result += f"{item.name:<30} {item.quantity:<10} {item.date_added}\n"

        return result
