"""implementing utitlity functions for Ex 06"""

__author__ = "730473549"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """inverts keys and values"""
    output: dict[str, str] = {}  # instantiating empty str
    for key in dict1:
        if dict1[key] in output:  # if the inverted key already exists raise error
            raise KeyError("key already exists!")
        output[dict1[key]] = key  # inverts input and writes to new dict
    return output


def favorite_color(cols: dict[str, str]) -> str:
    """returns color that is most popular (if tie one that appears first)"""
    counts: dict[str, int] = {}  # stores counts of all colors mentioned
    winner_count: int = 0  # output winning color count
    winner_name: str = ""  # output color
    for key in cols:
        if (
            cols[key] in counts
        ):  # if the color is already in the counter dict then adds to value at key
            counts[cols[key]] += 1
        else:
            counts[cols[key]] = 1  # otherwise writes color as key and adds value of 1
    for key in counts:
        if (
            counts[key] > winner_count
        ):  # finds the largest value in dict (or first in a tie)
            winner_count = counts[key]  # updates the largest count
            winner_name = key  # stores key associated with largest value
    return winner_name


def count(inp: list[str]) -> dict[str, int]:
    """counts the number of time each elem appears in list and returns dict of all elems and number of appearances"""
    result: dict[str, int] = {}  # output
    for elem in inp:  # cycling through elements in input list
        if elem in result:
            result[elem] += 1  # if elements already found increasing counter
        else:
            result[elem] = (
                1  # otherwise writes new key value pair with count starting at 1
            )
    return result


def alphabetizer(inp: list[str]) -> dict[str, list[str]]:
    """sorts input strings by first letter and groups them in output"""
    output: dict[str, list[str]] = {}  # output
    for elem in inp:
        low_elem = elem.lower()  # makes sure string starts with lowercase
        if (
            low_elem[0] in output
        ):  # if first letter already exists as key then adds word to list value
            output[low_elem[0]] += [elem]
        else:
            output[low_elem[0]] = [elem]  # otherwise establishing neww key value pair
    return output


def update_attendance(old_attend: dict[str, list[str]], day: str, student: str) -> None:
    """updates old attendance sheet with new students on certain days"""
    if (
        day in old_attend
    ):  # if day already key in old_attend then adds student to list value
        if (
            student not in old_attend[day]
        ):  # only adds student not already in list that day
            old_attend[day] += [student]
    else:
        old_attend[day] = [
            student
        ]  # otherwise writes new key value pair of day and student as list
