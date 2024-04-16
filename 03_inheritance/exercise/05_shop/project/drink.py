from ex_1_and_2.project import Product


class Drink(Product):
    """
    A drink is a product that has a name and a quantity.

    Attributes:
        name (str): The name of the drink.
        quantity (int): The quantity of the drink.

    """

    DEFAULT_DRINK_QUANTITY: int = 10

    def __init__(self, name: str):
        """
        Initialize a drink with a name.

        Args:
            name (str): The name of the drink.

        """
        super().__init__(name, Drink.DEFAULT_DRINK_QUANTITY)
