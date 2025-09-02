# Bagram Game Simulation
#
# Simulating the game 'Bagram', a game where the player avoids being the one
# to say the number 21. Players may choose to call up to 3 consecutive numbers.
#
# Calling non-consecutive numbers is an immediate loss. 

"""
Planned Algorithm

Ask for player name:
Ask whether the player wants to go first or second
If the player goes second:
    Start computer turn
Else:
    While loop for player -> computer turns:
        Player Turn:
            Request numbers to be entered
            Retrieve numbers -- check for consecutive numbers
                Check to see if numbers are in in order, consecutive, and not 21
                Order: is called_number - last_number == 1?
                Consecutive: if a number isnt in order, then it cant be consecutive
                21: Separate check, likely able to done during computer turn.
            Append numbers to numbers list as their called with last_called being
                every new number
            last_called = numbers_list[-1]

        Computer Turn:
            if the last_called was 20, computer loss.

            Attempt to call numbers to the nearest multiple of 4
                Done by checking the previous number in numbers list
                Calculate the next multiple (target) of 4 by doing:
                    4 - (previous_number % 4) -- capped at 3, ensure result < 4
                Call numbers up to the next multiple of 4 (maximum of 3)
                    While Loop (while called_number < target)
                    All numbers appended to numbers list, last_called = numbers_list[-1]

            If the computer lands on 20 (last_called), player loss
"""

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
            



    




