from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        return [letter for letter in function() if letter in vowels]

    return wrapper


# Test code
@vowel_filter
def get_letters():
    """
    Test function
    """
    return ["a", "b", "c", "d", "e"]


print(get_letters())
print(get_letters.__doc__)
