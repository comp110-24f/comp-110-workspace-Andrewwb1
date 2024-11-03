"""File to define Bear class."""

__author__ = "730473549"


class Bear:
    """New Bear class where each bear has an age and a hunger_score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initiliating age 0 and hunger score 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulating 1 day of life for a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Keeping tracking of bear eating."""
        self.hunger_score += num_fish
