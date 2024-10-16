"""unit testing utils.py"""

__author__ = "730473549"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edge() -> None:
    """if empty list inputted returns empty list"""
    a: list[int] = []  # empty list
    assert only_evens(a) == []


def test_only_evens_use1() -> None:
    """testing basic behavrior, func should mutate list and return evens only"""
    a: list[int] = [20, 40, 33]
    assert only_evens(a) == [20, 40]  # should return even elements


def test_only_evens_use2() -> None:
    """testing case where no evens given, func should mutate list"""
    a: list[int] = [17, 9, 43]
    assert only_evens(a) == []  # no evens so should get empty


def test_sub_edge() -> None:
    """testing if empty string returns empty string"""
    a: list[int] = []
    assert sub(a, 1, 3) == []


def test_sub_use1() -> None:
    """testing normal run"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, 1, 3) == [2, 3]


def test_sub_use2() -> None:
    """testing if idx2 beyond length idx is mutated to equal length"""
    a: list[int] = [1, 2, 3, 4]
    assert sub(a, 0, 12) == [1, 2, 3, 4]
