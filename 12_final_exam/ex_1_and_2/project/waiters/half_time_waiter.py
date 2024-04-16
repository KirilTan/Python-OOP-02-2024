from ex_1_and_2.project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    WAGE = 12.0

    def calculate_earnings(self) -> float:
        wage = self.hours_worked * self.WAGE
        return wage

    def report_shift(self) -> str:
        information = f"{self.name} worked a half-time shift of {self.hours_worked} hours."
        return information
