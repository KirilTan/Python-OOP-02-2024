from abc import ABC, abstractmethod
from ex_1_and_2.project import BasePeak


class BaseClimber(ABC):
    RECOVER_STRENGTH_FROM_REST = 15

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list = []
        self.is_prepared: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")

        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")

        self.__strength = value

    @abstractmethod
    def can_climb(self) -> bool:
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += BaseClimber.RECOVER_STRENGTH_FROM_REST

    def __str__(self):
        return (f"{self.__class__.__name__}: "
                f"/// Climber name: {self.name} * "
                f"Left strength: {float(self.strength)} * "
                f"Conquered peaks: {', '.join(sorted(self.conquered_peaks))} ///")
