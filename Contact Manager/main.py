# main.py
import contacts_manager as cm  # import the contacts_manager module :)
import sys  # Import the sys module to use the exit function

contacts = cm.load_contacts("contacts.json")


def main():
    cm.clear_terminal()

    while True:
        print(cm.TBLUE + cm.contacts_logo + cm.TWHITE)
        print("1. Add a contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Display all contacts")
        print("5. Search contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                cm.clear_terminal()
                cm.add_contact(contacts)
            case "2":
                cm.clear_terminal()
                cm.display_contacts(contacts, False)
                cm.update_contact(contacts)
            case "3":
                cm.clear_terminal()
                cm.display_contacts(contacts, False)
                cm.delete_contact(contacts)
            case "4":
                cm.clear_terminal()
                cm.display_contacts(contacts, True)
            case "5":
                cm.clear_terminal()
                cm.search_contacts(contacts)
            case "6":
                print("Exiting program...")
                cm.save_contacts(contacts, "contacts.json")
                cm.clear_terminal()
                sys.exit()  # Use the exit function from the sys module to exit the program
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
                cm.press_enter_to_continue()
                cm.clear_terminal()


if __name__ == "__main__":
    main()
