"""Using while loop to iterate over a string"""

__author__ = "730473549"


def num_instances(phrase: str, search_char: str) -> int:
    """counts number of instances of search character in phrase"""
    count: int = 0  # instance counter
    index: int = 0  # index
    while index < len(phrase):  # runs index
        if (
            str(phrase[index]) == search_char
        ):  # if the letter at index is the search character adds to counter
            count += 1
        else:
            count += 0  # otherwise doesn't add to counter
        index += 1
    return count  # returns the count


print(num_instances("Hoop", "o"))
