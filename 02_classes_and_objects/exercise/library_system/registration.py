from project.library import Library
from project.user import User


class Registration:
    """
    This class provides the functionality for registering new users and managing their usernames.
    """

    def add_user(self, user: User, library: Library) -> str or None:
        """
        Adds a new user to the system.

        Args:
            user (User): The user object to be added.
            library (Library): The library object that contains the user records.

        Returns:
            str or None: A message indicating whether the user was added or not, or None if no message is required.
        """
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library) -> str or None:
        """
        Removes an existing user from the system.

        Args:
            user (User): The user object to be removed.
            library (Library): The library object that contains the user records.

        Returns:
            str or None: A message indicating whether the user was removed or not, or None if no message is required.
        """
        if user not in library.user_records:
            return "We could not find such user to remove!"

        try:
            del library.rented_books[user.username]
        except KeyError:
            pass
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        """
        Changes the username of an existing user.

        Args:
            user_id (int): The ID of the user whose username is to be changed.
            new_username (str): The new username to be assigned to the user.
            library (Library): The library object that contains the user records and rental history.

        Returns:
            str: A message indicating whether the username was changed or not.
        """
        try:
            user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        try:
            library.rented_books[new_username] = library.rented_books.pop(user.username)
        except KeyError:
            pass

        user.username = new_username

        return f"Username successfully changed to: {new_username} for user id: {user_id}"
