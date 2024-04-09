def store_results(function):
    _FILE_NAME = 'function_solution/log_function.txt'

    def wrapper(*args, **kwargs):
        with open(_FILE_NAME, 'a') as log_file:
            log_file.write(
                f"Function: {function.__name__} was called with args: {args} and kwargs: {kwargs}.\n"
                f"It produced the result: {function(*args, **kwargs)}\n"
                f"---\n"
            )

    return wrapper


@store_results
def some_function(a: int or float, b: int or float):
    result = (a + b)
    return "{:.2f}".format(result)


some_function(1, 2)
some_function(1.2345, 5.6789)
