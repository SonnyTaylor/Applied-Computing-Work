from datetime import datetime
import xml.etree.ElementTree as ET
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
        self.in_stock = quantity > 0

    def to_xml(self):
        """Convert item to XML element"""
        item = ET.Element("item")
        ET.SubElement(item, "name").text = self.name
        ET.SubElement(item, "quantity").text = str(self.quantity)
        ET.SubElement(item, "price").text = str(self.price)
        ET.SubElement(item, "date_added").text = self.date_added
        ET.SubElement(item, "in_stock").text = str(self.in_stock)
        return item

    @classmethod
    def from_xml(cls, item_element: ET.Element):
        """Create item from XML element"""
        return cls(
            name=item_element.find("name").text,
            quantity=int(item_element.find("quantity").text),
            price=float(item_element.find("price").text),
            date_added=item_element.find("date_added").text,
        )


class InventoryManager:
    def __init__(self, filename: str = "inventory.xml"):
        self.filename = filename
        self.items = []
        self._ensure_file_exists()
        self._load_inventory()

    def _ensure_file_exists(self):
        """Create the inventory file if it doesn't exist"""
        try:
            root = ET.Element("inventory")
            tree = ET.ElementTree(root)
            tree.write(self.filename, encoding="utf-8", xml_declaration=True)
        except FileExistsError:
            pass

    def _load_inventory(self):
        """Load inventory from XML file"""
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            self.items = [InventoryItem.from_xml(item) for item in root.findall("item")]
        except Exception as e:
            print(f"Error loading inventory: {e}")
            self.items = []

    def _save_inventory(self):
        """Save inventory to XML file"""
        try:
            root = ET.Element("inventory")
            for item in self.items:
                root.append(item.to_xml())
            tree = ET.ElementTree(root)
            tree.write(self.filename, encoding="utf-8", xml_declaration=True)
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
