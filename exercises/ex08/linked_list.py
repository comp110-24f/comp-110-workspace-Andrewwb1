"""Linked List in class practice. Exercise 8 at the bottom."""

from __future__ import annotations


class Node:
    """New class of linked lists with a value and next Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Class constructor."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: figure out rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)  # calling a constructor
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
# these two could be combined to:
# one_two: Node = Node(1, Node(2,None))
courses: Node = Node(110, Node(210, Node(301, None)))
# in one line we are constructing 3 Node object
# the most inner parenthesis is the most inner node, the last node
# print(one)
# print(str(courses))
# print(courses)
# all three of these lines access the magic method __str__
# becuase we defined a str representation of each


# implementation as a function for what we earlier defined as a method
def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


# print(to_str(one))
# print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: When head is the last node
    print(f"Enter last ({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value}")
        # return its value!
        return head.value
    # Recursive case:
    else:
        #   Figure out the last node (recursive call)
        #   in the "rest of list"
        #   Return this value!
        rest: int = last(
            head.next  # this needs to be a .NEXT otherwise infinite recursion
        )  # recursion becauase we use the function in the function
        print(f"Return recur: {head.value} -> {rest}")
        return rest


# if you get recursion error you are not making progress to the base case, infinite loop basically
# make sure you are moving to the next node in the recursive statement
# Will the base case always be reached?
# It always should
# Use edge cases to test

# print(last(one))  # Expect to print 2
# print(last(courses))  # Expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)."""
    # Raise an Exception with string "Invalid use of recursive_range" when called improperly
    if start > end:
        raise ValueError("Invalid use of recursive_range")
    # Base case
    if start == end:
        return None
    # Recursive case
    else:
        return Node(start, recursive_range(start + 1, end))


# a: Node | None = recursive_range(2, 8)
# b: Node | None = recursive_range(110, 112)
# print(a)
# print(b)


# --------------------------EX 08-------------------------------- #


def value_at(head: Node | None, index: int) -> int:
    """Returns that value stored at an indexed Node."""
    if head is None:
        raise IndexError(
            "Index is out of bounds on the list."
        )  # edge case for empty list
    elif index == 0:  # base case 2
        return head.value
    else:  # recursive
        return value_at(head.next, index - 1)


# print(value_at(Node(10, Node(20, Node(30, None))), 0))
# print(value_at(Node(10, Node(20, Node(30, None))), 1))
# print(value_at(Node(10, Node(20, Node(30, None))), 2))
# print(value_at(Node(10, Node(20, Node(30, None))), 3))


def max(head: Node | None) -> int:
    """Returns maximum value from linked list of Nodes."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:  # base case
        return head.value
    else:  # recursive case
        if head.value > head.next.value:
            head.next.value = head.value
        return max(head.next)


# print(max(Node(10, Node(20, Node(30, None)))))
# print(max(Node(10, Node(30, Node(20, None)))))
# print(max(Node(30, Node(20, Node(10, None)))))
# print(max(None))


def linkify(items: list[int]) -> Node | None:
    """Takes in list and returns linked list of Nodes with same values."""
    if items == []:  # Base Case: items is empty
        return None
    else:  # Recursive Case
        return Node(
            items[0], linkify(items[1:])
        )  # Node created with value of first item in list and remaining part of list is next node


# print(linkify([1, 2, 3]))
# print(linkify([1]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Mltiplies each value in linked list by factor."""
    if head is None:  # Base Case: last node, which is none
        return None
    else:  # Recursive case:
        return Node(
            head.value * factor, scale(head.next, factor)
        )  # new node with value times factor, then recursion


# print(scale(linkify([1, 2, 3]), 2))
