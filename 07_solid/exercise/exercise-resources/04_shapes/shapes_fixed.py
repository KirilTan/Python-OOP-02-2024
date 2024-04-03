from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> int or float:
        ...


class Rectangle(Shape):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def calculate_area(self) -> int or float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def calculate_area(self) -> int or float:
        return (self.base * self.height) / 2


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise ValueError("`shapes` should be of type `list`.")
        self.__shapes = value

    @property
    def total_area(self) -> int or float:
        total = 0

        for shape in self.shapes:
            total += shape.calculate_area()

        return total


# Test code
shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

print('-----------------------------------------------------------------')

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
