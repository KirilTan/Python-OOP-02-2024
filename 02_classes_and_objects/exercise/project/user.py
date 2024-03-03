from typing import List


class User:
    """
    This class represents a user in the library system.
    It contains information about the user's ID, username, and a list of books that they have rented.
    """

    def __init__(self, user_id: int, username: str):
        """
        Initializes a new instance of the User class.

        Args:
            user_id (int): The ID of the user.
            username (str): The username of the user.
        """
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []

    def info(self) -> str:
        """
        Returns a string containing the books currently rented by the user

        Returns:
            str: A string containing the books currently rented by the user
                 in ascending order separated by a comma and space.
        """
        text = ', '.join(sorted(self.books)) or '[]'
        return text

    def __str__(self):
        """
        Returns a string in the format: "{user_id}, {username}, {list of rented books}".

        Returns:
            str: A string in the format: "{user_id}, {username}, {list of rented books}".
        """
        text = f"{self.user_id}, {self.username}, {self.info()}"
        return text
    