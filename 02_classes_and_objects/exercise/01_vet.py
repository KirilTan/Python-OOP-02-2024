from typing import List


class Vet:
    """
    A class to represent a veterinarian clinic.

    Attributes:
        animals (list): A list of animals that have been registered with the clinic.
        space (int): The number of available spaces in the clinic.

    Methods:
        __init__(self, name: str): Initializes the veterinarian with a name.
        register_animal(self, animal_name: str): Adds an animal to the clinic if there is space.
        unregister_animal(self, animal_name: str): Removes an animal from the clinic if it is registered.
        info(self): Returns a string with information about the veterinarian and the animals in the clinic.
    """

    animals = []
    space = 5

    def __init__(self, name: str):
        """
        Initializes the veterinarian with a name.

        Args:
            name (str): The name of the veterinarian.
        """
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        """
        Adds an animal to the clinic if there is space.

        Args:
            animal_name (str): The name of the animal to be registered.

        Returns:
            str: A message indicating whether the animal was registered or not.
        """
        if Vet.space > 0:  # Enough space
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        else:              # Not enough space
            return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        """
        Removes an animal from the clinic if it is registered.

        Args:
            animal_name (str): The name of the animal to be unregistered.

        Returns:
            str: A message indicating whether the animal was unregistered or not.
        """
        if animal_name in Vet.animals:  # Animal is registered
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        else:                           # Animal is not registered
            return f"{animal_name} not in the clinic"

    def info(self) -> str:
        """
        Returns a string with information about the veterinarian and the animals in the clinic.

        Returns:
            str: A message with information about the veterinarian and the animals in the clinic.
        """
        animals_doctor = len(self.animals)
        text = (
            f"{self.name} has {animals_doctor} animals. "
            f"{Vet.space} space left in clinic"
        )
        return text


# Example usage
peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
