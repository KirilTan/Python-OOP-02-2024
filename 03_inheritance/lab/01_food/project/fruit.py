from ex_1_and_2.project import Food


class Fruit(Food):
    """
    A class that represents a fruit.

    Parameters:
        name (str): The name of the fruit.
        expiration_date (str): The expiration date of the fruit.

    Attributes:
        name (str): The name of the fruit.
        expiration_date (str): The expiration date of the fruit.
    """

    def __init__(self, name: str, expiration_date: str):
        """
        Initialize a Fruit object.

        Args:
            name (str): The name of the fruit.
            expiration_date (str): The expiration date of the fruit.
        """
        self.name = name
        super().__init__(expiration_date)
