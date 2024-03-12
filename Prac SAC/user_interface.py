import os
from student_management_system_class import StudentManagementSystem as sms

sms_instance = sms()


def clear_terminal():
    """clears the screen of the terminal."""
    if os.name == "nt":
        # Windows
        os.system("cls")
    else:
        # Linux
        os.system("clear")


def add_course():
    """adds a course to the system."""
    course_code = input("Enter the course code: ")
    course_name = input("Enter the course name: ")
    sms_instance.add_course(course_code, course_name)
    print(f"Course {course_code} has been added to the system.")


def add_student():
    """adds a student to the system."""
    student_id = int(input("Enter the student ID: "))
    student_name = input("Enter the student name: ")
    sms_instance.add_student(student_id, student_name)
    print(f"Student {student_id} has been added to the system.")


def remove_student():
    """remove a student from the system"""
    student_id = input("Enter the student ID: ")
    course_code = input("Enter the course code: ")
    sms_instance.remove_student(student_id, course_code)
    print(f"Student {student_id} has been removed from course {course_code}.")


def enroll_student():
    """enroll a student into a course"""
    student_id = input("Enter the student ID: ")
    course_code = input("Enter the course code: ")
    sms_instance.enroll_student(student_id, course_code)
    print(f"Student {student_id} has been enrolled in course {course_code}.")


def list_students():
    """lists all students"""
    students = sms_instance.list_students()
    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")


def list_courses():
    """lists all courses"""
    courses = sms_instance.list_courses()
    if courses:
        for course in courses:
            print(course)
    else:
        print("No courses found.")


def list_students_in_course():
    """lists all students in a course"""
    course_code = input("Enter the course code: ")
    students = sms_instance.list_students_in_course(course_code)
    if students:
        for student in students:
            print(student)
    else:
        print("No students found in course", course_code)


def calculate_gpa():
    """calculate the gpa of a student"""
    student_id = input("Enter the student ID: ")
    gpa = sms_instance.calculate_gpa(student_id)
    if gpa is not None:
        print(f"The GPA of student {student_id} is {gpa:.2f}.")
    else:
        print(f"No student found with ID {student_id}.")


def search_student():
    """search for a student in the system."""
    student_id = input("Enter the student ID: ")
    student = sms_instance.search_student(student_id)
    if student:
        print(student)
    else:
        print(f"No student found with ID {student_id}.")


def get_student_info():
    """get student info"""
    student_id = input("Enter the student ID: ")
    student = sms_instance.get_student_info(student_id)
    if student:
        print(student)
    else:
        print(f"No student found with ID {student_id}.")
