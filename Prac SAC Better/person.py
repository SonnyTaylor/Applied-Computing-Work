# person.py


class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def __str__(self):
        return f"Name: {self.name}, ID: {self.ID}"
