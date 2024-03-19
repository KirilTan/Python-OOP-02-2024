from project.animal import Animal


class Tiger(Animal):
    """
    This class represents a Tiger in the Project.

    Parameters:
        name (str): The name of the Tiger.
        gender (str): The gender of the Tiger.
        age (int): The age of the Tiger.
        money_for_care (int): The amount of money required to care for the Tiger.

    Attributes:
        name (str): The name of the Tiger.
        gender (str): The gender of the Tiger.
        age (int): The age of the Tiger.
        money_for_care (int): The amount of money required to care for the Tiger.

    """

    def __init__(self, name: str, gender: str, age: int) -> None:
        """
        Initialize a Tiger object.

        Args:
            name (str): The name of the Tiger.
            gender (str): The gender of the Tiger.
            age (int): The age of the Tiger.

        """
        super().__init__(name, gender, age, 45)
