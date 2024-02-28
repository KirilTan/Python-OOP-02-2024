class Glass:
    """
    A glass object with a defined capacity.

    Attributes:
        capacity (int): The maximum capacity of the glass, in milliliters (ml).
        content (int): The current volume of liquid in the glass, in milliliters (ml).

    Methods:
        fill(ml: int) -> str: Adds the specified amount of liquid to the glass.
            Returns a message indicating whether the addition was successful or not.
        empty() -> None: Empties the glass.
        info() -> str: Returns a message indicating the current volume of liquid in the glass,
            as well as the remaining capacity.

    """

    capacity = 250  # capacity is in ml

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        """
        Adds the specified amount of liquid to the glass.

        Args:
            ml (int): The amount of liquid to add, in milliliters (ml).

        Returns:
            str: A message indicating whether the addition was successful or not.

        """
        new_content = self.content + ml

        if new_content <= Glass.capacity:
            self.content = new_content
            return f"Glass filled with {ml} ml"  # Successful addition
        else:
            return f"Cannot add {ml} ml"         # Unsuccessful addition

    def empty(self) -> str:
        """
        Empties the glass.

        Returns:
            str: A message indicating that the glass is now empty.

        """
        self.content = 0
        return 'Glass is now empty'

    def info(self) -> str:
        """
        Returns a message indicating the current volume of liquid in the glass,
        as well as the remaining capacity.

        Returns:
            str: A message indicating the current volume and remaining capacity.

        """
        space_left = Glass.capacity - self.content
        text = f"{space_left} ml left"
        return text


# Example usage
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
