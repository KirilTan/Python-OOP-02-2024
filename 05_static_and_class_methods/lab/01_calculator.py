from functools import reduce


class Calculator:

    @staticmethod
    def add(*numbers) -> int or float:
        return sum(numbers)

    @staticmethod
    def multiply(*numbers) -> int or float:
        return reduce(lambda x, y: x * y, numbers)

    @staticmethod
    def subtract(*numbers) -> int or float:
        return reduce(lambda x, y: x - y, numbers)

    @staticmethod
    def divide(*numbers) -> int or float:
        return reduce(lambda x, y: x / y, numbers)


# Test code
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
