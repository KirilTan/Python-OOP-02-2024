class Flower:
    """
    Represents a flower with a name, water requirements, and its happiness state based on watering.

    Attributes:
        name (str): The name of the flower.
        water_requirements (int|float): The minimum amount of water (in units) required to make the flower happy.
        is_happy (bool): The state of the flower's happiness, True if happy, False otherwise.

    Methods:
        water: Water the flower with a specified amount and update its happiness state.
        status: Return a string indicating whether the flower is happy or not.
    """

    def __init__(self, name: str, water_requirements: int or float):
        """
        Initializes a new Flower instance with a given name and water requirements.

        Parameters:
            name (str): The name of the flower.
            water_requirements (int|float): The minimum amount of water (in units) required to make the flower happy.
        """
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int or float) -> None:
        """
        Water the flower with a specified amount. If the quantity is equal to or greater than the flower's
        water requirements, the flower becomes happy. Otherwise, the flower is not happy.

        Parameters:
            quantity (int|float): The amount of water to give to the flower.
        """
        self.is_happy = quantity >= self.water_requirements

    def status(self) -> str:
        """
        Returns the flower's happiness status in a string format.

        Returns:
            str: A message indicating whether the flower is happy or not.
        """
        return f'{self.name} is {"happy" if self.is_happy else "not happy"}'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())