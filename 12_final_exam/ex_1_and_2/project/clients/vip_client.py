from ex_1_and_2.project.clients.base_client import BaseClient


class VIPClient(BaseClient):
    MEMBERSHIP_TYPE = 'VIP'

    def __init__(self, name: str):
        super().__init__(name, VIPClient.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float) -> int:
        earned_points = int(order_amount // 5)
        self.points += earned_points

        return earned_points
