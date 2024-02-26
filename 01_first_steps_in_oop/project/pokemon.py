class Pokemon:
    """
    This class represents a pokemon in the game.

    Args:
        name (str): The name of the pokemon.
        health (int): The health of the pokemon.

    Attributes:
        name (str): The name of the pokemon.
        health (int): The health of the pokemon.

    """

    def __init__(self, name: str, health: int):
        """
        Initialize the pokemon with the given name and health.

        Args:
            name (str): The name of the pokemon.
            health (int): The health of the pokemon.

        """
        self.name = name
        self.health = health

    def pokemon_details(self) -> str:
        """
        Returns a string representation of the pokemon with its health.

        Returns:
            str: The pokemon details.

        """
        return f"{self.name} with health {self.health}"
