import csv
from pathlib import Path


def make_inventory_file():
    try:
        with open("inventory.csv", "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "quantity", "date added"])

    except FileExistsError:
        pass


def inventory_file_existance():
    inventory_file = Path("/inventory.csv")
    if inventory_file.is_file():
        return True
    else:
        return False


def get_inventory():
    try:
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)
            return list(reader)
    except Exception as e:
        return f"An error occurred: {e}"


def add_inventory(name, quantity, date_added):
    if not inventory_file_existance():
        make_inventory_file()
    fields = [name, quantity, date_added]
    try:
        with open("inventory.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fields)
    except Exception as e:
        return f"An error occurred: {e}"
    return "Inventory added successfully"


def search_inventory():
    pass


def remove_inventory():
    pass


def save_inventory():
    pass


def view_inventory():
    try:
        with open("inventory.csv", "r") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"An error occurred: {e}"
