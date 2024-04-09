def type_check(_type: type):
    def decorator(function):
        def wrapper(*args, **kwargs):

            for arg in args:
                if not isinstance(arg, _type):
                    return 'Bad Type'

            for k, v in kwargs:
                if not isinstance(v, _type):
                    return 'Bad Type'

            return function(*args, **kwargs)

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))

print('---')


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
