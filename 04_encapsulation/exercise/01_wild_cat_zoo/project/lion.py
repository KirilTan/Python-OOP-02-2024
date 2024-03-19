from project.animal import Animal


class Lion(Animal):
    """
    This class represents a lion in the project.

    Parameters:
        name (str): The name of the lion.
        gender (str): The gender of the lion.
        age (int): The age of the lion.
        money_for_care (int): The amount of money required to care for the lion.

    Attributes:
        name (str): The name of the lion.
        gender (str): The gender of the lion.
        age (int): The age of the lion.
        money_for_care (int): The amount of money required to care for the lion.

    """

    def __init__(self, name: str, gender: str, age: int) -> None:
        """
        Initialize a new Lion object.

        Args:
            name (str): The name of the lion.
            gender (str): The gender of the lion.
            age (int): The age of the lion.

        """
        super().__init__(name, gender, age, 50)
