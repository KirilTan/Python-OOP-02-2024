from project.computer_types.computer import Computer


class Laptop(Computer):
    TYPE: str = 'laptop'
    MAX_RAM: int = 64
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }

    @property
    def type(self) -> str:
        return Laptop.TYPE

    @property
    def available_processors(self):
        return Laptop.AVAILABLE_PROCESSORS

    @property
    def max_ram(self) -> int:
        return Laptop.MAX_RAM
