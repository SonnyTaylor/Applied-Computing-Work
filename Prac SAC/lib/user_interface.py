from main import main
import student_management_system as stud
import os

TGREEN = "\033[32m"
TWHITE = "\033[37m"
TBLUE = "\033[34m"
TRED = "\033[31m"
TYELLOW = "\033[33m"
TBOLD = "\033[1m"
TUNDERLINE = "\033[4m"
TNOUNDERLINE = "\033[24m"
TDEFAULT = "\033[0m"
TPURPLE = "\033[35m"
TCYAN = "\033[36m"


student_management_logo = r"""WIP"""


def press_enter_to_continue():
    """Prints a message to the console and waits for the user to press enter."""
    enter = input(TGREEN + TUNDERLINE + "Press enter to continue" + TDEFAULT)
    match enter:
        case None:
            clear_terminal()
            return
        case _:
            clear_terminal()
            return


def clear_terminal():
    """
    Clears the terminal screen.
    """
    match os.name:
        case "nt":  # Windows
            os.system("cls")
        case "posix":  # Sigma Linux or macOS
            os.system("clear")
        case _:
            # Super niche message that most people should never see, only occurs if user doesnt run Windows, Linux or MacOS. Like seriously though, who uses anything else besides Windows, Linux, or macOS? maybe if this were in some kind of embedded program but like really though.
            print("Unsupported operating system, clearing terminal is not supported")


def add_remove_student(students):
    print("Would you like to add or remove a student?")
    print("1. Add student")
    print("2. Remove student")
    print("3. Return to main menu")
    choice = input("Enter a number: ")
    match choice:
        case "1":
            print("Enter student details")
            student_name = input("Enter student name: ")
            student_ID = input("Enter student ID: ")
            student_email = input("Enter student email: ")
            student_password = input("Enter student password: ")
            student_dob = input("Enter date of birth (dd/mm/yyyy): ")
            print("Adding student...")

        case "2":
            print("Removing student...")
        case "3":
            print("Returning to main menu...")
            main.main()

        case _:
            print("Invalid choice. Please enter a number between 1 and 3.")
