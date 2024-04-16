from typing import List

from ex_1_and_2.project import Drink
from ex_1_and_2.project import Food


class ProductRepository:
    """
    This class is responsible for managing the products in the system.

    """

    def __init__(self):
        self.products: List[Food, Drink] = []

    def add(self, product: Food or Drink) -> None:
        """
        Adds a product to the repository.

        Args:
            product (Food or Drink): The product to be added.

        Returns:
            None

        """
        self.products.append(product)

    def find(self, product_name: str) -> Food or Drink:
        """
        Returns a product(object) with that name

        Args:
            product_name (str): The name of the product

        Returns:
            Food or Drink: The product object with that name

        """
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        """
        Removes a product from the repository.

        Args:
            product_name (str): The name of the product to be removed.

        Returns:
            None

        """
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        return '\n'.join(f"{p.name}: {p.quantity}" for p in self.products)
