# Number Guessing Game
# System chooses a value from 1 - 100 and the user guesses numbers until the
# correct result is reached. Different outputs depending on the guess in comparison to
# the given number:
#   guess > target -> "Too High"
#   guess < target -> "Too Low"

import random

guessed_number = -1 
total_guesses = 0
generated_number = random.randint(0, 100)

while (guessed_number != generated_number):
    
    try:
        guessed_number = int(input(f"\nEnter a number to be guessed: "))
    except ValueError:
        print(" !! [INVALID GUESS TYPE] !! ")

    if (type(guessed_number) != int) or (guessed_number < 0) or (guessed_number > 100):
        print("Please only enter positive integer values (0 - 100) for guesses.")
    else:
        total_guesses += 1
        if guessed_number < generated_number: print("Too Low!\n")
        elif guessed_number > generated_number: print("Too High!\n")

print(f"Congratulations on guessing the number {generated_number}!\n")
print(f"You took {total_guesses} guesses to find the correct number!")
