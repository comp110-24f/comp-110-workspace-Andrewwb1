"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730473549"


class River:
    """New class that will utilize Fish and Bear to model the environment."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Simulates death by removing oldest in population."""
        survivor_fish: list[Fish] = []  # new list of remaining fish
        for fish in self.fish:  # iterate through our list
            if fish.age <= 3:  # if the fish young enough gets added to survivor list
                survivor_fish.append(fish)
        self.fish = survivor_fish  # set survivor list to be fish list

        survivor_bears: list[Bear] = []  # same idea as above but with diff age for bear
        for bear in self.bears:
            if bear.age <= 5:
                survivor_bears.append(bear)
        self.bears = survivor_bears
        return None

    def remove_fish(self, amount: int):
        """Method for removing fish when eaten by bears."""
        while amount > 0:  # removing first element amount times
            self.fish.pop(0)
            amount -= 1

    def bears_eating(self):
        """Bears consuming fish at a rate of 3 fish per bear."""
        for bear in self.bears:
            if len(self.fish) >= 5:  # must be at least 5 fish for bear
                bear.eat(3)
                River.remove_fish(self, 3)  # uses remove_fish method
        return None

    def check_hunger(self):
        """Simulates starvation and filters out starved bears."""
        survivor_bears: list[Bear] = []  # new list of bears that don't die
        for bear in self.bears:
            if bear.hunger_score >= 0:  # positive hunger bears get added to new list
                survivor_bears.append(bear)
        self.bears = survivor_bears  # assign only survivors to bear list
        return None

    def repopulate_fish(self):
        """Method for fish reproduction that adds 4 fish for every 2 existing."""
        fish_couples: int = int(
            (len(self.fish) - (len(self.fish) % 2)) / 2
        )  # if odd subtracts to next lower even
        new_fish: int = fish_couples * 4  # 4 offspring per couple
        while (
            new_fish > 0
        ):  # just iterating through new fish and adding Fish class to list
            self.fish.append(Fish())
            new_fish -= 1
        return None

    def repopulate_bears(self):  # same concept at repop fish
        """Bears reproduce at a rate of 1 bear per couple."""
        bear_couples: int = int((len(self.bears) - (len(self.bears) % 2)) / 2)
        new_bear: int = bear_couples
        while new_bear > 0:
            self.bears.append(Bear())
            new_bear -= 1
        return None

    def view_river(self):
        """Outputs current river information."""
        print(
            f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear Population: {len(self.bears)}"
        )  # need to be length becuase these are list types
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        self.one_river_day()  # calls one river day 7 times
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
