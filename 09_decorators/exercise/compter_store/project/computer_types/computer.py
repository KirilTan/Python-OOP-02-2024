from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    PRICE_PER_RAM_BLOCK: int = 100

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    def power_of_two(number: int) -> bool:
        result = log2(number)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int) -> str:
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if ram > self.max_ram or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def set_parts(self, processor: str, ram: int) -> None:
        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[self.processor]
        self.price += int(log2(ram)) * Computer.PRICE_PER_RAM_BLOCK

    def __repr__(self):
        text = f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
        return text
