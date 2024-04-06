def genrange(start: int, end: int):
    current_num = start
    while current_num <= end:
        yield current_num
        current_num += 1


# Test code
print(list(genrange(1, 10)))


