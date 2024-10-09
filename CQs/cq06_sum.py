"""Summing the elements of a list using different loops"""

__author__ = "730473549"


def w_sum(vals: list[float]) -> float:
    "sums all elements within the list using while loop"
    sum: float = 0  # intializing empty float that will be used to store sum
    index: int = 0
    while index < len(vals):
        sum = sum + vals[index]  # adding each element to sum
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """sums all elements within the list"""
    sum: float = 0  # intializing empty float that will be used to store sum
    for idx in vals:
        sum = sum + idx  # adding each element to sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    """sums all elements within the list"""
    sum: float = 0  # intializing empty float that will be used to store sum
    for idx in range(0, len(vals)):
        sum = sum + vals[idx]  # adding each element to sum
    return sum
