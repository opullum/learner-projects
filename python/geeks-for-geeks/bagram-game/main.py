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

def computer_lost() -> bool:

    continue_playing = True

    print("OH NO! IT APPEARS THE COMPUTER HAS LOST!")
    print("CONGRATULATIONS ON WINNING!")
    print("WOULD YOU LIKE TO KEEP PLAYING?")
    print("ENTER 'YES' or 'NO' AS AN ANSWER!")
    response = input("> ").lower()

    if (response == 'no'): continue_playing = False

    return continue_playing

def player_lost() -> bool:
    continue_playing = True
    
    print("OH NO! IT APPEARS YOU HAVE LOST!")
    print("WOULD YOU LIKE TO KEEP PLAYING?")
    print("ENTER 'YES' OR 'NO' AS AN ANSWER!")
    response = input("> ").lower()

    if (response == 'no'): continue_playing = False

    return continue_playing

def computer_turn(called_numbers: list) -> bool:

    recent_number = 0
    target_distance = 0
    game_ended = False

    # Calculate target value for the computer to attempt to call towards
    if called_numbers:
        recent_number = called_numbers[-1]
        target_distance = 4 - (recent_number % 4) 

        if recent_number == 20: 
            computer_lost()
            game_ended = True

    if (not game_ended):
        if target_distance > 3: target_distance = 3

        added_num = recent_number + 1

        while added_num < recent_number + target_distance:        
            called_numbers.append(added_num)
            added_num += 1   

        recent_number = called_numbers[-1]

        if recent_number == 20: 
            continue_playing = player_lost()
            game_ended = True

    return game_ended


called_numbers = []
recent_number = None
playing = True

print("ENTER THE NAME YOU WOULD LIKE TO USE")
player_name = input("> ")

print(f"WELCOME TO BAGRAM, {player_name}. WOULD YOU LIKE TO GO FIRST OR SECOND?")
print("ENTER 'FIRST' TO GO FIRST AND 'SECOND' TO GO SECOND")
response = input("> ").lower()

if not (response == "first" or response == "second"):
    print("I'M AFRAID THAT IS NOT A VALID OPTION. GOODBYE.")
    playing = False

if (response == "second"):
    print("THEN YOU WILL GO SECOND. ALLOW US TO BEGIN.")

    




