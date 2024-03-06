class Product:
    """
    Base class for any food or drink.

    Parameters:
        name (str): The name of the product.
        quantity (int): The initial quantity of the product.

    Attributes:
        name (str): The name of the product.
        quantity (int): The current quantity of the product.

    """

    def __init__(self, name: str, quantity: int):
        """
        Initialize a new instance of the Product class.

        Args:
            name (str): The name of the product.
            quantity (int): The initial quantity of the product.

        """
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int) -> None:
        """
        Decrease the quantity of the product.

        Args:
            quantity (int): The amount to decrease the quantity by.

        Returns:
            None
        """
        if quantity <= self.quantity:
            self.quantity -= quantity

    def increase(self, quantity: int) -> None:
        """
        Increase the quantity of the product.

        Args:
            quantity (int): The amount to increase the quantity by.

        Returns:
            None
        """
        self.quantity += quantity

    def __repr__(self) -> str:
        """
        Return a string representation of the product.

        Returns:
            str: The name of the product.

        """
        return self.name
