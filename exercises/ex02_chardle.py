"""EX 02 - Chardle - A cute step towards Wordle"""

__author__ = "730473549"


def input_word() -> str:
    """gathers user input on word"""
    word: str = input("Enter a 5-character word: ")
    """prompts user for word"""
    if len(word) == 5:
        """if length of word is five then returns the word"""
        print(word)
    else:
        """if length is not 5 returns an error message"""
        print("Error: Word must contain 5 characters.")
        exit()
    """quits running program if error occurs"""
    return word


def input_letter() -> str:
    """gathers single letter guess from user"""
    character: str = input("Enter a single character: ")
    """prompts user for a character"""
    if len(character) == 1:
        """ensures only single character input"""
        print(character)
    else:
        """returns error message if user inputs invalid"""
        print("Error: Character must be a single character.")
        exit()
        """quits running program if error ocrrus"""
    return character


def contains_char(word: str, character: str) -> None:
    """check if the input character matches any of the characters within the input word"""
    print("Searching for " + character + " in " + word)  # message for user
    count: int = 0
    if word[0] == character:
        """if first letter is the guess character then prints such"""
        print(character + " found at index 0")
        count += 1
    else:
        """otherwise prints nothing"""
        None
    if word[1] == character:
        """repeat index for each letter"""
        print(character + " found at index 1")
        count += 1
    else:
        None
    if word[2] == character:
        print(character + " found at index 2")
        count += 1
    else:
        None
    if word[3] == character:
        print(character + " found at index 3")
        count += 1
    else:
        None
    if word[4] == character:
        print(character + " found at index 4")
        count += 1
    else:
        None
    if count == 0:
        """if there are no occurences print this message"""
        print("No instances of " + character + " found in " + word)
    elif count == 1:
        """if there is one occurence prints singular of instance"""
        print(str(count) + " instance of " + character + " found in " + word)
    else:
        """otherwise prints plural of instances"""
        print(str(count) + " instances of " + character + " found in " + word)


def main() -> None:
    """calls functions to run the game"""
    contains_char(word=input_word(), character=input_letter())


if __name__ == "__main__":
    """makes program run as module"""
    main()
