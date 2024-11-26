class Course:
    """
    Class representing a course.

    Attributes:
        course_name (str): The name of the course.
        course_code (str): The code of the course.
        enrolled_students (list): A list of Student instances enrolled in the course.
    """

    def __init__(self, course_name, course_code):
        """
        Initialize a Course instance.

        Args:
            course_name (str): The name of the course.
            course_code (str): The code of the course.
        """
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []

    def add_student(self, student):
        """
        Add a student to the course.

        Args:
            student (Student): The Student instance to add.
        """
        if student in self.enrolled_students:
            print(f"{student.name} is already enrolled in {self.course_name}")
        else:
            self.enrolled_students.append(student)
            student.enroll_course(self.course_name)
            print(f"{student.name} enrolled in {self.course_name}")

    def remove_student(self, student):
        """
        Remove a student from the course.

        Args:
            student (Student): The Student instance to remove.
        """
        if student not in self.enrolled_students:
            print(f"{student.name} is not enrolled in {self.course_name}")
        else:
            self.enrolled_students.remove(student)
            del student.enrolled_courses[self.course_name]
            del student.attendance[self.course_name]
            print(f"{student.name} removed from {self.course_name}")

    def list_students(self):
        """
        List all students enrolled in the course.
        """
        if not self.enrolled_students:
            print(f"No students enrolled in {self.course_name}")
        else:
            print(f"Students enrolled in {self.course_name}:")
            for student in self.enrolled_students:
                print(f"- {student.name} ({student.roll_number})")
