from abc import ABC, abstractmethod

from math import pi


class Shape(ABC):
    @staticmethod
    @abstractmethod
    def calculate_area():
        pass

    @staticmethod
    @abstractmethod
    def calculate_perimeter():
        pass


class Circle(Shape):

    def __init__(self, radius: int or float):
        self.__radius = radius

    def calculate_area(self) -> float:
        return self.__radius * self.__radius * pi

    def calculate_perimeter(self) -> float:
        return 2 * self.__radius * pi


class Rectangle(Shape):

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def calculate_area(self) -> int:
        return self.__width * self.__height

    def calculate_perimeter(self) -> int:
        return 2 * (self.__width + self.__height)


# Test code
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
