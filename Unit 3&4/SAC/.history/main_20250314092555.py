import sys
import inventory_management as inventory


def main_menu():
    print("Welcome to Inventory Manager")
    print("1. View inventory")
    print("2. Add inventory")
    print("3. Remove inventory")
    print("4. Search inventory")

    main_option = input("Pick an option (1-4): ")


def view_inventory():
    print("\nWould you like to view the inventory:")
    print("1. In console")
    print("2. Open externally")


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
