class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number -1:
            raise StopIteration

        self.index += 1

        return self.sequence[self.index % len(self.sequence)]


# Test code
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print('\n-------------------------------------------------------------------------------------------------------------')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
