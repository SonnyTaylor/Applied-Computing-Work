# main.py
import contacts_manager as cf


def main():
    contacts = cf.load_contacts("contacts.json")

    while True:
        print("\nContact Management System")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Display all contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                cf.add_contact(contacts)
            case "2":
                cf.search_contact(contacts)
            case "3":
                cf.update_contact(contacts)
            case "4":
                cf.delete_contact(contacts)
            case "5":
                cf.display_contacts(contacts)
            case "6":
                print("Exiting program...")
                cf.save_contacts(contacts, "contacts.json")
                exit()
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
