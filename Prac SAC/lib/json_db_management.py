import json
import ui


def load_students(filename):
    """Loads the students from a file and returns them as a dictionary.

    Args:
        filename (string): the json file to load contacts from

    Returns:
        dictionary: returns a dictionary of contacts
    """
    try:
        with open(filename, "r") as file:
            contacts = json.load(file)
            print(
                "Contacts loaded successfully:", contacts
            )  # Add this line for debugging
            return contacts
    except FileNotFoundError:
        print(
            user_interfaceTRED + "Contacts file not found:",
            filename + user_interfaceTDEFAULT,
        )  # Add this line for debugging
        return {}
    except json.JSONDecodeError:
        print(
            user_interfaceTRED + "Error decoding JSON data in contacts file:",
            filename + user_interfaceTDEFAULT,
        )  # Add this line for debugging
        return {}


def save_students(contacts, filename):
    """
    Saves the students to a JSON file.

    Args:
        contacts (list): A list of dictionaries representing the students.
        filename (str): The name of the file to save the contacts to.
    """
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)
