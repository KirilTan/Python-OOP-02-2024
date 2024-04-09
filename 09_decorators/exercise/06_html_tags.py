def tags(html_tag: str):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return f"<{html_tag}>{function(*args, **kwargs)}</{html_tag}>"

        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

print('---')


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
