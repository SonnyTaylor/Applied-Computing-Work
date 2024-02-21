# main.py

from contacts_manager import ContactsManager
import sys  # Import the sys module to use the exit function

contacts_manager = ContactsManager()  # Initating the class
contacts = contacts_manager.load_contacts("contacts.json")


def main():
    contacts_manager.clear_terminal()

    while True:
        # Print logo and menu
        print(
            contacts_manager.TBLUE
            + contacts_manager.contacts_logo
            + contacts_manager.TWHITE
        )
        print("1. Add a contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Display all contacts")
        print("5. Search contacts")
        print("6. Delete all contacts")
        print("7. Exit")

        choice = input(
            contacts_manager.TBLUE + "Enter a number: " + contacts_manager.TDEFAULT
        )

        match choice:
            case "1":
                contacts_manager.clear_terminal()
                contacts_manager.add_contact(contacts)
            case "2":
                contacts_manager.clear_terminal()
                contacts_manager.display_contacts(contacts, False)
                contacts_manager.update_contact(contacts)
            case "3":
                contacts_manager.clear_terminal()
                contacts_manager.display_contacts(contacts, False)
                contacts_manager.delete_contact(contacts)
            case "4":
                contacts_manager.clear_terminal()
                contacts_manager.display_contacts(contacts, True)
            case "5":
                contacts_manager.clear_terminal()
                contacts_manager.search_contacts(contacts)
            case "6":
                contacts_manager.clear_terminal()
                contacts_manager.delete_all_contacts(contacts)
            case "7":
                print("Exiting program...")
                contacts_manager.save_contacts(contacts, "contacts.json")
                contacts_manager.clear_terminal()
                sys.exit()  # Use the exit function from the sys module to exit the program
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
                contacts_manager.press_enter_to_continue()
                contacts_manager.clear_terminal()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program...")
        contacts_manager.save_contacts(contacts, "contacts.json")
        contacts_manager.clear_terminal()
        sys.exit()
    except EOFError:
        print("\nExiting program...")
        contacts_manager.save_contacts(contacts, "contacts.json")
        contacts_manager.clear_terminal()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        contacts_manager.press_enter_to_continue()
        contacts_manager.clear_terminal()
