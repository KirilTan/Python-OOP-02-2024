from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass

    @abstractmethod
    def get_species(self) -> str:
        return self.__class__.__name__


class Cat(Animal):
    def get_species(self) -> str:
        pass

    def make_sound(self) -> None:
        print('meow')


class Dog(Animal):
    def get_species(self) -> str:
        pass

    def make_sound(self) -> None:
        print('woof-woof')


def animal_sound(animals: list[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


# Test code
animals = [Cat(), Dog()]
animal_sound(animals)
