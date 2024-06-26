from ex_1_and_2.project import HotBeverage


class Coffee(HotBeverage):

    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, price=Coffee.PRICE, milliliters=Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
