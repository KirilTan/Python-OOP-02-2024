class Point:
    """
    A class to represent a point in a plane.

    Args:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.

    Methods:
        set_x(new_x: int) -> None: Sets the x-coordinate of the point.
        set_y(new_y: int) -> None: Sets the y-coordinate of the point.
        __str__() -> str: Returns a string representation of the point.

    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int) -> None:
        """
        Sets the x-coordinate of the point.

        Args:
            new_x (int): The new x-coordinate of the point.

        """
        self.x = new_x

    def set_y(self, new_y: int) -> None:
        """
        Sets the y-coordinate of the point.

        Args:
            new_y (int): The new y-coordinate of the point.

        """
        self.y = new_y

    def __str__(self) -> str:
        """
        Returns a string representation of the point.

        Returns:
            str: A string representation of the point in the form "(x, y)".

        """
        text = f"The point has coordinates ({self.x},{self.y})"
        return text


# Example usage
p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
