from ex_1_and_2.project import Cat


class Tomcat(Cat):

    def __init__(self, name: str, age: int):
        super().__init__(name=name,
                         age=age,
                         gender='Male')

    @staticmethod
    def make_sound() -> str:
        return 'Hiss'
