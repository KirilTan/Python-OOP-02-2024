from typing import List
from to_do_list import Pokemon


class Trainer:
    """
    This class represents a Pokemon Trainer.

    Args:
        name (str): The name of the Trainer.

    Attributes:
        name (str): The name of the Trainer.
        pokemons (List[Pokemon]): A list of Pokemon that the Trainer has caught.
    """

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        """
        Adds a Pokemon to the Trainer's collection.

        Args:
            pokemon (Pokemon): The Pokemon to be added.

        Returns:
            str: A message indicating whether the Pokemon was added or not.
        """
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        """
        Releases a Pokemon from the Trainer's collection.

        Args:
            pokemon_name (str): The name of the Pokemon to be released.

        Returns:
            str: A message indicating whether the Pokemon was released or not.
        """
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        """
        Returns a string containing information about the Trainer and their Pokemon.

        Returns:
            str: A message containing information about the Trainer and their Pokemon.
        """
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)

        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemons)}\n" \
               f"{pokemons_data}"


# Example Usage
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
