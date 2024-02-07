# contact_manager.py

# Import json module so that contacts can be pulled from a json file and saved to a json file.
import json

# import os to clear screen
import os
from re import T

# Logo that is displayed on startup
# its the star wars font lol 👽
contacts_logo = r"""
  ______   ______   .__   __. .___________.    ___       ______ .___________.    _______.
 /      | /  __  \  |  \ |  | |           |   /   \     /      ||           |   /       |
|  ,----'|  |  |  | |   \|  | `---|  |----`  /  ^  \   |  ,----'`---|  |----`  |   (----`
|  |     |  |  |  | |  . `  |     |  |      /  /_\  \  |  |         |  |        \   \    
|  `----.|  `--'  | |  |\   |     |  |     /  _____  \ |  `----.    |  |    .----)   |   
 \______| \______/  |__| \__|     |__|    /__/     \__\ \______|    |__|    |_______/                                                                                         
"""

# Define terminal colors constants cause i dont wanna use a pip module for this like colorama
# some of these arnt used but oh well, theyre here for future use i guess
TGREEN = "\033[32m"
TWHITE = "\033[37m"
TBLUE = "\033[34m"
TRED = "\033[31m"
TYELLOW = "\033[33m"
TBOLD = "\033[1m"
TUNDERLINE = "\033[4m"
TNOUNDERLINE = "\033[24m"
TDEFAULT = "\033[0m"
TPURPLE = "\033[35m"
TCYAN = "\033[36m"


def press_enter_to_continue():
    """Prints a message to the console and waits for the user to press enter."""
    enter = input(TGREEN + TUNDERLINE + "Press enter to continue" + TDEFAULT)
    match enter:
        case None:
            clear_terminal()
            return
        case _:
            clear_terminal()
            return


def clear_terminal():
    """
    Clears the terminal screen.
    """
    match os.name:
        case "nt":  # Windows
            os.system("cls")
        case "posix":  # Sigma Linux or macOS
            os.system("clear")
        case _:
            # Super niche message that most people should never see, only occurs if user doesnt run Windows, Linux or MacOS. Like seriously though, who uses anything else besides Windows, Linux, or macOS? maybe if this were in some kind of embedded program but like really though.
            print("Unsupported operating system, clearing terminal is not supported")


def load_contacts(filename):
    """Loads the contacts from a file and returns them as a dictionary.

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
            TRED + "Contacts file not found:", filename + TDEFAULT
        )  # Add this line for debugging
        return {}
    except json.JSONDecodeError:
        print(
            TRED + "Error decoding JSON data in contacts file:", filename + TDEFAULT
        )  # Add this line for debugging
        return {}


def save_contacts(contacts, filename):
    """
    Saves the contacts to a JSON file.

    Args:
        contacts (list): A list of dictionaries representing the contacts.
        filename (str): The name of the file to save the contacts to.
    """
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Gets user input to add a new contact

    Args:
        contacts (dict): A dictionary containing the existing contacts.
    """
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")
    save_contacts(contacts, "contacts.json")
    add_contacts_finished = input("Would you like to add another contact? (y/n): ")
    match add_contacts_finished.lower():
        case "y":
            add_contact(contacts)
        case "n":
            clear_terminal()
            return
        case _:
            print("Invalid input. Returning to main menu.")
            clear_terminal()
            return


def update_contact(contacts):
    """Updates an existing contact.

    Args:
        contacts (dict): A dictionary containing the existing contacts.
    """
    name = input("Enter contact name to update: ")
    if name == "":
        print("Contact not found.")
    elif name in contacts:
        new_name = input("Enter new contact name (press enter to leave unchanged): ")
        phone = input("Enter new phone number (press enter to leave unchanged): ")
        email = input("Enter new email address (press enter to leave unchanged): ")
        # i could use a match case here, but tbh its just harder to read due to the way its structered with the dictionary and stuff
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if new_name:
            contacts[new_name] = contacts.pop(name)
        print("Contact updated successfully.")
        save_contacts(contacts, "contacts.json")
        press_enter_to_continue()
    else:
        print("Contact not found.")


def delete_contact(contacts):
    """Deletes a selected contact

    Args:
        contacts (dict): A dictionary containing the existing contacts.
    """
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
        save_contacts(contacts, "contacts.json")
        press_enter_to_continue()
    else:
        print("Contact not found.")


def display_contacts(contacts, ent_to_contin):
    """Prints the contacts to the console.

    Args:
        contacts (dict): A dictionary containing the existing contacts.
        ent_to_contin (bool): A boolean that determines if the user needs to press enter to continue.
    """
    if contacts:
        print("Contacts:")
        for name, info in contacts.items():
            print(
                TBLUE
                + f"Name: {TDEFAULT}{name}, {TBLUE}Phone: {TDEFAULT}{info['phone']}, {TBLUE}Email: {TDEFAULT}{info['email']}"
            )
            print(
                "--------------------------------------------------------------------"
            )
    else:
        # Print error in red
        print(TRED + "No contacts found." + TDEFAULT)

    if ent_to_contin:
        press_enter_to_continue()
    else:
        return


def delete_all_contacts(contacts):
    """Deletes all contacts.

    Args:
        contacts (dict): A dictionary containing the existing contacts.
    """
    confirm = input("Are you sure you want to delete all contacts? (y/n): ")
    if confirm.lower() == "y":
        contacts.clear()
        print("All contacts deleted successfully.")
        save_contacts(contacts, "contacts.json")
        press_enter_to_continue()
    else:
        print("Contacts not deleted.")
        press_enter_to_continue()


def search_contacts(contacts):
    """Searches for a contact by name.

    Args:
        contacts (dict): A dictionary containing the existing contacts.
    """
    name = input("Enter contact name to search for: ").lower()
    found = False
    print(TBLUE + TUNDERLINE + "Search results:" + TDEFAULT)
    for contact_name, info in contacts.items():
        if name in contact_name.lower():
            print(
                TBLUE
                + f"Name: {TDEFAULT}{contact_name}, {TBLUE}Phone: {TDEFAULT}{info['phone']}, {TBLUE}Email: {TDEFAULT}{info['email']}"
            )
            print(
                "--------------------------------------------------------------------"
            )
            found = True
    if not found:
        print("Contact not found.")
    press_enter_to_continue()
