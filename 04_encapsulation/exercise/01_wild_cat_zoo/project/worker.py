class Worker:
    """
    A class that represents a worker. The Worker class is a base class for any type of employee in the zoo.

    Parameters:
    name (str): The name of the worker.
    age (int): The age of the worker.
    salary (int): The salary of the worker.

    Attributes:
    name (str): The name of the worker.
    age (int): The age of the worker.
    salary (int): The salary of the worker.
    """

    def __init__(self, name: str, age: int, salary: int) -> None:
        """
        Initialize a Worker instance.

        Args:
        name (str): The name of the worker.
        age (int): The age of the worker.
        salary (int): The salary of the worker.
        """
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        """
        Return a string representation of the Worker instance.

        Returns:
        str: A string representation of the Worker instance.
        """
        text = f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
        return text
