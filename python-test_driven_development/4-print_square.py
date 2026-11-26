#!/usr/bin/python3
"""Module providing a function to print a square using '#' characters."""


def print_square(size):
    """Print a square with the character '#' of a given side length.

    Args:
        size (int): The side length of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
