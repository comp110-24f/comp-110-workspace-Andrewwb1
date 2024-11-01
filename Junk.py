""" Practice """

"""Practicing my conditions."""


def less_than_10(num: int) -> None:
    """tells us if num < 10"""
    if num < 10:  # check if this is true
        print("Small number!")  # then black
    else:
        print("Big number!")
    print(
        "This is the end of function!"
    )  # prints regardless of whether the input is greater than or less than


def wake_up(alarm: bool) -> str:
    """return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Kepp sleeping."


# print(wake_up(alarm=False))


"""CL07 Last Slide Practice"""


def check_first_letter(word: str, letter: str) -> str:
    """identifies whether a word inputed starts with letter inputed"""
    if word[0] == letter:
        return "Match!"
    else:
        return "No Match!"

    # print(
    check_first_letter(
        word="happy", letter="s"
    )  # so if the word is 'happy' and letter is 's' then it should be false since 'happy' doesn't start with letter 's'


"""CL08 Last Slide Practice - elif"""


def get_weather_report() -> str:
    """prompts user for weather and then outputs proper action"""
    weather: str = input("What is the Weather?")  # prompts user for the weather
    if (
        weather == "rainy" or weather == "cold"
    ):  # if it is rainy or cold will print following
        print("Bring a jacket!")
    elif weather == "hot":  # use second option for option
        print("Keep cool out there!")
    else:  # third option of if input is not recognized as one of the others
        "I don't recognize this weather."
    return weather  # just returns your intput


"""IDK"""


def double(x: int) -> int:
    return x * 2


def double_display(y: int):
    print(y * 2)

    # double_display(2)

    # if __name__ == "__main__":
    # print(double(3))

    # class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy

    # pt1: Point = Point(2.0, 1.0)
    # pt2: Point = Point(4.0, 6.0)

    # class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        return (
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2
        ) ** 0.5

    def get_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)


# Line1: Line = Line(pt1, pt2)

# print(Line1.get_slope())
