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


book = Book("1984", "George Orwell")
print(book.get_info())

ebook = EBook("A Brief History of Time", "Stephen Hawking", "ePub")
ebook.set_file_size(14)
print(ebook.get_ebook_info())
