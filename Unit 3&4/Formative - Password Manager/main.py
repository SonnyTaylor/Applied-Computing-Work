import csv
import getpass
import random
import string

import pyfiglet  # type: ignore


def create_password_file(logs=False):
    """Create a password file if it does not exist.

    Args:
        logs (bool, optional): If true, displays logs in console. Defaults to False.
    """
    try:
        with open("passwords.csv", "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            if logs:
                print("Password file created.")
    except FileExistsError:
        if logs:
            print("Password file already exists.")
    except Exception as e:
        if logs:
            print(f"An error occurred: {e}")


def create_user_file(logs=False):
    """Create a user file if it does not exist.

    Args:
        logs (bool, optional): If true, displays logs in console. Defaults to False.
    """
    try:
        with open("users.csv", "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
            if logs:
                print("User file created.")
    except FileExistsError:
        if logs:
            print("User file already exists.")
    except Exception as e:
        if logs:
            print(f"An error occurred: {e}")


def generate_password(length, complexity):
    """Generates a secure password based on length and complexity specified.

    Args:
        length (int): The length of the password
        complexity (int): The complexity of the password (1-3)

    Returns:
        str: generated random password
    """
    characters = string.ascii_letters
    if complexity > 1:
        characters += string.digits
    if complexity > 2:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


def store_password(account_name, password):
    """Stores a username and password in the password csv file.

    Args:
        account_name (str): The users inputted account name to be stored
        password (str): The users inputted account password to be stored
    """
    with open("passwords.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([account_name, password])


def retrieve_password(account_name):
    """Retrieves a stored password from the password csv file.

    Args:
        account_name (str): The account name to retrieve the password for

    Returns:
        str: The retrieved password if found, otherwise None
    """
    try:
        with open("passwords.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == account_name:
                    return row[1]
        print("Account not found.")
        return None
    except FileNotFoundError:
        print("Password file not found.")
        return None


def update_password(account_name, new_password):
    """Updates a stored password in the password csv file.

    Args:
        account_name (str): The account name to update the password for
        new_password (str): The new password to update the account with
    """
    found = False
    with open("passwords.csv", "r") as file:
        lines = list(csv.reader(file))
    with open("passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in lines:
            if row[0] == account_name:
                writer.writerow([account_name, new_password])
                found = True
            else:
                writer.writerow(row)
    if not found:
        print("Account not found.")


def create_user_account():
    """Creates a new user account by storing a username and password in the users csv file."""
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print("User account created successfully.")


def user_login():
    """Logs a user in by checking if the username and password match the users csv file.

    Returns:
        bool: True if the user is logged in, otherwise False
    """
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [username, password]:
                return True
    return False


def title(text, figlet_font="chunky"):
    """Prints a title in ASCII art using pyfiglet.

    Args:
        text (str): The text to display in ASCII art title.
        figlet_font (str, optional): The figlet font to be used. Defaults to "chunky".
    """
    ascii_title = pyfiglet.figlet_format(text, font=figlet_font)
    print(ascii_title)


def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\n=== Main Menu ===")
        print("1. Create a new user account")
        print("2. Login")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        if choice == 1:
            create_user_account()
        elif choice == 2:
            if user_login():
                print("Login successful.")
                user_menu()
            else:
                print("Login failed. Please check your username and password.")
        elif choice == 3:
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


def user_menu():
    """Displays the user menu and handles user input."""
    while True:
        print("\n=== User Menu ===")
        print("1. Generate a new password")
        print("2. Store a password")
        print("3. Retrieve a password")
        print("4. Update a password")
        print("5. Logout")
        try:
            user_choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
        if user_choice == 1:
            length = int(input("Enter password length: "))
            complexity = int(input("Enter complexity (1-3): "))
            print(f"Generated password: {generate_password(length, complexity)}")
        elif user_choice == 2:
            account_name = input("Enter account name: ")
            password = getpass.getpass("Enter password: ")
            store_password(account_name, password)
            print("Password stored successfully.")
        elif user_choice == 3:
            account_name = input("Enter account name: ")
            password = retrieve_password(account_name)
            if password:
                print(f"Password for {account_name}: {password}")
            else:
                print("Account not found.")
        elif user_choice == 4:
            account_name = input("Enter account name: ")
            new_password = getpass.getpass("Enter new password: ")
            update_password(account_name, new_password)
            print("Password updated successfully.")
        elif user_choice == 5:
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def main():
    """Main function to run the password manager program."""
    try:
        create_password_file()
        create_user_file()
        title("Password Manager", figlet_font="chunky")
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)


if __name__ == "__main__":
    main()
