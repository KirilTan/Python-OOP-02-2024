class Cup:
    """
    Represents a cup with a specific size and current quantity of liquid.

    Attributes:
        size (int): The total capacity of the cup.
        quantity (int): The current quantity of liquid in the cup.

    Methods:
        fill: Adds a specified quantity of liquid to the cup.
        status: Returns the amount of free space left in the cup.

    """

    def __init__(self, size: int, quantity: int):
        """
        Initializes a new Cup instance with a given size and initial quantity of liquid.

        Parameters:
            size (int): The total capacity of the cup.
            quantity (int): The initial quantity of liquid in the cup.
        """
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int):
        """
        Adds a specified quantity of liquid to the cup. If the new quantity exceeds the cup's size,
        the cup is not filled beyond its capacity.

        Parameters:
            quantity (int): The quantity of liquid to add to the cup.

        """
        new_quantity = self.quantity + quantity
        if new_quantity <= self.size:
            self.quantity = new_quantity

    def status(self) -> int:
        """
        Calculates and returns the amount of free space left in the cup.

        Returns:
            int: The amount of free space left in the cup.

        """
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
