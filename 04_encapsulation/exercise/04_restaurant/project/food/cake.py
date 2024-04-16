from ex_1_and_2.project import Dessert


class Cake(Dessert):

    GRAMS = 250
    CALORIES = 1_000
    PRICE = 5

    def __init__(self, name: str):
        super().__init__(name, price=Cake.PRICE, grams=Cake.GRAMS, calories=Cake.CALORIES)
