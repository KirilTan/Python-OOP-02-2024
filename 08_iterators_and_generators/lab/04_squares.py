def squares(n: int) -> int:
    current_num = 1

    while current_num <= n:
        yield current_num ** 2
        current_num += 1


# Test code
print(list(squares(5)))
