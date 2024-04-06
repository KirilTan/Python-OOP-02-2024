def reverse_text(text: str):
    reversed_text = text[::-1]
    for char in reversed_text:
        yield char


# Test code
for char in reverse_text("step"):
    print(char, end='')
