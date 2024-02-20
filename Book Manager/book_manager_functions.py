from re import search
import sys  # Import the sys module to use the exit function
import os  # Import the os module to clear the terminal
from datetime import (
    date,
)  # Import the date class from the datetime module to be used for last_checked_out


class Bookmanager:
    def __init__(self):
        # premade list of all books
        self.books = {
            "The Great Gatsby": {
                "name": "The Great Gatsby",
                "year": 1925,
                "author": "F. Scott Fitzgerald",
                "last_checked_out": None,
                "checked_out": False,
            },
            "To Kill a Mockingbird": {
                "name": "To Kill a Mockingbird",
                "year": 1960,
                "author": "Harper Lee",
                "last_checked_out": None,
                "who_checked_out": None,
                "checked_out": True,
            },
        }

    def todays_date(self):
        """Returns the current date in the format of DD-MM-YYYY"""
        return date.today().strftime("%d-%m-%Y")

    def clear_terminal(self):
        """
        Clears the terminal screen.
        """
        match os.name:
            case "nt":  # Windows
                os.system("cls")
            case "posix":  # linux or macOS
                os.system("clear")
            case _:
                print(
                    "Unsupported operating system, clearing terminal is not supported"
                )

    def press_enter_to_continue(self):
        """Prints a message to the console and waits for the user to press enter."""
        enter = input("Press enter to continue")
        match enter:
            case None:
                self.clear_terminal()
                return
            case _:
                self.clear_terminal()
                return

    def add_books(self, books):
        """Gets user input to add a new contact

        Args:
            books (dict): A dictionary containing the existing books.
        """
        book_name = input("Enter book name: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        year = input("Enter year: ")
        quantity = input("Enter quantity: ")
        # print confirmation details about book
        self.clear_terminal()
        print("Book added successfully.")
        print(f"Book name: {book_name}")
        print(f"Author: {author}")
        print(f"Genre: {genre}")
        print(f"Year: {year}")
        print(f"Quantity: {quantity}")
        input("Press enter to continue...")
        self.clear_terminal()

    def display_books(self, books):
        """Displays all books

        Args:
            books (dict): A dictionary containing the existing books.
        """
        for book in books:
            print(f"Book name: {books[book]['name']}")
            print(f"Author: {books[book]['author']}")
            print(f"Year: {books[book]['year']}")
            print(f"Last checked out: {books[book]['last_checked_out']}")
            print(f"Checked out: {books[book]['checked_out']}")
            print("\n")
        self.press_enter_to_continue()
        self.clear_terminal()

    def delete_book(self, books):
        """Deletes a book

        Args:
            books (dict): A dictionary containing the existing books.
        """
        book_name = input("Enter book name to delete: ")
        if book_name in books:
            del books[book_name]
            print("Book deleted successfully.")
        else:
            print("Book not found.")
        self.press_enter_to_continue()
        self.clear_terminal()

    def check_out_book(self, books):
        """Checks out a book

        Args:
            books (dict): A dictionary containing the existing books.
        """
        user_name = input("Enter your name: ")
        book_to_check_out = input("Enter book name to check out: ")
        if book_to_check_out in books:
            if books[book_to_check_out]["checked_out"]:
                print("Book already checked out.")
            else:
                books[book_to_check_out]["checked_out"] = Bookmanager.todays_date(self)
                books[book_to_check_out]["last_checked_out"] = user_name
                print("Book checked out successfully.")
        Bookmanager.press_enter_to_continue(self)
        Bookmanager.clear_terminal(self)

    def delete_all_books(self, books):
        """Deletes all books

        Args:
            books (dict): A dictionary containing the existing books.
        """
        confirm = input("Are you sure you want to delete all books? (y/n): ")
        if confirm.lower() == "y":
            books.clear()
            print("All books deleted successfully.")
        else:
            print("No books were deleted.")
        self.press_enter_to_continue()
        self.clear_terminal()

    def search_books(self, books):
        """Searches for a book

        Args:
            books (dict): A dictionary containing the existing books.
        """
        search_term = input("Enter book name, author, or year to search for: ").lower()
        found = False
        print("Search results:")
        for book_name, info in books.items():
            if (
                search_term in book_name.lower()
                or search_term in info["name"].lower()
                or search_term in str(info["year"]).lower()
                or search_term in info["author"].lower()
            ):
                print(
                    f"Book Name: {book_name}, Author: {info['author']}, Year: {info['year']}"
                )
                print(
                    "--------------------------------------------------------------------"
                )
                found = True
        if not found:
            print("Book not found.")
        self.press_enter_to_continue()

    def check_in_book(self, books):
        """Checks in a book

        Args:
            books (dict): A dictionary containing the existing books.
        """
        book_to_check_in = input("Enter book name to check in: ")
        if book_to_check_in in books:
            if not books[book_to_check_in]["checked_out"]:
                print("Book already checked in.")
            else:
                books[book_to_check_in]["checked_out"] = False
                books[book_to_check_in]["last_checked_out"] = None
                print("Book checked in successfully.")
        else:
            print("Book not found.")
        self.press_enter_to_continue()

    def update_book(self, books):
        """Updates a book

        Args:
            books (dict): A dictionary containing the existing books.
        """
        book_name = input("Enter book name to update: ")
        if book_name in books:
            new_book_name = input(
                "Enter new book name (leave blank to keep it the same): "
            )
            new_author = input("Enter new author (leave blank to keep it the same): ")
            new_year = input("Enter new year (leave blank to keep it the same): ")
            if new_book_name:
                books[book_name]["name"] = new_book_name
            if new_author:
                books[book_name]["author"] = new_author
            if new_year:
                books[book_name]["year"] = new_year
            print("Book updated successfully.")
        else:
            print("Book not found.")
        self.press_enter_to_continue()
