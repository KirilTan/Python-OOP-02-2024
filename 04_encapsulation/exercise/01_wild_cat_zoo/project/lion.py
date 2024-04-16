from ex_1_and_2.project import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, 50)