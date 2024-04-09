from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    TYPE: str = 'desktop computer'
    MAX_RAM: int = 128
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }

    @property
    def type(self) -> str:
        return DesktopComputer.TYPE

    @property
    def available_processors(self):
        return DesktopComputer.AVAILABLE_PROCESSORS

    @property
    def max_ram(self) -> int:
        return DesktopComputer.MAX_RAM
