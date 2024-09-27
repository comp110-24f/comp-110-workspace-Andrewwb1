"""Defines concatenation function, input variables, and then prints call"""

__author__ = "730473549"

# global vars def #
word1: str = "happy"
word2: str = "tuesday"


def concat(string1: str, string2: str) -> str:
    """combines two strings into 1 and returns the concatenation"""
    strings: str = string1 + string2
    return strings


if __name__ == "__main__":  # supresses call
    print(concat(word1, word2))
