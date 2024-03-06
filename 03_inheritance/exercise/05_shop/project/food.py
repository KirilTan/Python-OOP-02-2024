from project.product import Product


class Food(Product):
    """
    A basic food item that can be sold.

    Parameters:
        name (str): The name of the food item.
        quantity (int): The quantity of the food item.

    Attributes:
        DEFAULT_FOOD_QUANTITY (int): The default quantity of food items.

    """

    DEFAULT_FOOD_QUANTITY: int = 15

    def __init__(self, name: str, quantity: int = DEFAULT_FOOD_QUANTITY):
        """
        Initialize a new Food instance.

        Args:
            name (str): The name of the food item.
            quantity (int, optional): The quantity of the food item. Defaults to DEFAULT_FOOD_QUANTITY.

        """
        super().__init__(name, quantity)
