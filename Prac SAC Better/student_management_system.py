# student_management_system.py
import json
from student import Student
from course import Course


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student, course):
        if student in self.students and course in self.courses:
            course.add_student(student)
            student.enroll_course(course.course_name)
        else:
            print("Error: Student or course not found")

    def record_grade(self, student, course, grade):
        if student in self.students and course in self.courses:
            student.record_grade(course.course_name, grade)
        else:
            print("Error: Student or course not found")

    def mark_attendance(self, student, course, date):
        if student in self.students and course in self.courses:
            student.mark_attendance(course.course_name, date)
        else:
            print("Error: Student or course not found")

    def generate_gpa_report(self, student):
        if student in self.students:
            return student.calculate_gpa()
        else:
            print("Error: Student not found")

    def generate_attendance_report(self, course):
        if course in self.courses:
            return course.list_students()
        else:
            print("Error: Course not found")

    def save_data(self, filename):
        data = {
            "students": [student.__dict__ for student in self.students],
            "courses": [course.__dict__ for course in self.courses],
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.students = [Student(**student) for student in data["students"]]
            self.courses = [Course(**course) for course in data["courses"]]


def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll Student in Course")
        print("4. Record Grade")
        print("5. Mark Attendance")
        print("6. Generate GPA Report")
        print("7. Generate Attendance Report")
        print("8. Display Students")
        print("9. Display Courses")
        print("10. Save Data")
        print("11. Load Data")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            ID = input("Enter student ID: ")
            roll_number = input("Enter student roll number: ")
            student = Student(name, ID, roll_number)
            system.add_student(student)
            print(f"Student {name} added successfully")

        elif choice == "2":
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            course = Course(course_name, course_code)
            system.add_course(course)
            print(f"Course {course_name} added successfully")

        elif choice == "3":
            student_name = input("Enter student name: ")
            course_name = input("Enter course name: ")
            student = next((s for s in system.students if s.name == student_name), None)
            course = next(
                (c for c in system.courses if c.course_name == course_name), None
            )
            if student and course:
                system.enroll_student(student, course)
                print(f"{student_name} enrolled in {course_name} successfully")
            else:
                print("Error: Student or course not found")

        elif choice == "4":
            student_name = input("Enter student name: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            student = next((s for s in system.students if s.name == student_name), None)
            course = next(
                (c for c in system.courses if c.course_name == course_name), None
            )
            if student and course:
                system.record_grade(student, course, grade)
                print(f"Grade recorded for {student_name} in {course_name}")
            else:
                print("Error: Student or course not found")

        elif choice == "5":
            student_name = input("Enter student name: ")
            course_name = input("Enter course name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            student = next((s for s in system.students if s.name == student_name), None)
            course = next(
                (c for c in system.courses if c.course_name == course_name), None
            )
            if student and course:
                system.mark_attendance(student, course, date)
                print(f"Attendance marked for {student_name} in {course_name}")
            else:
                print("Error: Student or course not found")

        elif choice == "6":
            student_name = input("Enter student name: ")
            student = next((s for s in system.students if s.name == student_name), None)
            if student:
                gpa = system.generate_gpa_report(student)
                print(f"GPA for {student_name}: {gpa}")
            else:
                print("Error: Student not found")

        elif choice == "7":
            course_name = input("Enter course name: ")
            course = next(
                (c for c in system.courses if c.course_name == course_name), None
            )
            if course:
                students = system.generate_attendance_report(course)
                print(f"Students enrolled in {course_name}: {students}")
            else:
                print("Error: Course not found")

        elif choice == "8":
            print("\nStudents:")
            for student in system.students:
                print(student)

        elif choice == "9":
            print("\nCourses:")
            for course in system.courses:
                print(course)

        elif choice == "10":
            filename = input("Enter filename to save data: ")
            system.save_data(filename)
            print("Data saved successfully")

        elif choice == "11":
            filename = input("Enter filename to load data: ")
            system.load_data(filename)
            print("Data loaded successfully")

        elif choice == "12":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
