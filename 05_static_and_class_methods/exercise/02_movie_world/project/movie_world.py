from typing import List

from ex_1_and_2.project import Customer
from ex_1_and_2.project import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        # Find Customer object
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
        except StopIteration:
            return f"Customer {customer_id} is not found."

        # Find DVD object
        try:
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return f"DVD {dvd_id} is not found."

        # Check if DVD is rented by this customer
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        # Check if DVD is rented by someone else
        if dvd.is_rented is True:
            return "DVD is already rented"

        # Check if age restrictions are met
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        # Rent the DVD
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        # Find Customer object
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
        except StopIteration:
            return f"Customer {customer_id} is not found."

        # Find DVD object
        try:
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return f"DVD {dvd_id} is not found."

        # Check if DVD is rented by this customer
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        # Return the DVD
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        """Returns a string representation of each customer and each DVD on a separate line"""
        text = "\n".join([
            *[str(c) for c in self.customers],
            *[str(d) for d in self.dvds],
        ])

        return text
