class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.numbers = [num for num in range(0, count + 1)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers:
            return self.numbers.pop()
        raise StopIteration()


# Test code
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print('\n-------------------------------------------------------------------------------------------------------------')
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
