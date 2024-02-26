class Music:
    """
    This class represents a music object with a title, an artist, and lyrics.

    """

    def __init__(self, title: str, artist: str, lyrics: str):
        """
        Initialize a new Music object.

        Args:
            title (str): The title of the music.
            artist (str): The artist of the music.
            lyrics (str): The lyrics of the music.

        """
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self) -> str:
        """
        Returns information about the music.

        Returns:
            str: The information about the music.

        """
        text = f'This is "{self.title}" from "{self.artist}"'
        return text

    def play(self):
        """
        Shows the lyrics of the music.

        Returns:
            str: The lyrics of the music.
        """
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
