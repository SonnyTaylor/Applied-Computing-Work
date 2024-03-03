# student.py
from person import Person


class Student(Person):
    def __init__(self, name, ID, roll_number):
        super().__init__(name, ID)
        self.roll_number = roll_number
        self.enrolled_courses = {}
        self.attendance = {}

    def enroll_course(self, course_name):
        self.enrolled_courses[course_name] = None

    def record_grade(self, course_name, grade):
        if course_name in self.enrolled_courses:
            self.enrolled_courses[course_name] = grade
        else:
            print(f"Error: {self.name} is not enrolled in {course_name}")

    def mark_attendance(self, course_name, date):
        if course_name in self.attendance:
            self.attendance[course_name].append(date)
        else:
            self.attendance[course_name] = [date]

    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0
        for course, grade in self.enrolled_courses.items():
            if grade is not None:
                total_credits += 1
                total_grade_points += grade
        if total_credits == 0:
            return 0
        return total_grade_points / total_credits
