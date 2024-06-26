from ex_1_and_2.project import BasePeak


class ArcticPeak(BasePeak):

    def get_recommended_gear(self) -> list:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self) -> str:
        # Extreme difficulty - above 3000m
        if self.elevation > 3000:
            return "Extreme"

        # Advanced difficulty - between 2000m and 3000m, both inclusive
        elif 2000 <= self.elevation <= 3000:
            return "Advanced"
