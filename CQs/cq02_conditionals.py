"""Simple number guessing game"""

__author__ = "730473549"


def guess_a_number() -> None:
    """function takes nothing and gives nothing, just a prompt for number input and game"""
    secret: int = 7  # establishing number user trying to guess
    x: int = int(
        input("Guess a number:")
    )  # prompting user for their guess and assigning it to x
    print("Your guess was " + str(x))  # printing back the guess
    if x == secret:  # if the guess is the secret number prints affirmative response
        print("You got it!")
    elif (
        x < secret
    ):  # if the guess is less than secret, says guess is too low, reveals secret number
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # if guess is not secret number of less than, must be greater than so responds as such
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
