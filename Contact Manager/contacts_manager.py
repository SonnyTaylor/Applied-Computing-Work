# contact_manager.py

# Import json module so that contacts can be pulled from a json file and saved to a json file.
import json

# import os to clear screen
import os

# Logo that is displayed on startup
# its the star wars font lol
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
TREVERSE = "\033[7m"
TDEFAULT = "\033[0m"


def press_enter_to_continue():
    """Prints a message to the console and waits for the user to press enter."""
    enter = input(TBLUE + TUNDERLINE + "Press enter to continue" + TDEFAULT)
    if enter is not None:
        clear_terminal()
        return
    else:
        clear_terminal()
        return


def clear_terminal():
    """
    Clears the terminal screen.
    """
    if os.name == "nt":  # Windows
        os.system("cls")
    elif os.name == "posix":  # Sigma Linux or macOS
        os.system("clear")
    else:
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
        print("Contacts file not found:", filename)  # Add this line for debugging
        return {}
    except json.JSONDecodeError:
        print(
            "Error decoding JSON data in contacts file:", filename
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
    add_contacts_finished = input("Would you like to add another contact? (y/n): ")
    if add_contacts_finished.lower() == "y":
        add_contact(contacts)
    elif add_contacts_finished.lower() == "n":
        clear_terminal()
        return
    else:
        print("Invalid input. Returning to main menu.")
        clear_terminal()
        return


def update_contact(contacts):
    """Updates an existing contact.

    Args:
        contacts (dict): A dictionary containing the existing contacts.
    """
    name = input("Enter contact name to update: ")
    if name in contacts:
        phone = input("Enter new phone number (press enter to leave unchanged): ")
        email = input("Enter new email address (press enter to leave unchanged): ")
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print("Contact updated successfully.")
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
    else:
        print("Contact not found.")


def display_contacts(contacts):
    """Prints the contacts to the console.

    Args:
        contacts (dict): A dictionary containing the existing contacts.
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

    press_enter_to_continue()
