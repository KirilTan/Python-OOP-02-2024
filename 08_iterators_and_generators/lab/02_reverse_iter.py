class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return reversed(self.iterable)


# Test code
reversed_list = reverse_iter([1, 2, 3, 4, 5, 6, 7])
for item in reversed_list:
    print(item)
