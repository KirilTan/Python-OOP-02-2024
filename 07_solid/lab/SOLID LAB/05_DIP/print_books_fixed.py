from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @staticmethod
    @abstractmethod
    def format(book: Book) -> str:
        ...


class BaseFormatter(Formatter):

    @staticmethod
    def format(book: Book) -> str:
        return book.content


class AngryFormatter(Formatter):
    @staticmethod
    def format(book: Book) -> str:
        return book.content.upper()


class PoliteFormatter(Formatter):
    @staticmethod
    def format(book: Book) -> str:
        return book.content.lower()


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book


# Test code
my_book = Book(content='Hello World')

base = BaseFormatter()
angry = AngryFormatter()
polite = PoliteFormatter()

print(Printer.get_book(book=my_book,
                       formatter=base))
print(Printer.get_book(book=my_book,
                       formatter=angry))
print(Printer.get_book(book=my_book,
                       formatter=polite))
