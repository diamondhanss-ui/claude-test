"""
Sample module with a few simple utility functions.
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


def reverse_string(text: str) -> str:
    """Return the given string reversed."""
    return text[::-1]


if __name__ == "__main__":
    print(add(2, 3))
    print(is_even(4))
    print(reverse_string("sample"))
