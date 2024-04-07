from functools import wraps


def even_numbers(function):
    @wraps(function)
    def wrapper(numbers):
        return [number for number in numbers if number % 2 == 0]

    return wrapper


# Test code
@even_numbers
def get_numbers(numbers):
    """Test function"""
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
print(get_numbers.__doc__)
