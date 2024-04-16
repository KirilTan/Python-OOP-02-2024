from ex_1_and_2.project.clients.regular_client import RegularClient
from ex_1_and_2.project.clients.vip_client import VIPClient

from ex_1_and_2.project.waiters.full_time_waiter import FullTimeWaiter
from ex_1_and_2.project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITER_TYPES = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }

    VALID_CLIENT_TYPES = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient
    }

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        try:
            waiter = self.VALID_WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        except KeyError:
            return f"{waiter_type} is not a recognized waiter type."

        try:
            next(filter(lambda w: w.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."
        except StopIteration:
            self.waiters.append(waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        try:
            client = self.VALID_CLIENT_TYPES[client_type](client_name)
        except KeyError:
            return f"{client_type} is not a recognized client type."

        try:
            next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} is already a client."
        except StopIteration:
            self.clients.append(client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
        except StopIteration:
            return f"{client_name} is not a registered client."

        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        total_earnings = f"{sum(waiter.calculate_earnings() for waiter in self.waiters):.2f}"
        total_client_points = int(sum(client.points for client in self.clients))
        total_client_count = len(self.clients)

        text = "$$ Monthly Report $$"
        text += f"\nTotal Earnings: ${total_earnings}"
        text += f"\nTotal Clients Unused Points: {total_client_points}"
        text += f"\nTotal Clients Count: {total_client_count}"
        text += f"\n** Waiter Details **"

        for waiter in sorted(self.waiters, key=lambda w: (-w.calculate_earnings())):
            text += f"\n{str(waiter)}"

        return text
