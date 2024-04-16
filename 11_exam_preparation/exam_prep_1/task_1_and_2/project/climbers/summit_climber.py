from ex_1_and_2.project import BaseClimber
from ex_1_and_2.project import BasePeak


class SummitClimber(BaseClimber):
    MIN_STRENGTH_NEEDED: float = 75
    INITIAL_STRENGTH: float = 150

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= SummitClimber.MIN_STRENGTH_NEEDED

    def climb(self, peak: BasePeak) -> None:
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)
