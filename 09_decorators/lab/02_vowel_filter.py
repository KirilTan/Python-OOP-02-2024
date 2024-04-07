def vowel_filter(function):

    def wrapper():
        vowels = ["a", "e", "i", "o", "u"]
        return [letter for letter in function() if letter in vowels]

    return wrapper


# Test code
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
