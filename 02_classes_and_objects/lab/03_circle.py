class Circle:
    """
    This class represents a circle.

    Attributes:
        radius (int or float): The radius of the circle.
        pi (float): The mathematical constant pi.

    Methods:
        __init__(self, radius: int or float): Initializes a new instance of the Circle class.
        set_radius(self, new_radius: int or float) -> None: Sets the radius of the circle.
        get_area(self) -> int or float: Returns the area of the circle.
        get_circumference(self) -> int or float: Returns the circumference of the circle.

    """

    pi = 3.14

    def __init__(self, radius: int or float):
        """
        Initializes a new instance of the Circle class.

        Args:
            radius (int or float): The radius of the circle.

        """
        self.radius = radius

    def set_radius(self, new_radius: int or float) -> None:
        """
        Sets the radius of the circle.

        Args:
            new_radius (int or float): The new radius of the circle.

        """
        self.radius = new_radius

    def get_area(self) -> int or float:
        """
        Returns the area of the circle.

        Returns:
            int or float: The area of the circle.

        """
        area = self.radius * self.radius * Circle.pi
        return area

    def get_circumference(self) -> int or float:
        """
        Returns the circumference of the circle.

        Returns:
            int or float: The circumference of the circle.

        """
        circumference = 2 * self.radius * Circle.pi
        return circumference


# Example usage
circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
