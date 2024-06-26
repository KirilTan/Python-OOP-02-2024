from typing import Dict

from ex_1_and_2.project import Dough
from ex_1_and_2.project import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[Topping] = {}  # Topping type: topping weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value: Dough):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> str or None:
        """Add a new topping to the dictionary"""
        # No space left
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        # Topping already in the dictionary
        elif topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight  # Increase the value of its weight

        # New topping
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        toppings_weight = sum(self.toppings.values())
        pizza_wight = self.dough.weight + toppings_weight
        return pizza_wight
