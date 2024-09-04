"""Input number of guests and outputs tea bags,treats, and cost for the number of guests"""

__author__: str = "730473549"


def main_planner(guests: int) -> None:
    """Prints the output of each function to the screen"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Inputs number of people and outputs number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Inputs number of people and outputs numbers of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Inputs number of tea and treats and outputs combined cost"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    """prompts number of guests and then runs program"""
    main_planner(guests=int(input("How many guests are attending?")))
