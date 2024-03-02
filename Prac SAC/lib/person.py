# 	• Create a base class Person with attributes for name and ID.
# 	• Include a constructor that initializes these attributes.
#   - Implement a __str__ method to return a string representation of the person.


class Person:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}"
