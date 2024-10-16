"""implementing utility functions"""

__author__ = "730473549"


def only_evens(list1: list[int]) -> list[int]:
    """returns integers from input list that are even numbers"""
    evens: list[int] = []  # initiallizing empty list for even elements
    for elem in list1:  # looping through elements in the list
        if elem % 2 == 0:
            evens.append(elem)  # if the element is even then adds to evens list
    return evens


def sub(list1: list[int], idx1: int, idx2: int) -> list[int]:
    """returns subset of input list that is between the start index and end index -1"""
    output_list: list[int] = []  # initiallizing empty list for sublist
    if idx1 < 0:  # if negative index 1, changes it to start of list
        idx1 = 0
    if idx2 > len(list1):  # if idx2 is outside list, then changes it to end of list
        idx2 = len(list1)
    if len(list1) == 0:  # if list is empty then returns empty output list
        return output_list
    if idx1 >= len(
        list1
    ):  # if start of idx is greater or equal to length returns empty
        return output_list
    if idx2 <= 0:  # if end of idx is at most zero returns empty list
        return output_list
    for elem in range(idx1, idx2):
        output_list.append(
            list1[elem]
        )  # adds elements from input list to output list if they are between the idxs
    return output_list


def add_at_index(list1: list[int], num1: int, idx1: int) -> None:
    """modifies list1 by adding elem1 at idx1 to the list"""
    if idx1 < 0 or idx1 > len(list1):  # throws error if index is out of range
        raise IndexError("Index is out of bounds for the input list")
    list1.append(0)  # add space to end of list
    for idx in range(
        idx1 + 1, len(list1)
    ):  # shifts down all elements by one starting after target idx
        list1[idx] = list1[
            idx - 1
        ]  # now have two occuences of same number at idx1 and idx+1
    list1[idx1] = num1  # mutate element at idx1 to input target int
