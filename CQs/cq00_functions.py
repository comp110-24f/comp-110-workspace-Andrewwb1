__author__ = "730473549"


def mimic(message: str) -> str:
    """returns input back to you"""
    return message


def main() -> None:
    """prints result of calling mimic"""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
