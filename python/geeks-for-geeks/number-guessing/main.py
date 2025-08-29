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
    print(f"\nEnter a number to be guessed: ")