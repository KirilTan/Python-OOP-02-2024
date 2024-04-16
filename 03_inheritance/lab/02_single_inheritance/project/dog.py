from ex_1_and_2.project import Animal

class Dog(Animal):
    """
    Represents a Dog, which is a specific kind of Animal.

    Inherits from Animal class to model dog-specific behavior.

    Methods:
        bark(): Simulates the dog barking, returning a string to indicate the action.
    """

    def bark(self):
        """
        Simulates barking action for the dog.

        Returns:
            str: A string indicating that the dog is barking.
        """
        return 'barking...'
