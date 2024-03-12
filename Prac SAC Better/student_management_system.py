from student import Student
from course import Course


class StudentManagementSystem:
    """
    Class representing the student management system.

    Attributes:
        students (list): A list of Student instances.
        courses (list): A list of Course instances.
    """

    def __init__(self):
        """
        Initialize the StudentManagementSystem instance.
        """
        self.students = []
        self.courses = []

    def add_student(self, name, id, roll_number):
        """
        Add a new student to the system.

        Args:
            name (str): The name of the student.
            id (str): The unique identifier for the student.
            roll_number (str): The roll number of the student.
        """
        student = Student(name, id, roll_number)
        self.students.append(student)
        print(f"Student {name} with ID {id} and roll number {roll_number} added")

    def add_course(self, course_name, course_code):
        """
        Add a new course to the system.

        Args:
            course_name (str): The name of the course.
            course_code (str): The code of the course.
        """
        course = Course(course_name, course_code)
        self.courses.append(course)
        print(f"Course {course_name} with code {course_code} added")

    def enroll_student(self, student_id, course_name):
        """
        Enroll a student in a course.

        Args:
            student_id (str): The unique identifier of the student.
            course_name (str): The name of the course to enroll in.
        """
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_name(course_name)
        if student and course:
            course.add_student(student)
        else:
            print("Invalid student ID or course name")

    def record_grade(self, student_id, course_name, grade):
        """
        Record a grade for a student in a course.

        Args:
            student_id (str): The unique identifier of the student.
            course_name (str): The name of the course.
            grade (float): The grade to record.
        """
        student = self.find_student_by_id(student_id)
        if student:
            student.record_grade(course_name, grade)
        else:
            print("Invalid student ID")

    def mark_attendance(self, student_id, course_name, date):
        """
        Mark the attendance of a student in a course on a specific date.

        Args:
            student_id (str): The unique identifier of the student.
            course_name (str): The name of the course.
            date (str): The date of attendance in "YYYY-MM-DD" format.
        """
        student = self.find_student_by_id(student_id)
        if student:
            student.mark_attendance(course_name, date)
        else:
            print("Invalid student ID")

    def generate_gpa_report(self, student_id):
        """
        Generate a GPA report for a student.

        Args:
            student_id (str): The unique identifier of the student.
        """
        student = self.find_student_by_id(student_id)
        if student:
            gpa = student.calculate_gpa()
            print(f"GPA Report for {student.name} ({student.roll_number}):")
            print(f"Overall GPA: {gpa:.2f}")
            print("Grades:")
            for course, grade in student.enrolled_courses.items():
                print(f"{course}: {grade if grade is not None else 'N/A'}")
        else:
            print("Invalid student ID")

    def generate_attendance_report(self, course_name):
        """
        Generate an attendance report for a course.

        Args:
            course_name (str): The name of the course.
        """
        course = self.find_course_by_name(course_name)
        if course:
            print(f"Attendance Report for {course.course_name} ({course.course_code}):")
            for student in course.enrolled_students:
                attendance_dates = student.attendance.get(course_name, [])
                print(f"{student.name} ({student.roll_number}):")
                if not attendance_dates:
                    print("  No attendance records")
                else:
                    print("  Attendance dates:")
                    for date in attendance_dates:
                        print(f"    {date}")
        else:
            print("Invalid course name")

    def find_student_by_id(self, student_id):
        """
        Find a student by their unique identifier.

        Args:
            student_id (str): The unique identifier of the student.

        Returns:
            Student: The Student instance if found, None otherwise.
        """
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def find_course_by_name(self, course_name):
        """
        Find a course by its name.

        Args:
            course_name (str): The name of the course.

        Returns:
            Course: The Course instance if found, None otherwise.
        """
        for course in self.courses:
            if course.course_name == course_name:
                return course
        return None
