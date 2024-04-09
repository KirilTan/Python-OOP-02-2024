class store_results:
    _FILE_NAME = 'log_class.txt'

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):

        with open(self._FILE_NAME, 'a') as log_file:
            log_file.write(
                f"Function: {self.function.__name__} was called.\n"
                f"It produced the result: {self.function(*args, **kwargs)}\n"
                f"---\n"
            )


@store_results
def some_function(a: int or float, b: int or float):
    result = (a + b)
    return "{:.2f}".format(result)


some_function(1, 2)
some_function(1.2345, 5.6789)
