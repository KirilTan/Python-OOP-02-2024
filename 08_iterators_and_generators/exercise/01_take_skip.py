class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        self.count -= 1
        if self.count >= 0:
            return self.current
        raise StopIteration()


# Test code
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print('---------------------------------------------------------------------------------------------------------------')

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
