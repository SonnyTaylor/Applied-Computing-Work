class Person:
    """Represents a person."""

    def __init__(self) -> None:
        self.name = ""  # The name of the person
        self.student_id = ""  # The ID of the person

    def __str__(self) -> str:
        """Returns a string representation of the person.
        Returns:
            str: A string in the format "Name: {name}, Student ID: {student_id}".
        """
        return f"Name: {self.name}, Student ID: {self.student_id}"
