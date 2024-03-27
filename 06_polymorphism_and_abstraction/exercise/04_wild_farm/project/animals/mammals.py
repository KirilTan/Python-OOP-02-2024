from typing import Type

from project.animals.animals import Mammal

from project.food import Food, Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    @property
    def eatable_food(self) -> list[Type[Meat | Vegetable | Fruit | Seed]]:
        return [Fruit, Vegetable]

    @property
    def gained_weight(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return 'Squeak'


class Dog(Mammal):
    @property
    def eatable_food(self) -> list[Type[Meat | Vegetable | Fruit | Seed]]:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return 'Woof!'


class Cat(Mammal):
    @property
    def eatable_food(self) -> list[Type[Meat | Vegetable | Fruit | Seed]]:
        return [Meat, Vegetable]

    @property
    def gained_weight(self) -> float:
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return 'Meow'


class Tiger(Mammal):
    @property
    def eatable_food(self) -> list[Type[Meat | Vegetable | Fruit | Seed]]:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return 'ROAR!!!'
