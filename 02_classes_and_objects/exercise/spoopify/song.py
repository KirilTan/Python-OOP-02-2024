class Song:
    """
    A Song represents a musical piece with a name, length, and whether it is a single or not.

    Args:
        name (str): The name of the song.
        length (float): The length of the song in seconds.
        single (bool): Whether the song is a single or not.

    Attributes:
        name (str): The name of the song.
        length (float): The length of the song in seconds.
        single (bool): Whether the song is a single or not.
    """

    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self) -> str:
        """
        Returns a string containing the name and length of the song.

        Returns:
            str: The name and length of the song.
        """
        text = f'{self.name} - {self.length}'
        return text
