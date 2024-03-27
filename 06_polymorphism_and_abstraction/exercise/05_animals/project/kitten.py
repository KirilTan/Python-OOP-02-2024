from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name=name,
                         age=age,
                         gender='Female')

    @staticmethod
    def make_sound() -> str:
        return 'Meow'

