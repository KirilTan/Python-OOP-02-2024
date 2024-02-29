class PizzaDelivery:
    """
    A class for creating and managing pizza orders.

    Attributes:
        ordered (bool): A flag indicating whether the pizza has been ordered or not.
        name (str): The name of the pizza.
        price (float): The price of the pizza.
        ingredients (dict): A dictionary of ingredients and their quantities.
    """

    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        """
        Initialize a new pizza order.

        Args:
            name (str): The name of the pizza.
            price (float): The price of the pizza.
            ingredients (dict): A dictionary of ingredients and their quantities.
        """
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> None or str:
        """
        Add an extra ingredient to the pizza.

        Args:
            ingredient (str): The name of the ingredient.
            quantity (int): The quantity of the ingredient to add.
            price_per_quantity (float): The price of the ingredient per unit.

        Returns:
            None or str: None if the operation was successful, or a string with an error message if not.
        """
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity

        elif ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str or None:
        """
        Remove an ingredient from the pizza.

        Args:
            ingredient (str): The name of the ingredient.
            quantity (int): The quantity of the ingredient to remove.
            price_per_quantity (float): The price of the ingredient per unit.

        Returns:
            str or None: A string with an error message if the operation was not successful, or None if it was.
        """
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients.keys():
            return (f"Wrong ingredient selected! "
                    f"We do not use {ingredient} in {self.name}!")

        else:  # ingredient in self.ingredients.keys():
            if self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"

            else:
                self.ingredients[ingredient] -= quantity
                self.price -= price_per_quantity * quantity

    def make_order(self) -> str:
        """
        Make the pizza order and return a confirmation message.

        Returns:
            str: A message confirming that the order has been made.
        """
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        PizzaDelivery.ordered = True

        ingredient_quantity = ', '.join(
            f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items())

        text = (f"You've ordered pizza {self.name} prepared with {ingredient_quantity} "
                f"and the price will be {self.price}lv.")

        return text


# Example usage
margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
