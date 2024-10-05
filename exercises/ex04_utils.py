"""Copying the greats"""

__author__ = "730473549"


def all(list1: list[int], num1: int) -> bool:
    """Checks whether all ints in list are of input int"""
    index: int = 0
    if len(list1) == 0:
        return False
    while index < len(list1):
        if list1[index] != num1:
            return False
        index += 1
    return True


def max(list1: list[int]) -> int:
    """returns the max int of the list"""
    if len(list1) == 0:  # if the list is empty returns an error
        raise ValueError("max() arg is an empty List")
    index: int = 0
    big_val: int = list1[index]  # max value storing, starting with first element
    while index < len(list1):
        if big_val < list1[index]:
            big_val = list1[
                index
            ]  # if the big value is smaller than current value then replace with new index
        index += 1
    return big_val


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """returns True if lists are identical"""
    index1: int = 0
    index2: int = 0
    if len(list1) != len(list2):  # lists not of equal length are not equal
        return False
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] != list2[index2]:
            return False
        index1 += 1
        index2 += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """appends all elements in list2 to list 1"""
    index: int = 0
    while index < len(list2):
        list1.append(list2[index])
        index += 1
