# Implement a Student class that inherits from Person and adds attributes for roll_number, enrolled_courses (a dictionary to store course names as keys and grades as values), and attendance (a dictionary with course names as keys and lists of dates present as values).
# Include methods to enroll in a course, record a grade for a course, mark attendance, and calculate overall GPA.

from person import Person


class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.enrolled_courses = {}
        self.attendance = {}

    def enroll_course(self, course_name):
        self.enrolled_courses[course_name] = None

    def record_grade(self, course_name, grade):
        if course_name in self.enrolled_courses:
            self.enrolled_courses[course_name] = grade
        else:
            print("Course not found.")

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
                credits = 3  # Assuming all courses have 3 credits
                total_credits += credits
                total_grade_points += grade * credits

        if total_credits == 0:
            return 0

        return total_grade_points / total_credits
