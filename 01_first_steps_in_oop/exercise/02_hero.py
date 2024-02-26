class Hero:
    """
    This class represents a hero in the game.

    Args:
        name (str): The name of the hero.
        health (int or float): The health of the hero.

    Attributes:
        name (str): The name of the hero.
        health (int or float): The health of the hero.

    """

    def __init__(self, name: str, health: int or float):
        """
        Initialize the hero with the given name and health.

        Args:
            name (str): The name of the hero.
            health (int or float): The health of the hero.

        """
        self.name = name
        self.health = health

    def defend(self, damage: int or float) -> str or None:
        """
        Reduce the hero's health by the given damage.

        Args:
            damage (int or float): The amount of damage to reduce the hero's health by.

        Returns:
            str: A message if the hero was defeated.
            None: If the hero was not defeated.

        """
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            output_text = f"{self.name} was defeated"
            return output_text

    def heal(self, amount: int or float) -> None:
        """
        Increase the hero's health by the given amount.

        Args:
            amount (int or float): The amount of health to increase the hero's health by.

        Returns:
            None

        """
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
