from project.player import Player
from typing import List


class Guild:
    """
    A class representing a Guild in a game.

    Attributes:
        name (str): The name of the guild.
        players (List[Player]): A list of players in the guild.
    """

    def __init__(self, name: str):
        """
        Initializes a new Guild.

        Args:
            name (str): The name of the guild.
        """
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        """
        Adds a player to the guild.

        Args:
            player (Player): The player to be added to the guild.

        Returns:
            str: A message indicating whether the player was added or not.
        """
        # Not in any guild
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        # Already in the guild
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        # In a different guild
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        """
        Removes a player from the guild.

        Args:
            player_name (str): The name of the player to be removed from the guild.

        Returns:
            str: A message indicating whether the player was removed from the guild or not.
        """
        for player in self.players:

            if player.name == player_name:
                player.guild = 'Unaffiliated'
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        """
        Returns information about the guild, including the list of players in the guild.

        Returns:
            str: The information about the guild.
        """
        text = f"Guild: {self.name}"
        for current_player in self.players:
            current_player_info = current_player.player_info()
            text += f"\n{current_player_info}"
        return text

