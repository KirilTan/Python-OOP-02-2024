from typing import Tuple, List
from song import Song


class Album:
    """
    A class that represents an album.

    An album contains a list of songs and metadata about the album such as its name and whether it has been published or not.
    """

    def __init__(self, name: str, *songs: Tuple[Song]):
        """
        Initializes an album with the given name and songs.

        Args:
            name (str): The name of the album.
            songs (Tuple[Song]): The songs that are included in the album.
        """
        self.name = name
        self.songs: List[Song] = [*songs]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        """
        Adds the given song to the album.

        Args:
            song (Song): The song to be added.

        Returns:
            str: A message indicating whether the song was added or not.
        """
        # Song is a single
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        # Album is already published
        if self.published:
            return "Cannot add songs. Album is published."

        # Song is already added to the album
        if song in self.songs:
            return "Song is already in the album."

        # Song added to the album
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        """
        Removes the given song from the album.

        Args:
            song_name (str): The name of the song to be removed.

        Returns:
            str: A message indicating whether the song was removed or not.
        """
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        # Album is already published
        if self.published:
            return "Cannot remove songs. Album is published."

        # Song removed from the album
        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self) -> str:
        """
        Publishes the album.

        Returns:
            str: A message indicating whether the album was published or not.
        """
        # Album is already published
        if self.published:
            return f"Album {self.name} is already published."

        # Album published
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        """
        Returns information about the album, including the list of songs.

        Returns:
            str: The information about the album.
        """
        songs_details = '\n'.join(f'== {s.get_info()}' for s in self.songs)
        return f"Album {self.name}\n" \
               f"{songs_details}"
