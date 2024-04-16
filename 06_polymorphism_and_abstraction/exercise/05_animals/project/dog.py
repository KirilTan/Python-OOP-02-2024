from ex_1_and_2.project import Animal


class Dog(Animal):
    @staticmethod
    def make_sound() -> str:
        return 'Woof!'
