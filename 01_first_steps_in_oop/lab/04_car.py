class Car:
    """
    A simple car class with name, model, and engine attributes.

    Args:
        name (str): The name of the car.
        model (str): The model of the car.
        engine (str): The engine type of the car.

    Attributes:
        name (str): The name of the car.
        model (str): The model of the car.
        engine (str): The engine type of the car.

    """

    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self) -> str:
        """
        Returns a string with information about the car.

        Returns:
            str: A string with information about the car.

        """
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())
