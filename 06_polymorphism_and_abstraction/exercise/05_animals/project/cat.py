from ex_1_and_2.project import Animal


class Cat(Animal):
    @staticmethod
    def make_sound() -> str:
        return 'Meow meow!'
