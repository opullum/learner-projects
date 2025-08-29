# Number Guessing Game
# User provides a value for the lower and upper bounds (inclusive)
# System chooses a value from LOWER_BOUND - UPPER_BOUND and the user guesses numbers until the
# correct result is reached. Different outputs depending on the guess in comparison to
# the given number:
#   guess > target -> "Too High"
#   guess < target -> "Too Low"
# User will have a maximum number of guesses based on Binary Search Algorithm (7)
#   If the user follows the Binary Search Algorithm it should take no more than 7 guesses.
#   Program will display appropriate number of guesses if reached

MAXIMUM_GUESSES = 7

import random

guessed_number = -1
total_guesses = 0

upper_bound = -1
lower_bound = -1

while not (upper_bound > lower_bound):
    try:
        lower_bound = int(input(f"Enter the lower bound for guesses: "))
        upper_bound = int(input(f"Enter the upper bound for guesses: "))
    except ValueError:
        print(f"[!] Please enter a valid number for the Upper and Lower bounds")


generated_number = random.randint(lower_bound, upper_bound)

while guessed_number != generated_number and total_guesses < MAXIMUM_GUESSES:

    try:
        guessed_number = int(input(f"\nEnter a number to be guessed: "))
    except ValueError:
        print("!! [INVALID GUESS TYPE] !!")

    if (type(guessed_number) != int) or (guessed_number < 0) or (guessed_number > 100):
        print("Please only enter positive integer values (0 - 100) for guesses.")
    else:
        total_guesses += 1
        if guessed_number < generated_number:
            print("Too Low!\n")
        elif guessed_number > generated_number:
            print("Too High!\n")

if total_guesses < MAXIMUM_GUESSES:
    print(f"Congratulations on guessing the number {generated_number}!\n")
    print(f"You took {total_guesses} guesses to find the correct number!")
else:
    print(f"It took you too many guesses to guess the number {generated_number}")
