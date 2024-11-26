class Course:
    def __init__(self) -> None:
        self.course_name = ""  # The name of the course
        self.course_code = ""  # The code of the course
        self.enrolled_students = []  # A list to store enrolled students

    def add_student(self, student):
        """
        Adds a student to the course.

        Args:
            student (Student): The student to add.
        """
        self.enrolled_students.append(student)

    def remove_student(self, student):
        """
        Removes a student from the course.

        Args:
            student (Student): The student to remove.
        """
        self.enrolled_students.remove(student)

    def list_enrolled_students(self):
        """
        Lists all the enrolled students in the course.
        """
        for student in self.enrolled_students:
            print(student)
