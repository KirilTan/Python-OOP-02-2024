from abc import ABC, abstractmethod


class Vehicle(ABC):  # Abstract Base Class

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        ...

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    ADDITIONAL_CONSUMPTION: float = 0.9

    def drive(self, distance: float) -> None:
        consumption = (self.ADDITIONAL_CONSUMPTION + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ADDITIONAL_CONSUMPTION: float = 1.6
    CAPACITY: float = 0.95

    def drive(self, distance: float) -> None:
        consumption = (self.ADDITIONAL_CONSUMPTION + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.CAPACITY


# Test code
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
