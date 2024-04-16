from ex_1_and_2.project import MainDish


class Salmon(MainDish):

    GRAMS = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, grams=Salmon.GRAMS)
