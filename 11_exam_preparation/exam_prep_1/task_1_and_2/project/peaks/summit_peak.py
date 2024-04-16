from ex_1_and_2.project import BasePeak


class SummitPeak(BasePeak):
    def get_recommended_gear(self) -> list:
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self) -> str:
        # Extreme difficulty - above 2500m
        if self.elevation > 2500:
            return "Extreme"

        # Advanced difficulty - between 1500m and 2500m, both inclusive
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"
