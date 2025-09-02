# Bagram Game Simulation
#
# Simulating the game 'Bagram', a game where the player avoids being the one
# to say the number 21. Players may choose to call up to 3 consecutive numbers.
#
# Calling non-consecutive numbers is an immediate loss. 

import sys

from computer import computer_turn
from player import player_turn

called_numbers = []
recent_number = None
game_ended = False
playing = True

while playing:
    print(f"WELCOME TO BAGRAM. WOULD YOU LIKE TO GO FIRST OR SECOND?")
    print("ENTER 'FIRST' TO GO FIRST AND 'SECOND' TO GO SECOND")
    response = input("> ").lower()

    if not (response == "first" or response == "second"):
        print("I'M AFRAID THAT IS NOT A VALID OPTION. GOODBYE.")
        playing = False

    if (response == "second"):
        print("THEN YOU WILL GO SECOND. ALLOW US TO BEGIN.")

        while (not game_ended):
            if (not game_ended): game_ended, playing = computer_turn(called_numbers)
            if (not game_ended): game_ended, playing = player_turn(called_numbers)
    elif (response == "first"):
        print("THEN YOU WILL GO FIRST. ALLOW US TO BEGIN.")

        while (not game_ended):
            if (not game_ended): game_ended, playing = player_turn(called_numbers)
            if (not game_ended): game_ended, playing = computer_turn(called_numbers)
            



    




