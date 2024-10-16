"""defining function that find largest value in list and removes all occurences"""

__author__ = "730473549"


def find_and_remove_max(list1: list[int]) -> int:
    """finds and returns largest number in list1 list and removes largest number from list"""
    if list1 == []:  # if list1 is empty returns -1 and exits function
        return -1
    max_val: int = list1[0]  # initializes empty max value holder
    for (
        elem
    ) in list1:  # if the element is greater than max_val then element becomes max val
        if elem > max_val:
            max_val = elem
    idx: int = 0
    while idx < len(list1):
        if (
            list1[idx] == max_val
        ):  # if the element is the max value will remove that element from list
            list1.pop(idx)
        else:  # assures no numbers are skipped in the list becuase index shifts over as element removed
            idx += 1
    return max_val
