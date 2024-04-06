from itertools import permutations


def possible_permutations(elements: list[int]):
    for el in permutations(elements):
        yield list(el)


# Test code
[print(n) for n in possible_permutations([1, 2, 3])]
print('--------------------------------------------------------------------------------------------------')
[print(n) for n in possible_permutations([1])]
