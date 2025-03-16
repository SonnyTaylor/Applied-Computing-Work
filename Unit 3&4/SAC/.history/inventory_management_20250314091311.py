from pathlib import Path


def make_inventory_file():
    try:
        with open("inventory.csv", "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["number", "name", "quantity"])
    except FileExistsError:
        pass


def check_for_inventory_file():
    inventory_file = Path("/inventory.csv")
    if inventory_file.is_file():
        return False


def get_inventory():
    pass


def add_inventory():
    pass


def search_inventory():
    pass


def remove_inventory():
    pass


def save_inventory():
    pass
