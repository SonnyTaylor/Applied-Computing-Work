from datetime import datetime
import csv
from pathlib import Path
from search_sort import binary_search, quicksort


class InventoryItem:
    def __init__(self, name: str, quantity: int, price: float, date_added: str = None):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.date_added = (
            date_added
            if date_added is not None
            else datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        )

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "date added": self.date_added,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            quantity=int(data["quantity"]),
            price=float(data["price"]),
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
                writer.writerow(["name", "quantity", "price", "date added"])
        except FileExistsError:
            pass

    def _load_inventory(self):
        """Load inventory from CSV file"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                self.items = [InventoryItem.from_dict(row) for row in reader]
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.items = []

    def _save_inventory(self):
        """Save inventory to CSV file"""
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["name", "quantity", "price", "date added"]
                )
                writer.writeheader()
                writer.writerows([item.to_dict() for item in self.items])
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, name: str, quantity: int, price: float) -> bool:
        """Add a new item to inventory"""
        try:
            new_item = InventoryItem(name, quantity, price)
            self.items.append(new_item)
            self._save_inventory()
            return True
        except Exception as e:
            print(f"Error adding item: {e}")
            return False

    def remove_item(self, name: str) -> bool:
        """Remove an item from inventory"""
        try:
            original_length = len(self.items)
            self.items = [
                item for item in self.items if item.name.lower() != name.lower()
            ]
            # Only save and return True if an item was actually removed
            if len(self.items) < original_length:
                self._save_inventory()
                return True
            return False
        except Exception as e:
            print(f"Error removing item: {e}")
            return False

    def search_item(self, name: str) -> InventoryItem:
        """Search for an item using binary search"""
        sorted_items = sorted(self.items, key=lambda x: x.name)
        names = [item.name for item in sorted_items]
        index = binary_search(names, name)

        if index != -1:
            return sorted_items[index]
        return None

    def get_all_items(self) -> list[InventoryItem]:
        """Get all items in inventory"""
        return self.items

    def view_inventory(self) -> str:
        """Return string representation of inventory"""
        if not self.items:
            return "Inventory is empty"

        output = "name,quantity,date added\n"
        for item in self.items:
            output += f"{item.name},{item.quantity},{item.price},{item.date_added}\n"
        return output

    def sort_by_name(self):
        self.items = quicksort(self.items, lambda x: x.name)
        self._save_inventory()

    def sort_by_quantity(self):
        self.items = quicksort(self.items, lambda x: x.quantity)
        self._save_inventory()

    def sort_by_price(self):
        self.items = quicksort(self.items, lambda x: x.price)
        self._save_inventory()

    def sort_by_date_added(self):
        self.items = quicksort(self.items, lambda x: x.date_added)
        self._save_inventory()
