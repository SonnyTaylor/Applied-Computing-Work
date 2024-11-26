# contact_manager.py

# Import json module so that contacts can be pulled from a json file and saved to a json file.
import json

# import os to clear screen
import os
from re import T


class ContactsManager:
    def __init__(self):
        self.contacts_logo = r"""
  ______   ______   .__   __. .___________.    ___       ______ .___________.    _______.
 /      | /  __  \  |  \ |  | |           |   /   \     /      ||           |   /       |
|  ,----'|  |  |  | |   \|  | `---|  |----`  /  ^  \   |  ,----'`---|  |----`  |   (----`
|  |     |  |  |  | |  . `  |     |  |      /  /_\  \  |  |         |  |        \   \    
|  `----.|  `--'  | |  |\   |     |  |     /  _____  \ |  `----.    |  |    .----)   |   
 \______| \______/  |__| \__|     |__|    /__/     \__\ \______|    |__|    |_______/                                                                                         
"""
        self.TGREEN = "\033[32m"
        self.TWHITE = "\033[37m"
        self.TBLUE = "\033[34m"
        self.TRED = "\033[31m"
        self.TYELLOW = "\033[33m"
        self.TBOLD = "\033[1m"
        self.TUNDERLINE = "\033[4m"
        self.TNOUNDERLINE = "\033[24m"
        self.TDEFAULT = "\033[0m"
        self.TPURPLE = "\033[35m"
        self.TCYAN = "\033[36m"

    def clear_terminal(self):
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
                print(
                    "Unsupported operating system, clearing terminal is not supported"
                )

    def press_enter_to_continue(self):
        """Prints a message to the console and waits for the user to press enter."""
        enter = input(
            self.TGREEN + self.TUNDERLINE + "Press enter to continue" + self.TDEFAULT
        )
        match enter:
            case None:
                self.clear_terminal()
                return
            case _:
                self.clear_terminal()
                return

    def load_contacts(self, filename):
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
                self.TRED + "Contacts file not found:", filename + self.TDEFAULT
            )  # Add this line for debugging
            return {}
        except json.JSONDecodeError:
            print(
                self.TRED + "Error decoding JSON data in contacts file:",
                filename + self.TDEFAULT,
            )  # Add this line for debugging
            return {}

    def save_contacts(self, contacts, filename):
        """
        Saves the contacts to a JSON file.

        Args:
            contacts (list): A list of dictionaries representing the contacts.
            filename (str): The name of the file to save the contacts to.
        """
        with open(filename, "w") as file:
            json.dump(contacts, file, indent=4)

    def add_contact(self, contacts):
        """Gets user input to add a new contact

        Args:
            contacts (dict): A dictionary containing the existing contacts.
        """
        name = input(self.TBLUE + "Enter contact name: " + self.TDEFAULT)
        phone = input(self.TBLUE + "Enter phone number: " + self.TDEFAULT)
        email = input(self.TBLUE + "Enter email address: " + self.TDEFAULT)
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully.")
        self.save_contacts(contacts, "contacts.json")
        add_contacts_finished = input(
            self.TBLUE
            + "Would you like to add another contact? (y/n): "
            + self.TDEFAULT
        )
        match add_contacts_finished.lower():
            case "y":
                self.add_contact(contacts)
            case "n":
                self.clear_terminal()
                return
            case _:
                print(
                    self.TRED + "Invalid input. Returning to main menu." + self.TDEFAULT
                )
                self.clear_terminal()
                return

    def update_contact(self, contacts):
        """Updates an existing contact.

        Args:
            contacts (dict): A dictionary containing the existing contacts.
        """
        name = input(self.TBLUE + "Enter contact name to update: " + self.TDEFAULT)
        if name == "":
            print("Contact not found.")
        elif name in contacts:
            new_name = input(
                self.TBLUE
                + "Enter new coTntact name (press enter to leave unchanged): "
                + self.TDEFAULT
            )
            phone = input(
                self.TBLUE
                + "Enter new phone number (press enter to leave unchanged): "
                + self.TDEFAULT
            )
            email = input(
                self.TBLUE
                + "Enter new email address (press enter to leave unchanged): "
                + self.TDEFAULT
            )
            # i could use a match case here, but tbh its just harder to read due to the way its structered with the dictionary and stuff
            if phone:
                contacts[name]["phone"] = phone
            if email:
                contacts[name]["email"] = email
            if new_name:
                contacts[new_name] = contacts.pop(name)
            print("Contact updated successfully.")
            self.save_contacts(contacts, "contacts.json")
            self.press_enter_to_continue()
        else:
            print("Contact not found.")

    def delete_contact(self, contacts):
        """Deletes a selected contact

        Args:
            contacts (dict): A dictionary containing the existing contacts.
        """
        name = input(self.TBLUE + "Enter contact name to delete: " + self.TDEFAULT)
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
            self.save_contacts(contacts, "contacts.json")
            self.press_enter_to_continue()
        else:
            print("Contact not found.")

    def display_contacts(self, contacts, ent_to_contin):
        """Prints the contacts to the console.

        Args:
            contacts (dict): A dictionary containing the existing contacts.
            ent_to_contin (bool): A boolean that determines if the user needs to press enter to continue.
        """
        if contacts:
            print("Contacts:")
            for name, info in contacts.items():
                print(
                    self.TBLUE
                    + f"Name: {self.TDEFAULT}{name}, {self.TBLUE}Phone: {self.TDEFAULT}{info['phone']}, {self.TBLUE}Email: {self.TDEFAULT}{info['email']}"
                )
                print(
                    "--------------------------------------------------------------------"
                )
        else:
            # Print error in red
            print(self.TRED + "No contacts found." + self.TDEFAULT)

        if ent_to_contin:
            self.press_enter_to_continue()
        else:
            return

    def delete_all_contacts(self, contacts):
        """Deletes all contacts.

        Args:
            contacts (dict): A dictionary containing the existing contacts.
        """
        confirm = input(
            self.TRED
            + "Are you sure you want to delete all contacts? (y/n): "
            + self.TDEFAULT
        )
        if confirm.lower() == "y":
            contacts.clear()
            print("All contacts deleted successfully.")
            self.save_contacts(contacts, "contacts.json")
            self.press_enter_to_continue()
        else:
            print("Contacts not deleted.")
            self.press_enter_to_continue()

    def search_contacts(self, contacts):
        """Searches for a contact by name, phone number, or email.

        Args:
            contacts (dict): A dictionary containing the existing contacts.
        """
        search_term = input(
            self.TBLUE
            + "Enter contact name, phone number, or email to search for: "
            + self.TDEFAULT
        ).lower()
        found = False
        print(self.TBLUE + self.TUNDERLINE + "Search results:" + self.TDEFAULT)
        for contact_name, info in contacts.items():
            if (
                search_term in contact_name.lower()
                or search_term in info["phone"]
                or search_term in info["email"]
            ):
                print(
                    self.TBLUE
                    + f"Name: {self.TDEFAULT}{contact_name}, {self.TBLUE}Phone: {self.TDEFAULT}{info['phone']}, {self.TBLUE}Email: {self.TDEFAULT}{info['email']}"
                )
                print(
                    "--------------------------------------------------------------------"
                )
                found = True
        if not found:
            print("Contact not found.")
        self.press_enter_to_continue()
