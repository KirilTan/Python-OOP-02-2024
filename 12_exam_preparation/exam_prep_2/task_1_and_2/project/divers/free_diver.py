from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    STARTING_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.STARTING_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        oxygen_to_reduce = round(time_to_catch * 0.6)

        if (self.oxygen_level - oxygen_to_reduce) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= oxygen_to_reduce

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.STARTING_OXYGEN_LEVEL
