def even_parameters(function):
    def wrapper(*args, **kwargs):
        for arg in args:
            try:
                if arg % 2 != 0:
                    return 'Please use only even numbers!'
            except TypeError:
                return 'Please use only even numbers!'

        for k, v in kwargs:
            try:
                if v % 2 != 0:
                    return 'Please use only even numbers!'
            except TypeError:
                return 'Please use only even numbers!'

        return function(*args, **kwargs)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

print('---')


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
