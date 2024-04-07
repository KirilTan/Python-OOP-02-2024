from functools import wraps


def multiply(factor):
    @wraps(factor)
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * factor

        return wrapper

    return decorator


# Test code
@multiply(3)
def add_ten(number):
    """Test function"""
    return number + 10


print(add_ten(3))
print(add_ten.__doc__)

print('---------------------------------------------------------------------------------------------------------------')


@multiply(5)
def add_ten(number):
    """Test function two"""
    return number + 10


print(add_ten(6))
print(add_ten.__doc__)
