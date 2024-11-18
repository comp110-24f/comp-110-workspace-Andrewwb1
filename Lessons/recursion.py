"""11/18 Recursive Functions"""


def factorial(n: int) -> int:
    """factorial calculation of given input, n."""
    if n < 0:
        raise ValueError("Cannot compute factorial for negative integer")
    elif n == 0:  # base case
        return 1
    else:  # recursive case
        return n * factorial(n - 1)


print(factorial(0))
