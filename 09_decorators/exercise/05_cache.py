def cache(function):
    def wrapper(number):
        if not wrapper.log.get(number):
            wrapper.log[number] = function(number)
        return wrapper.log[number]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)  # Expected result: {1: 1, 0: 0, 2: 1, 3: 2}

print('---')

fibonacci(4)
print(fibonacci.log)  # Expected result: {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
