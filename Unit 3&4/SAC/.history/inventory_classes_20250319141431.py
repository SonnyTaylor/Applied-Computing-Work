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

    def search_item(self, name: str) -> InventoryItem | None:
        """Search for an item using case-insensitive exact matching"""
        if not name.strip():
            return None

        search_term = name.lower().strip()
        for item in self.items:
            if search_term == item.name.lower():
                return item
        return None

    def get_all_items(self) -> list[InventoryItem]:
        """Get all items in inventory"""
        return self.items

    def view_inventory(self) -> str:
        """Return string representation of inventory"""
        if not self.items:
            return "Inventory is empty"

        result = []
        for item in self.items:
            result.append(
                f"{item.name}: {item.quantity} units at ${item.price:.2f} each"
            )
        return "\n".join(result)

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

    def search_by_name_range(
        self, start_name: str, end_name: str
    ) -> list[InventoryItem]:
        """Search for items with names within a range (alphabetically)"""
        return [
            item
            for item in self.items
            if start_name.lower() <= item.name.lower() <= end_name.lower()
        ]

    def search_by_quantity_range(
        self, min_quantity: int, max_quantity: int
    ) -> list[InventoryItem]:
        """Search for items with quantities within a range"""
        return [
            item for item in self.items if min_quantity <= item.quantity <= max_quantity
        ]

    def search_by_price_range(
        self, min_price: float, max_price: float
    ) -> list[InventoryItem]:
        """Search for items with prices within a range"""
        return [item for item in self.items if min_price <= item.price <= max_price]

    def search_by_date_range(
        self, start_date: str, end_date: str
    ) -> list[InventoryItem]:
        """Search for items added within a date range"""
        return [
            item for item in self.items if start_date <= item.date_added <= end_date
        ]

    def search_by_multiple_criteria(self, criteria: dict) -> list[InventoryItem]:
        """Search for items matching multiple criteria"""
        matching_items = self.items

        for field, value in criteria.items():
            if field == "name":
                matching_items = [
                    item
                    for item in matching_items
                    if value.lower() in item.name.lower()
                ]
            elif field == "quantity":
                if isinstance(value, tuple):
                    min_qty, max_qty = value
                    matching_items = [
                        item
                        for item in matching_items
                        if min_qty <= item.quantity <= max_qty
                    ]
                else:
                    matching_items = [
                        item for item in matching_items if item.quantity == value
                    ]
            elif field == "price":
                if isinstance(value, tuple):
                    min_price, max_price = value
                    matching_items = [
                        item
                        for item in matching_items
                        if min_price <= item.price <= max_price
                    ]
                else:
                    matching_items = [
                        item for item in matching_items if item.price == value
                    ]
            elif field == "date":
                start_date, end_date = value
                matching_items = [
                    item
                    for item in matching_items
                    if start_date <= item.date_added <= end_date
                ]

        return matching_items
