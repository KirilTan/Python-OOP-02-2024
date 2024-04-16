from typing import List

from ex_1_and_2.project import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        # Player already in the team
        if player in self.__players:
            return f"Player {player.name} has already joined"
        # Add player to the team
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str or Player:
        try:
            player = next((p for p in self.__players if p.name == player_name),)
            self.__players.remove(player)
            return player
        except StopIteration:
            return f"Player {player_name} not found"
