class Person:
    """
    Base class for representing a person.

    Attributes:
        name (str): The name of the person.
        id (str): The unique identifier for the person.
    """

    def __init__(self, name, id):
        """
        Initialize a Person instance.

        Args:
            name (str): The name of the person.
            id (str): The unique identifier for the person.
        """
        self.name = name
        self.id = id

    def __str__(self):
        """
        Return a string representation of the Person instance.

        Returns:
            str: The string representation of the Person instance.
        """
        return f"Name: {self.name}, ID: {self.id}"
