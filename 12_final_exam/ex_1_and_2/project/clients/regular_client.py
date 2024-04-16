from ex_1_and_2.project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    MEMBERSHIP_TYPE = 'Regular'

    def __init__(self, name: str):
        super().__init__(name, RegularClient.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float) -> int:
        earned_points = int(order_amount // 10)
        self.points += earned_points

        return earned_points
