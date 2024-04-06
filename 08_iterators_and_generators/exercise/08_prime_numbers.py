from math import isqrt


def get_primes(numbers: list[int]):
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                break

        else:
            yield number


# Test code
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print('--------------------------------------------------------------------------------------------------')
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
