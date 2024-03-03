from typing import List, Dict

from user import User


class Library:
    """
    A class that represents a library.

    Attributes:
        user_records (List[User]): A list of users.
        books_available (Dict[str, List[str]]): A dictionary that maps authors to a list of available book titles.
        rented_books (Dict[str, Dict[str, int]]): A dictionary that maps users to a dictionary that maps book titles
                                                  to the number of days they have been rented.
    """

    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str, List[str]] = {}
        self.rented_books: Dict[str, Dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        """
        Rents a book from the library.

        Args:
            author (str): The author of the book.
            book_name (str): The title of the book.
            days_to_return (int): The number of days the book should be rented for.
            user (User): The user renting the book.

        Returns:
            str: A message indicating whether the book was rented successfully or not.
        """
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for data in self.rented_books.values():
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        """
        Returns a book to the library.

        Args:
            author (str): The author of the book.
            book_name (str): The title of the book.
            user (User): The user returning the book.

        Returns:
            str: A message indicating whether the book was returned successfully or not.
        """
        if book_name not in self.rented_books[user.username]:
            return f"{user.username} doesn't have this book in his/her records!"

        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        
        