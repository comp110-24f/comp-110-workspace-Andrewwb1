"""Imports function and runs program"""

__author__ = "730473549"

from CQs.cq04.concatenation import (
    concat,
    word1,
    word2,
)  # importing concat function from companion file

x: str = "123"  # word1 input
y: str = "abc"  # word2 input

print(concat(x, y))  # calling function and printing result

from CQs.cq04.coordinates import (
    get_coords,
)  # importing get coords func from companion file

get_coords(x, y)  # calls function using global vars x and y
