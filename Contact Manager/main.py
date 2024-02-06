# main.py
import contacts_manager as cm


def main():
    contacts = cm.load_contacts("contacts.json")
    cm.clear_terminal()

    while True:
        print(cm.TBLUE + cm.contacts_logo + cm.TWHITE)
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Display all contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                cm.clear_terminal()
                cm.add_contact(contacts)
            case "2":
                cm.clear_terminal()
                cm.search_contact(contacts)
            case "3":
                cm.clear_terminal()
                cm.update_contact(contacts)
            case "4":
                cm.clear_terminal()
                cm.delete_contact(contacts)
            case "5":
                cm.clear_terminal()
                cm.display_contacts(contacts)
            case "6":
                print("Exiting program...")
                cm.save_contacts(contacts, "contacts.json")
                cm.clear_terminal()
                exit()
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
