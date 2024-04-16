from abc import ABC, abstractmethod
from typing import Type

from ex_1_and_2.project import Food, Meat, Vegetable, Fruit, Seed


class Animal(ABC):

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten: int or float = 0

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        ...

    @property
    @abstractmethod
    def gained_weight(self) -> float:
        ...

    @property
    @abstractmethod
    def eatable_food(self) -> list[Type[Meat | Vegetable | Fruit | Seed]]:
        ...

    def feed(self, food: Food) -> str or None:
        if type(food) in self.eatable_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.gained_weight * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name=name, weight=weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name=name, weight=weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
