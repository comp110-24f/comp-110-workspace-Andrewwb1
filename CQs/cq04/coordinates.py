"""defines get_coords function to be exported"""

__author__ = "730473549"


def get_coords(xs: str, ys: str) -> None:
    index: int = 0
    while index < len(xs):
        index2: int = 0
        while index2 < len(ys):
            print("(" + xs[index] + "," + ys[index2] + ")")
            index2 += 1
        index += 1
