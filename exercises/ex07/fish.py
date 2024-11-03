"""File to define Fish class."""

__author__ = "730473549"


class Fish:
    """New class called Fish with just an age."""

    age: int

    def __init__(self):
        """Initiliazing birth age of 0."""
        self.age = 0
        return None

    def one_day(self):
        """Simulating one day for a fish aging."""
        self.age += 1
        return None
