# Word Guessing Game
# User attempts to guess a word hangman style from a set of predefined options.
# Limited number of guesses before game fails
    # Can be modified by changing the variable
# Retrieve the name of the user and refer to the name throughout the program

import random

GUESS_COUNT = 12

name = input("Please enter your name for the Guessing Game: ")
print(f"Welcome to the game, {name}")

guesses = 0

# planned algorithm
#
# for each character in selected word:
#   if character not in word table:
#       add character to word char list
#
# while guesses less than guess count and not word guessed
#   allow the user to guess a character
#   check if the character already has been guessed -> output message
#   if not: add guesses to guess list
#   DISPLAY WORD
#       display each character sequentially
#       if char in guessed_characters output the character
#       else: output a "-" or similar character to show char has not been guessed
#   increment guesses
#
#   if word list == guess list
#       guessed = true
#
# display condition after loop ends:
#   if guessed and (guesses < GUESS_COUNT)
#       you win!!
#   else:
#       you lose!!

