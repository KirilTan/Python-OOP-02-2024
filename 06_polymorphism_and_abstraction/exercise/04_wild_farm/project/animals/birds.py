from typing import List, Type

from project.animals.animals import Bird

from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def eatable_food(self) -> list[Type[Meat]]:
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def eatable_food(self) -> list[Type[Meat | Vegetable | Fruit | Seed]]:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
