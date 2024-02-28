class Vehicle:
    """
    A generic vehicle class with an initial mileage and a maximum speed.

    Args:
        mileage (int or float): The initial mileage of the vehicle.
        max_speed (int, optional): The maximum speed of the vehicle. Defaults to 150.

    Attributes:
        mileage (int or float): The current mileage of the vehicle.
        max_speed (int): The maximum speed of the vehicle.
        gadgets (list): A list of gadgets installed in the vehicle.
    """

    def __init__(self, mileage: int or float, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)