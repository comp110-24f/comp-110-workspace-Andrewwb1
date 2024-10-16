"""unit testing utils.py"""

__author__ = "730473549"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge() -> None:
    """if empty list inputted returns empty list"""
    a: list[int] = []  # empty list
    assert only_evens(a) == []


def test_only_evens_use1() -> None:
    """testing basic behavior, func should return evens only"""
    a: list[int] = [20, 40, 33]
    assert only_evens(a) == [20, 40]  # returns even elements


def test_only_evens_use2() -> None:
    """function should not mutate input list"""
    a: list[int] = [17, 9, 43]
    only_evens(a)
    assert a == [17, 9, 43]  # input list should be unchanged


def test_sub_edge() -> None:
    """testing if idx2 beyond length idx is changed to equal length"""
    a: list[int] = [1, 2, 3, 4]
    assert sub(a, 0, 12) == [1, 2, 3, 4]


def test_sub_use1() -> None:
    """testing if empty string returns empty string"""
    a: list[int] = []
    assert sub(a, 1, 2) == []


def test_sub_use2() -> None:
    """testing func does not mutate input"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    sub(a, 1, 3)
    assert a == [1, 2, 3, 4, 5, 6]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    with pytest.raises(IndexError):
        add_at_index(a, 12, 12)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>


def test_add_at_index_edge() -> None:
    """testing if you add number to empty list at correct position"""
    a: list[int] = []
    add_at_index(a, 1, 0)  # should still get output since adding to only element
    assert a == [1]


def test_add_at_index_use1() -> None:
    """testing baisc use, input list should be mutated and output should be added"""
    a: list[int] = [1, 2, 3, 5]
    add_at_index(a, 4, 3)
    assert a == [1, 2, 3, 4, 5]


def test_add_at_index_use2() -> None:
    """function should return None"""
    a: list[int] = [1]
    assert add_at_index(a, 0, 1) == None
