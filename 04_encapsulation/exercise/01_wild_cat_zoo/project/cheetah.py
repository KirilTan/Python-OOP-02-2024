from project.animal import Animal


class Cheetah(Animal):
    """
    This class represents a cheetah.

    Parameters:
        name (str): The name of the cheetah.
        gender (str): The gender of the cheetah.
        age (int): The age of the cheetah.
        money_for_care (int): The amount of money required to care for the cheetah.

    Attributes:
        name (str): The name of the cheetah.
        gender (str): The gender of the cheetah.
        age (int): The age of the cheetah.
        money_for_care (int): The amount of money required to care for the cheetah.
    """

    def __init__(self, name: str, gender: str, age: int) -> None:
        """
        Initialize a new Cheetah instance.

        Args:
            name (str): The name of the cheetah.
            gender (str): The gender of the cheetah.
            age (int): The age of the cheetah.
            money_for_care (int): The amount of money required to care for the cheetah.
        """
        super().__init__(name, gender, age, 60)

