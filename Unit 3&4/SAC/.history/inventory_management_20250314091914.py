from pathlib import Path


def make_inventory_file():
    try:
        with open("inventory.csv", "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["number", "name", "quantity"])
            print("file made")
    except FileExistsError:
        print(file exists)
        pass


def inventory_file_existance():
    inventory_file = Path("/inventory.csv")
    if inventory_file.is_file():
        return True
    else:
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
