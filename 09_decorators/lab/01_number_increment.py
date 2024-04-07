def number_increment(numbers):

    def increase():
        return [number + 1 for number in numbers]

    return increase()


# Test code
print(number_increment([1, 2, 3]))
