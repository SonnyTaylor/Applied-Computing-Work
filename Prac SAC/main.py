import sys
from student_management_system_class import StudentManagementSystem as sms
import user_interface as ui


def main():
    print("Welcome to the Student Management System!")
    while True:
        print("1. Add a student")
        print("2. Add a course")
        print("3. Enroll a student in a course")
        print("4. Remove a student from a course")
        print("5. List all students")
        print("6. List all courses")
        print("7. List all students in a course")
        print("8. Calculate a student's GPA")
        print("9. Search for a student")
        print("10. Get student info")
        print("11. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                ui.add_student()
            elif choice == "2":
                ui.add_course()
            elif choice == "3":
                ui.enroll_student()
            elif choice == "4":
                ui.remove_student()
            elif choice == "5":
                ui.list_students()
            elif choice == "6":
                ui.list_courses()
            elif choice == "7":
                ui.list_students_in_course()
            elif choice == "8":
                ui.calculate_gpa()
            elif choice == "9":
                ui.search_student()
            elif choice == "10":
                ui.get_student_info()
            elif choice == "11":
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
