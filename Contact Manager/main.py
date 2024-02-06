# main.py
import contacts_manager as cm


def main():
    contacts = cm.load_contacts("contacts.json")
    cm.clear_terminal()

    while True:
        print(cm.TBLUE + cm.contacts_logo + cm.TWHITE)
        print("1. Add a contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Display all contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                cm.clear_terminal()
                cm.add_contact(contacts)
            case "2":
                cm.clear_terminal()
                cm.update_contact(contacts)
            case "3":
                cm.clear_terminal()
                cm.delete_contact(contacts)
            case "4":
                cm.clear_terminal()
                cm.display_contacts(contacts)
            case "5":
                print("Exiting program...")
                cm.save_contacts(contacts, "contacts.json")
                cm.clear_terminal()
                exit()
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
