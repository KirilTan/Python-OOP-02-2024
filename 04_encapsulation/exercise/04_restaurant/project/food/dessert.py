from ex_1_and_2.project import Food


class Dessert(Food):

    def __init__(self, name: str, price: float, grams: float, calories: float):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

