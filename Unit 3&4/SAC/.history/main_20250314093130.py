import sys
import inventory_management as inventory
import webbrowser


def main_menu():
    print("Welcome to Inventory Manager")
    print("1. View inventory")
    print("2. Add inventory")
    print("3. Remove inventory")
    print("4. Search inventory")

    main_option = int(input("Pick an option (1-4): "))
    match main_option:
        case: 1:
            view_inventory()
    


def view_inventory():
    print("\nWould you like to view the inventory:")
    print("1. In console")
    print("2. Open externally")

    choice = input("Enter the number of your choice (1 or 2): ")
    if choice == "1":
        print(inventory.view_inventory)
    elif choice == "2":
        webbrowser.open("inventory.csv")
    else:
        print("Invalid input. Please enter 1 or 2.\n")


def main():
    inventory.make_inventory_file
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print("Goodbye!")
        sys.exit(0)
