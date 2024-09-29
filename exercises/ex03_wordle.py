"""EX 03 - Wordle"""

__author__ = "730473549"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    """Prompts user for word and then validates that it is of the proper length"""
    guess_word: str = input(
        f"Enter a {secret_word_len} character word:"
    )  # stores user inputted word
    while (
        len(guess_word) != secret_word_len
    ):  # if the word is not of the right length then prompts user for another guess
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again:")
    return guess_word


def contains_char(word_param: str, char_param: str) -> bool:
    """Function that checks for the character within the word"""
    assert len(char_param) == 1  # assumes user input only one character
    index: int = 0  # counter
    instances: int = 0  # counts if character in word
    while index < len(word_param):
        if str(word_param[index]) == char_param:
            instances += (
                1  # if the character appears at that index spot then add to instances
            )
        index += 1
    return instances > 0  # bool if it found the character


def emojified(guess_word: str, secret_word: str) -> str:
    """compares guess to secret word and outputs corresponding emojis"""
    assert len(guess_word) == len(
        secret_word
    )  # assumes user input is of the proper length
    index2: int = 0
    emoji_str: str = ""  # empty str to build up emojis
    while index2 < len(guess_word):  # indexes through guess word
        if str(guess_word[index2]) == str(
            secret_word[index2]
        ):  # if same character in same place then green
            emoji_str += GREEN_BOX
        elif contains_char(
            secret_word, str(guess_word[index2])
        ):  # if same character but wrong place then yellow
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX  # if character not in secret word then white
        index2 += 1
    return emoji_str


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    loser: bool = True  # tracks if user has won game yet
    while (
        turn <= 6
    ) and loser:  # if you have not run out of turns or guessed the word then runs
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))  # stores value of user guess
        print(emojified(guess, secret))  # runs wordle emoji interface
        if guess == secret:  # if you guess the word sets you to not loser
            loser = False
        else:  # otherwise increase turn counter and go again
            turn += 1
    if loser:
        print("X/6 - Sorry try again tomorrow!")
    else:
        print(f"You won in {turn}/6 turns!")


if __name__ == "__main__":
    """runs as module and allows importing"""
    main(secret="codes")
