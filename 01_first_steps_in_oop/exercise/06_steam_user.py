from typing import List


class SteamUser:
    """
    Represents a Steam user with a collection of games and tracking for played hours.

    Attributes:
        username (str): The Steam user's username.
        games (List[str]): A list of names of games owned by the user.
        played_hours (int): Total number of hours the user has played across all games.

    """

    def __init__(self, username: str, games: List[str]):
        """
        Initializes a new SteamUser instance.

        Parameters:
            username (str): The user's username.
            games (List[str]): Initial list of games owned by the user.

        """
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game_name: str, hours: int) -> str:
        """
        Records playing time for a game if it's in the user's library.

        Parameters:
            game_name (str): The name of the game being played.
            hours (int): The number of hours played.

        Returns:
            str: A message indicating whether the game was played or if it's not in the user's library.

        """
        if game_name not in self.games:
            return f"{game_name} is not in library"

        self.played_hours += hours
        return f"{self.username} is playing {game_name}"

    def buy_game(self, game_name: str) -> str:
        """
        Adds a new game to the user's library unless the game is already owned.

        Parameters:
            game_name (str): The name of the game to purchase.

        Returns:
            str: A message indicating the outcome of the purchase attempt.

        """
        if game_name in self.games:
            return f"{game_name} is already in your library"

        self.games.append(game_name)
        return f"{self.username} bought {game_name}"

    def status(self) -> str:
        """
        Provides a summary of the user's game library and total play time.

        Returns:
            str: A status message including the number of games owned and total play time.

        """
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


# Example usage
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())