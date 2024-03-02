from project.guild import Guild


class Player:
    """
    This class represents a player in the game. It contains their name, health, mana, skills, and guild.
    """

    def __init__(self, name: str, hp: int, mp: int):
        """
        Initialize a new player with the given name, health, and mana.

        Args:
            name (str): The name of the player
            hp (int): The starting health of the player
            mp (int): The starting mana of the player
        """
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}  # Contains the skills of each player and its mana cost
        self.guild: str = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        """
        Adds the skill and the corresponding mana cost to the dictionary of skills.

        Args:
            skill_name (str): The name of the skill
            mana_cost (int): The mana cost of the skill

        Returns:
            str: A message indicating whether the skill was added or not
        """
        if skill_name in self.skills:
            return 'Skill already added'

        self.skills[skill_name] = mana_cost
        text = f'Skill {skill_name} added to the collection of the player {self.name}'
        return text

    def player_info(self) -> str:
        """
        Returns the player's information, including their skills.

        Returns:
            str: The player's information.
        """
        text = f'Name: {self.name}\n'
        text += f'Guild: {self.guild}\n'
        text += f'HP: {self.hp}\n'
        text += f'MP: {self.mp}\n'
        for skill_name, mana_cost in self.skills.items():
            text += f'==={skill_name} - {mana_cost}\n'
        return text
