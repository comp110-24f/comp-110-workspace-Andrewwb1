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


print(wake_up(alarm=False))


"""CL07 Last Slide Practice"""


def check_first_letter(word: str, letter: str) -> str:
    """identifies whether a word inputed starts with letter inputed"""
    if word[0] == letter:
        return "Match!"
    else:
        return "No Match!"


print(
    check_first_letter(word="happy", letter="s")
)  # so if the word is 'happy' and letter is 's' then it should be false since 'happy' doesn't start with letter 's'
