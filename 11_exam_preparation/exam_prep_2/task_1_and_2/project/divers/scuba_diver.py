from ex_1_and_2.project import BaseDiver


class ScubaDiver(BaseDiver):
    STARTING_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.STARTING_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        oxygen_to_reduce = round(time_to_catch * 0.3)

        if (self.oxygen_level - oxygen_to_reduce) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= oxygen_to_reduce

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.STARTING_OXYGEN_LEVEL

