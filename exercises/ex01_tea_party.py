"""Input number of guests and outputs tea bags,treats, and cost for the number of guests"""

__author__: str = "730473549"


def main_planner(guests: int) -> None:
    """Prints the output of each function to the screen"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints str of number of guests
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # calls tea bags function with key word arg
    print(
        "Treats: " + str(treats(people=guests))
    )  # calls treats function with key word arg
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # calls cost function with key word arguments


def tea_bags(people: int) -> int:
    """Inputs number of people and outputs number of tea bags needed"""
    return people * 2  # returns number of people multiplied by 2


def treats(people: int) -> int:
    """Inputs number of people and outputs numbers of treats needed"""
    return int(
        tea_bags(people=people) * 1.5
    )  # returns the int of 1.5 times number of people
    # will round float response to nearest integer since cannot have partial tea bag
    # would probably make sense to always round up. But, since 1.5 is price, answer will either be whole number or end in .5 and thus essentially does round up
    # uses a key word arg


def cost(tea_count: int, treat_count: int) -> float:
    """Inputs number of tea and treats and outputs combined cost"""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # multiplies results of number of goods times their respective costs
    # since cost is in dollars and cents, float is reasonable


if __name__ == "__main__":
    """prompts user with number of guests question and then runs main planner program"""
    main_planner(
        guests=int(input("How many guests are attending?"))
    )  # calls main planner function
    # asks user question
    # allows user input of number of guests
