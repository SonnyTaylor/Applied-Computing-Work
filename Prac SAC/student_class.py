from person_class import Person


# Derived from person
class Student(Person):
    """
    Represents a student.

    Attributes:
        roll_number (str): The roll number of the student.
        enrolled_courses (dict): A dictionary containing the enrolled courses of the student.
        attendance (dict): A dictionary containing the attendance records of the student.
    """

    def __init__(self) -> None:
        super().__init__()
        self.roll_number = ""  # The roll number of the student
        self.enrolled_courses = {}  # A dictionary to store enrolled courses
        self.attendance = {}  # A dictionary to store attendance records

    def enroll_course(self, course_name):
        """
        Enrolls the student in a course.

        Args:
            course_name (str): The name of the course to enroll in.
        """
        self.enrolled_courses[course_name] = ""

    def record_grade(self, course_name, grade):
        """
        Records the grade of the student for a course.

        Args:
            course_name (str): The name of the course.
            grade (str): The grade obtained by the student.
        """
        self.enrolled_courses[course_name] = grade

    def mark_attendance(self, course_name, date):
        """
        Marks the attendance of the student for a course on a specific date.

        Args:
            course_name (str): The name of the course.
            date (str): The date of attendance.
        """
        if course_name not in self.attendance:
            self.attendance[course_name] = []
        self.attendance[course_name].append(date)

    def calculate_gpa(self):
        """
        Calculates the GPA (Grade Point Average) of the student.

        Returns:
            float: The GPA of the student.
        """
        total_credits = 0
        total_grade_points = 0
        for course, grade in self.enrolled_courses.items():
            if grade == "A":
                grade_points = 4
            elif grade == "B":
                grade_points = 3
            elif grade == "C":
                grade_points = 2
            elif grade == "D":
                grade_points = 1
            else:
                grade_points = 0
            total_credits += 1
            total_grade_points += grade_points
        if total_credits == 0:
            return 0
        else:
            return total_grade_points / total_credits
