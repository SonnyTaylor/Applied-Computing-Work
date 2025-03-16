from pathlib import Path
import csv


def make_inventory_file():
    try:
        with open("inventory.csv", "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["number", "name", "quantity", "date added"])

    except FileExistsError:
        pass


def inventory_file_existance():
    inventory_file = Path("/inventory.csv")
    if inventory_file.is_file():
        return True
    else:
        return False


def get_inventory():
    pass


def add_inventory(name, quantity, date_added):
    fields = [name, quantity, date_added]
    with open(r"inventory.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(fields)


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
