from typing import List


class Shop:
    """
    This class represents a shop that sells items.

    Args:
        name (str): The name of the shop.
        items (list): A list of items that the shop sells.

    Attributes:
        name (str): The name of the shop.
        items (list): A list of items that the shop sells.
    """

    def __init__(self, name: str, items: List[str]):
        self.name = name
        self.items = items

    def get_items_count(self) -> int:
        """
        This function returns the number of items in the shop.

        Returns:
            int: The number of items in the shop.
        """
        number_of_items = len(self.items)
        return number_of_items


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
