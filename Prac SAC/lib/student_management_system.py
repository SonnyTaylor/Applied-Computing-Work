# Implement a StudentManagementSystem class that manages the entire system. This class should maintain a list of all students and a list of all courses.
# Include methods to add a new student, add a new course, enroll a student in a course, record grades, record attendance, generate a GPA report for a student, and generate an attendance report for a course.


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student, course):
        student.enroll_course(course)

    def record_grade(self, student, course, grade):
        student.record_grade(course, grade)

    def mark_attendance(self, student, course, date):
        student.mark_attendance(course, date)

    def generate_gpa_report(self, student):
        return student.calculate_gpa()

    def generate_attendance_report(self, course):
        return course.calculate_attendance()
