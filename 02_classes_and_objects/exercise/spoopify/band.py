from typing import List
from album import Album
from song import Song


class Band:
    """
    A class that represents a band.

    Attributes:
        name (str): The name of the band.
        albums (List[Album]): A list of albums by the band.
    """

    def __init__(self, name: str):
        """
        Initializes a new Band instance.

        Args:
            name (str): The name of the band.
        """
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album) -> str:
        """
        Adds an album to the collection and returns a message indicating if the operation was successful.

        Args:
            album (Album): The album to be added.

        Returns:
            str: A message indicating whether the album was added or not.
        """
        # Album is already added
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        # Add the album to the collection
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        """
        Removes the album from the collection and returns a message indicating if the operation was successful.

        Args:
            album_name (str): The name of the album to be removed.

        Returns:
            str: A message indicating whether the album was removed or not.
        """
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self) -> str:
        """
        Returns a detailed string representation of the band.

        Returns:
            str: A detailed string representation of the band.
        """
        albums_details = '\n'.join(a.details() for a in self.albums)
        return f"Band {self.name}\n" \
               f"{albums_details}"


# Test Code
song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
