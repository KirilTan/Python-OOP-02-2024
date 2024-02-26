def print_rhombus(size: int) -> None:
    """
    Prints a rhombus of the specified size.

    Args:
        size (int): The size of the rhombus, which must be an odd number.

    Returns:
        None

    """
    print_upper_part(size)
    print_lower_part(size)


def print_upper_part(size: int) -> None:
    """
    Prints the upper part of a rhombus of the specified size.

    Args:
        size (int): The size of the rhombus, which must be an odd number.

    Returns:
        None

    """
    for row in range(1, size + 1):
        print(' ' * (size - row), '* ' * row)


def print_lower_part(size: int) -> None:
    """
    Prints the lower part of a rhombus of the specified size.

    Args:
        size (int): The size of the rhombus, which must be an odd number.

    Returns:
        None

    """
    for row in range(size - 1, 0, -1):
        print(' ' * (size - row), '* ' * row)


n = int(input())
print_rhombus(size=n)
