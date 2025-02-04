import time
import os
from colorama import Fore

GAME_NAME = "Skyrim 2"


class Format:
    end = "\033[0m"
    underline = "\033[4m"


def clear_terminal():
    """Runs command "cls" when on"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_letter_by_letter(text):
    for i in text:
        print(i, end="")
        time.sleep(0.03)
    print("")


def game_intro():
    # egg
    os.system("color 7f")
    print_letter_by_letter(
        Format.underline + Fore.WHITE + f"Welcome to {GAME_NAME}" + Format.end
    )
    os.system("color 7f")
    print("")
    time.sleep(2)


def second_intro():
    # change function name from second intro to something else, dunno yet, stupid name.
    print_letter_by_letter("Hey you, you're finally awake... again.")
    time.sleep(1)
    print_letter_by_letter("You were trying to cross the border, right?")
    time.sleep(1)
    print_letter_by_letter(
        "Walked right into that Imperial ambush, same as us, and that thief over there."
    )
    time.sleep(1)


if __name__ == "__main__":
    clear_terminal()
    game_intro()
    second_intro()
    os.system("color 0f")
