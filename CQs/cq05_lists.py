"""mutating functions"""

__author__ = "730473549"


def manual_append(list1: list[int], number: int) -> None:
    """just making the append function"""
    list1.append(number)


def double(list1: list[int]) -> None:
    """multiplies every integer in list by two"""
    index: int = 0
    while index < len(list1):
        list1[index] = list1[index] * 2
        index += 1


# Global Vars Exploration

list1: list[int] = [1, 2, 3]
list2 = list1

double(list2)
print(list1)
print(list2)
