def main_menu():
    print("Welcome to Inventory Manager")
    print("1. View inventory")
    print("2. Add inventory")
    print("3. Remove inventory")
    print("4. Search inventory")

    main_option = input("Pick an option (1-4): ")


def main():
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye!")
        exit()
