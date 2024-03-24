from __future__ import annotations


class Integer:
    ROMAN_NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1_000}

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float) -> Integer or str:
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, value: str) -> Integer:
        int_sum = 0

        for i in range(len(value)):
            if i != 0 and cls.ROMAN_NUMERALS[value[i]] > cls.ROMAN_NUMERALS[value[i - 1]]:
                int_sum += cls.ROMAN_NUMERALS[value[i]] - 2 * cls.ROMAN_NUMERALS[value[i - 1]]
            else:
                int_sum += cls.ROMAN_NUMERALS[value[i]]

        return cls(int_sum)

    @classmethod
    def from_string(cls, value: str) -> Integer or str:
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


# Test code
first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
