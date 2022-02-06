#! bin/python
# bagels.py
# Original Author: Al Sweigart
# Bagels is a deductive logic game where you must gues
# a number based on textual clues.
# View the original code at
# https://nostarch.com/big-book-small-python-project

# Library imports
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        f"""Bagels, a deductive logic game.
    
    I am thinking of a {NUM_DIGITS}-digit number with
    no repeated digits.  Try to guess what it is.
    Here are some clues:

    When I say:     That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the right position.
        Bagels      No digit is correct.
        
    For example, if the secret number was 248 and your guess
    was 842, the clues would be Fermi Pico."""
    )
    # Main game loop
    secret = get_secret()
    print("I've thought of a number.")
    print("What is your guess?")
    guess_number = 1
    while guess_number <= MAX_GUESSES:
        guess = input(f"Guess #{guess_number}> ")
        # Validate guess format
        while len(guess) != NUM_DIGITS and guess.isdecimal():
            guess = input(f"Guess #{guess_number}> ")

        clues = get_clues(guess, secret)
        if clues == "Fermi Fermi Fermi":
            print("You got it!")
            break
        print(clues)
        guess_number += 1

        if guess_number > MAX_GUESSES:
            print("You're out of guesses!")
            print(f"The secret number was {secret}")
            print("Play again?", end="")
            if not input("> ").lower().startswith("y"):
                break
            else:
                guess_number = 1
                secret = get_secret()


def get_clues(guess: str, secret: str) -> str:
    """
    Compare guess to secret and return clues string for printing
    """
    if guess == secret:
        response = ["Fermi", "Fermi", "Fermi"]
    else:
        response = []

        for i, _ in enumerate(guess):
            if guess[i] == secret[i]:
                # Correct character, correct position
                response.append("Fermi")
            # Correct character, incorrect position
            elif guess[i] in secret:
                response.append("Pico")
        if len(response) == 0:
            # No correct characters
            response = ["Bagel"]
        else:
            sorted(set(response))

    return " ".join(response)


def get_secret() -> str:
    """
    Generate and return a NUM_DIGITS length string of random digits
    """
    return "".join(
        random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], NUM_DIGITS)
    )


if __name__ == "__main__":
    main()
