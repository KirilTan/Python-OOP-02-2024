class Task:
    """
    A class to represent a task.

    Args:
        name (str): The name of the task.
        due_date (str): The due date of the task.

    Attributes:
        name (str): The name of the task.
        due_date (str): The due date of the task.
        comments (list): A list of comments associated with the task.
        completed (bool): A boolean indicating whether the task is completed or not.

    Methods:
        change_name(new_name: str) -> str: Changes the name of the task and returns the new name.
        change_due_date(new_date: str) -> str: Changes the due date of the task and returns the new date.
        add_comment(comment: str) -> None: Adds a comment to the task.
        edit_comment(comment_number: int, new_comment: str) -> str: Edits a comment of the task and returns the updated list of comments.
        details() -> str: Returns a string containing the details of the task.
    """

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        """
        Changes the name of the task and returns the new name.

        Args:
            new_name (str): The new name of the task.

        Returns:
            str: The new name of the task or an error message if the new name is the same as the old one.
        """
        if new_name != self.name:
            self.name = new_name
            return new_name
        else:
            return 'Name cannot be the same.'

    def change_due_date(self, new_date: str) -> str:
        """
        Changes the due date of the task and returns the new date.

        Args:
            new_date (str): The new due date of the task.

        Returns:
            str: The new due date of the task or an error message if the new date is the same as the old one.
        """
        if new_date != self.due_date:
            self.due_date = new_date
            return new_date
        else:
            return 'Date cannot be the same.'

    def add_comment(self, comment: str) -> None:
        """
        Adds a comment to the task.

        Args:
            comment (str): The comment to be added.
        """
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        """
        Edits a comment of the task and returns the updated list of comments.

        Args:
            comment_number (int): The index of the comment to be edited.
            new_comment (str): The new comment to be set.

        Returns:
            str: The updated list of comments or an error message if the index is out of range.
        """
        try:
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        except IndexError:
            return 'Cannot find comment.'

    def details(self) -> str:
        """
        Returns a string containing the details of the task.

        Returns:
            str: The details of the task.
        """
        text = f'Name: {self.name} - Due Date: {self.due_date}'
        return text
