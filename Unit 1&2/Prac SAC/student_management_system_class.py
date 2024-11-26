import json


class StudentManagementSystem:
    def __init__(self):
        self.data = self.load_data("database.json")

    def load_data(self, filename):
        """
        Loads data from a JSON file.

        Args:
            filename (str): The name of the JSON file.

        Returns:
            dict: The loaded data.
        """
        with open(filename, "r") as file:
            data = json.load(file)
        return data

    def save_data(self, filename):
        """
        Saves data to a JSON file.

        Args:
            filename (str): The name of the JSON file.
        """
        with open(filename, "w") as file:
            json.dump(self.data, file)

    def add_student(self, student, student_id):
        """
        Adds a student to the student management system.

        Args:
            student (Student): The student to add.
            student_id (int): The ID of the student.
        """
        if not isinstance(student_id, int):
            try:
                student_id = int(student_id)
            except ValueError:
                raise ValueError("student_id must be an integer")

        student["id"] = student_id
        self.data["students"].append(student)

    def add_course(self, course):
        """
        Adds a course to the student management system.

        Args:
            course (Course): The course to add.
        """
        self.data["courses"].append(course)

    def enroll_student(self, student, course):
        """
        Enrolls a student in a course.

        Args:
            student (Student): The student to enroll.
            course (Course): The course to enroll in.
        """
        course.add_student(student)

    def search_student(self, student):
        """
        Searches for a student in the student management system.

        Args:
            student (Student): The student to search for.
        """
        for s in self.data["students"]:
            if s["name"] == student["name"]:
                return s
        return None

    def record_grade(self, student, course, grade):
        """
        Records the grade of a student for a course.

        Args:
            student (Student): The student.
            course (Course): The course.
            grade (str): The grade obtained by the student.
        """
        for s in self.data["students"]:
            if s["name"] == student["name"]:
                s["grades"][course["course_name"]] = grade
                break

    def record_attendance(self, student, course, date):
        """
        Records the attendance of a student for a course on a specific date.

        Args:
            student (Student): The student.
            course (Course): The course.
            date (str): The date of attendance.
        """
        for s in self.data["students"]:
            if s["name"] == student["name"]:
                if course["course_name"] not in s["attendance"]:
                    s["attendance"][course["course_name"]] = []
                s["attendance"][course["course_name"]].append(date)
                break

    def generate_gpa_report(self, student):
        """
        Generates a GPA report for a student.

        Args:
            student (Student): The student.
        """
        for s in self.data["students"]:
            if s["name"] == student["name"]:
                grades = s["grades"]
                total_grades = len(grades)
                if total_grades > 0:
                    gpa = sum(grades.values()) / total_grades
                else:
                    gpa = 0.0
                print(f"Student: {student['name']}, GPA: {gpa}")
                break

    def generate_attendance_report(self, course):
        """
        Generates an attendance report for a course.

        Args:
            course (Course): The course.
        """
        for c in self.data["courses"]:
            if c["course_name"] == course["course_name"]:
                print(f"Course: {course['course_name']}")
                for student in c["enrolled_students"]:
                    attendance = len(
                        student["attendance"].get(course["course_name"], [])
                    )
                    print(f"Student: {student['name']}, Attendance: {attendance}")
                break
