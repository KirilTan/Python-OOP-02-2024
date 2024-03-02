class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}  # Contains the skills of each player and its mana cost
        self.guild: str = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        """
        Adds the skill and the corresponding mana cost to the dictionary of skills

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

    def player_info(self):
        pass
