class Animal:
    """
    This class represents an animal. The Animal class is a base class for any type of animal in the zoo.

    Args:
        name (str): The name of the animal.
        gender (str): The gender of the animal.
        age (int): The age of the animal.
        money_for_care (int): The amount of money required to care for the animal.

    Attributes:
        name (str): The name of the animal.
        gender (str): The gender of the animal.
        age (int): The age of the animal.
        money_for_care (int): The amount of money required to care for the animal.

    """

    def __init__(self, name: str, gender: str, age: int, money_for_care: int) -> None:
        """
        Initialize an animal.

        Args:
            name (str): The name of the animal.
            gender (str): The gender of the animal.
            age (int): The age of the animal.
            money_for_care (int): The amount of money required to care for the animal.

        """
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self) -> str:
        """
        Return a string representation of the animal.

        Returns:
            str: A string representation of the animal.

        """
        text = f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
        return text
