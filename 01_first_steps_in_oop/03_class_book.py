class Book:
    """
    This class represents a book.

    Args:
        name (str): The name of the book.
        author (str): The name of the author.
        pages (int): The number of pages in the book.

    Attributes:
        name (str): The name of the book.
        author (str): The name of the author.
        pages (int): The number of pages in the book.

    """

    def __init__(self, name, author, pages):
        """
        Initialize a Book instance.

        Args:
            name (str): The name of the book.
            author (str): The name of the author.
            pages (int): The number of pages in the book.

        """
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
