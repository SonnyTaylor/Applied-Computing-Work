from book_manager_functions import (
    Bookmanager,
)  # Import the Bookmanager class from the book_manager_functions module
import sys  # Import the sys module to use the exit function

book_manager = Bookmanager()  # Initating the class
books = book_manager.books

logo = r"""
______             _     ___  ___                                  
| ___ \           | |    |  \/  |                                  
| |_/ / ___   ___ | | __ | .  . | __ _ _ __   __ _  __ _  ___ _ __ 
| ___ \/ _ \ / _ \| |/ / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_/ / (_) | (_) |   <  | |  | | (_| | | | | (_| | (_| |  __/ |   
\____/ \___/ \___/|_|\_\ \_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|   
                                                    __/ |          
                                                   |___/ 
"""


def main():
    print(logo)
    while True:
        print("Menu:")
        print("1. Add a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Display all books")
        print("5. Search books")
        print("6. Delete all books")
        print("7. Check out a book")
        print("8. Check in a book")
        print("9. Exit")

        choice = input("Enter a number: ")

        match choice:
            case "1":
                book_manager.clear_terminal()
                book_manager.add_books(books)
            case "2":
                book_manager.clear_terminal()
                book_manager.display_books(books)
                book_manager.update_book(books)
            case "3":
                book_manager.clear_terminal()
                book_manager.display_books(books)
                book_manager.delete_book(books)
            case "4":
                book_manager.clear_terminal()
                book_manager.display_books(books)
            case "5":
                book_manager.clear_terminal()
                book_manager.search_books(books)
            case "6":
                book_manager.clear_terminal()
                book_manager.delete_all_books(books)
            case "7":
                book_manager.clear_terminal()
                book_manager.check_out_book(books)
            case "8":
                book_manager.clear_terminal()
                book_manager.display_books(books)
                book_manager.check_in_book(books)
            case "9":
                print("Exiting program...")
                book_manager.clear_terminal()
                sys.exit()
            case _:
                print("Invalid choice. Please enter a number between 1 and 9.")
                book_manager.press_enter_to_continue()
                book_manager.clear_terminal()


if __name__ == "__main__":
    # run the main loop
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program...")
        book_manager.clear_terminal()
        sys.exit()
    except EOFError:
        print("\nExiting program...")
        book_manager.clear_terminal()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        book_manager.press_enter_to_continue()
        book_manager.clear_terminal()
