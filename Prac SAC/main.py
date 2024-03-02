# main.py

import lib.user_interface as user_interface
import lib.json_db_management as db
import lib.student_management_system as stud
import sys  # Import the sys module to use the exit function

students = db.load_students("students.json")


def main():
    user_interface.clear_terminal()

    while True:
        # Print logo and menu
        print(
            user_interface.TBLUE
            + user_interface.student_management_logo
            + user_interface.TWHITE
        )
        print("1. Add/Remove a student")
        print("2. Add/Remove a course")
        print("3. Mark Attendance")
        print("4. Entroll students")
        print("5. View GPA Reports")
        print("6. View attendance")
        print("7. Generate report")
        print("8. Search students")

        choice = input(
            user_interface.TBLUE + "Enter a number: " + user_interface.TDEFAULT
        )

        match choice:
            case "1":
                user_interface.clear_terminal()
                user_interface.add_remove_student(students)
            case "2":
                user_interface.clear_terminal()
                user_interface.add_remove_course()
            case "3":
                user_interface.clear_terminal()
                user_interface.mark_attendance()
            case "4":
                user_interface.clear_terminal()
                user_interface.enroll_students()
            case "5":
                user_interface.clear_terminal()
                user_interface.view_gpa_reports()
            case "6":
                user_interface.clear_terminal()
                user_interface.view_attendance()
            case "7":
                user_interface.clear_terminal()
                user_interface.generate_report()
            case "8":
                user_interface.clear_terminal()
                user_interface.search_students(students)
            case "9":
                print("Exiting program...")
                db.save_students(students, "students.json")
                user_interface.clear_terminal()
                sys.exit()  # Use the exit function from the sys module to exit the program
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
                user_interface.press_enter_to_continue()
                user_interface.clear_terminal()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program...")
        db.save_students(students, "students.json")
        user_interface.clear_terminal()
        sys.exit()
    except EOFError:
        print("\nExiting program...")
        db.save_students(students, "students.json")
        user_interface.clear_terminal()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        user_interface.press_enter_to_continue()
        user_interface.clear_terminal()
