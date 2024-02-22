# Requirements:
# Classes:
# 1. Define a class named Book.
# 2. The Book class should have an initializer (__init__) method that takes two parameters (besides self): title and author.
# 3. The Book class should have two instance variables: title and author, which are set to the values passed during object creation.
# 4. Define a method get_info within the Book class that returns a string formatted as "Title: [title], Author: [author]", where [title] and [author] are the respective instance variables' values.
# 5. Create an instance of the Book class with the title "1984" and author "George Orwell", and call the get_info method on this instance. Print the result.

# Inheritance and encapsulation:
# 6. Define a class named EBook that inherits from the Book class.
# 7. The EBook class should add an additional parameter to its initializer: file_format (e.g., 'PDF', 'ePub'), with a default value of 'PDF'.
# 8. Ensure that EBook calls the initializer of the Book class to set the title and author.
# 9. Add a private instance variable to EBook named __file_size (representing the file size in MB) and a method to set this variable named set_file_size(size).
# 10. Add another method get_ebook_info to EBook that returns a string formatted as "Title: [title], Author: [author], Format: [format], Size: [size]MB". Ensure this method respects encapsulation principles for accessing __file_size.
# 11. Create an instance of the EBook class with the title "A Brief History of Time", author "Stephen Hawking", and format 'ePub'. Set the file size to 14, and print the eBook information using get_ebook_info.

# Data Validation and Input Validation:
# Ensure you are relevant data validation and input validation in your code


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_format="PDF"):
        super().__init__(title, author)
        self.__file_size = None
        self.file_format = file_format

    def set_file_size(self, size):
        if isinstance(size, int) and size > 0:
            self.__file_size = size
        else:
            raise ValueError("Invalid file size")

    def get_ebook_info(self):
        return f"Title: {self.title}, Author: {self.author}, Format: {self.file_format}, Size: {self.__file_size}MB"


# Example Usage
book = Book("1984", "George Orwell")  # Initialize the book object
print(book.get_info())

ebook = EBook(
    "A Brief History of Time", "Stephen Hawking", "ePub"
)  # Initialize the ebook object
ebook.set_file_size(14)
print(ebook.get_ebook_info())
