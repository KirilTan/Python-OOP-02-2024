from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """
        If the name is an empty string or contains only white spaces,
        raise a ValueError with the message: "Fish name should be determined!"
        """
        if not value.strip():
            raise ValueError("Fish name should be determined!")

        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        """
        Must be a value between 1 and 10, both inclusive.
        If not, raise a ValueError with the message: "Points should be a value ranging from 1 to 10!"
        """
        if value < 1 or value > 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")

        self.__points = value

    @abstractmethod
    def fish_details(self) -> str:
        ...
