# Word Guessing Game
# User attempts to guess a word hangman style from a set of predefined options.
# Limited number of guesses before game fails
# Can be modified by changing the variable
# Retrieve the name of the user and refer to the name throughout the program

import random

GUESS_COUNT = 12


# Displays the word with the correctly guessed characters being visible and the
# non-guessed characters being represented with a "-"
def display_word(word: str, guessed_chars: list) -> None:
    output_string = ""
    for char in word:
        if char in guessed_chars:
            output_string += char
        else:
            output_string += "-"
    print(output_string)


guesses = 0
word_guessed = False
word_list = []
guess_list = []

available_words = ["TESTING", "COMPUTER", "SCIENCE"]

name = input("Please enter your name for the Guessing Game: ")
print(f"Welcome to the game, {name}")


selected_word = random.choice(available_words)

for char in selected_word:
    if char not in word_list:
        word_list.append(char)

while guesses < GUESS_COUNT and not word_guessed:
    guessed_char = input(f"Enter a character to guess: ")
    guessed_char = guessed_char[0]
    guessed_char = str.upper(guessed_char)

    if guessed_char not in guess_list:
        guess_list.append(guessed_char)
        guesses += 1
    else:
        print(
            f"You have already guessed the character {guessed_char}! Please try again.\n"
        )

    display_word(selected_word, guess_list)

    if set(word_list).issubset(guess_list):
        word_guessed = True

if word_guessed and (guesses < GUESS_COUNT):
    print(f"Congratulations, {name}! You win. The word was {selected_word}\n")
    print(f"You took {guesses} tries to guess the word correctly!")
else:
    print(f"Oh no! You lost. The correct word was {selected_word}")

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
