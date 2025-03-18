from pathlib import Path
import csv
from search_sort import binary_search


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
    fields = [name, quantity, date_added]
    with open(r"inventory.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(fields)


def search_inventory(target_name, filename="inventory.csv"):
    # i got help from copilot here
    # Open the CSV file and read its contents
    with open(filename, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        # Read all rows into a list of dictionaries
        inventory = [row for row in reader]

    # Sort the inventory by the 'name' key
    inventory.sort(key=lambda x: x["name"])

    # Extract the names into a list for binary search
    names = [item["name"] for item in inventory]

    # Perform binary search for the target name
    index = binary_search(names, target_name)

    if index != -1:
        # If the name is found, return the corresponding inventory item
        return inventory[index]
    else:
        # If not found, return None
        return None


def remove_inventory():
    pass


def view_inventory(filename="inventory.csv"):
    """Returns contents of csv file

    Returns:
        _type_: _description_
    """
    try:
        # Attempt to open the inventory CSV file in read mode
        with open(filename, "r") as file:
            # Read the entire contents of the file
            content = file.read()
        # Return the contents of the file
        return content
    except Exception as e:
        # If an error occurs (e.g., file not found), return an error message
        return f"An error occurred: {e}"
