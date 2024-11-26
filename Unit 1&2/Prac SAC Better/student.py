from person import Person


class Student(Person):
    """
    Class representing a student, derived from the Person class.

    Attributes:
        roll_number (str): The roll number of the student.
        enrolled_courses (dict): A dictionary mapping course names to grades.
        attendance (dict): A dictionary mapping course names to lists of attendance dates.
    """

    def __init__(self, name, id, roll_number):
        """
        Initialize a Student instance.

        Args:
            name (str): The name of the student.
            id (str): The unique identifier for the student.
            roll_number (str): The roll number of the student.
        """
        super().__init__(name, id)
        self.roll_number = roll_number
        self.enrolled_courses = {}
        self.attendance = {}

    def enroll_course(self, course_name):
        """
        Enroll the student in a course.

        Args:
            course_name (str): The name of the course to enroll in.
        """
        if course_name in self.enrolled_courses:
            print(f"Student is already enrolled in {course_name}")
        else:
            self.enrolled_courses[course_name] = None
            self.attendance[course_name] = []
            print(f"Student enrolled in {course_name}")

    def record_grade(self, course_name, grade):
        """
        Record the grade for a course.

        Args:
            course_name (str): The name of the course.
            grade (float): The grade to record.
        """
        if course_name not in self.enrolled_courses:
            print(f"Student is not enrolled in {course_name}")
        else:
            self.enrolled_courses[course_name] = grade
            print(f"Grade {grade} recorded for {course_name}")

    def mark_attendance(self, course_name, date):
        """
        Mark the attendance for a course on a specific date.

        Args:
            course_name (str): The name of the course.
            date (str): The date of attendance in "YYYY-MM-DD" format.
        """
        if course_name not in self.attendance:
            print(f"Student is not enrolled in {course_name}")
        else:
            self.attendance[course_name].append(date)
            print(f"Attendance marked for {course_name} on {date}")

    def calculate_gpa(self):
        """
        Calculate the overall GPA of the student.

        Returns:
            float: The overall GPA of the student.
        """
        total_grade = 0
        num_courses = 0
        for grade in self.enrolled_courses.values():
            if grade is not None:
                total_grade += grade
                num_courses += 1
        if num_courses == 0:
            return 0.0
        return total_grade / num_courses
