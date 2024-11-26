from student_management_system import StudentManagementSystem


def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Record Grade")
        print("5. Mark Attendance")
        print("6. Generate GPA Report")
        print("7. Generate Attendance Report")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            name = input("Enter student name: ")
            id = input("Enter student ID: ")
            roll_number = input("Enter student roll number: ")
            sms.add_student(name, id, roll_number)

        elif choice == "2":
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            sms.add_course(course_name, course_code)

        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            sms.enroll_student(student_id, course_name)

        elif choice == "4":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            sms.record_grade(student_id, course_name, grade)

        elif choice == "5":
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name: ")
            date = input("Enter attendance date (YYYY-MM-DD): ")
            sms.mark_attendance(student_id, course_name, date)

        elif choice == "6":
            student_id = input("Enter student ID: ")
            sms.generate_gpa_report(student_id)

        elif choice == "7":
            course_name = input("Enter course name: ")
            sms.generate_attendance_report(course_name)

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
