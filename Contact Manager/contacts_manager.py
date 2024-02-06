# Import json module so that contacts can be pulled from a json file and saved to a json file.
import json


def load_contacts(filename):
    """Loads the contacts from a file and returns them as a dictionary.

    Args:
        filename (string): the json file to load contacts from

    Returns:
        dictionary: returns a dictionary of contacts
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
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
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")


def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(
            f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}"
        )
    else:
        print("Contact not found.")


def update_contact(contacts):
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
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if contacts:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")
