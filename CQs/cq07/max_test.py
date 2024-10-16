"""find_max unit tests"""

__author__ = "730473549"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_use1() -> None:
    """test return of expected value"""
    a: list[int] = [1, 2, 3, 4, 5]  # func should return max value of 5
    assert find_and_remove_max(a) == 5


def test_find_and_remove_max_use2() -> None:
    """test mutation of input in expected way"""
    a: list[int] = [1, 2, 3, 4, 5]
    find_and_remove_max(a)  # should remove max val which is 5 and mutate list
    assert a == [1, 2, 3, 4]


def test_find_and_remove_max_edge() -> None:
    """test return of correct val if unconven. input"""
    a: list[int] = [
        -10,
        -7,
        -3,
    ]  # all negative inputs should still yeild max value which is closest to zero
    assert find_and_remove_max(a) == -3
