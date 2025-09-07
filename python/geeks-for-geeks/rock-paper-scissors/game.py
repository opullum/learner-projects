from random import randint
from os import system

# Stores the result of the previously played match in a list to be referenced
# 
# GAME #[game_number] [WIN/LOSS/DRAW]
# PLAYER: [ROCK/PAPER/SCISSORS]
# COMPUTER: [ROCK/PAPER/SCISSORS]

def store_results(plr_select: int, comp_select: int, result: str, game_data: dict) -> None:

    match_list = ["ROCK", "PAPER", "SCISSORS"]
    plr_choice = match_list[plr_select]
    comp_choice = match_list[comp_select]

    result_str = (
        f"GAME #{game_data["matches"] + 1} [{result}]\n"
        + f"PLAYER: {plr_choice}\n"
        + f"COMPUTER: {comp_choice}"
    )

    if len(game_data["results"]) == 5: game_data["results"].pop(0)
    game_data["results"].append(result_str)

# Iterates through results list[str] to output match results to the screen

def show_results(results_list: list):
    system('cls||clear')
    print("PRINTING RESULTS OF PREVIOUS 5 MATCHES...")
    for result in results_list:
        print(result + '\n')

    print("\n\nPRESS ENTER KEY TO CONTINUE...")
    input()

# Evaluates the winner of a match by comparing player and computer (int) selections
# Options comparison list stores the option a choice "wins" against

def eval_winner(plr_select: int, comp_select: int) -> int:

    # Option Comparison List
    # INDEX 0: [2] (Rock beats scissors)
    # INDEX 1: [0] (Paper beats rock)
    # INDEX 2: [1] (Scissors beats paper)

    game_list = [2, 0, 1]
    if comp_select == plr_select: return -1
    if comp_select == game_list[plr_select]: return 1
    else: return 0


# Main Menu function to provide player options
# Returns int (option) corresponding to the selected option to be referenced

def menu() -> int:
    system('cls||clear')

    selection = -1

    print("[ROCK PAPER SCISSORS]")
    print("SELECT A MENU OPTION FROM THE CHOICES BELOW:")
    print("1. Start Game")
    print("2. List Previous Matches")
    print("0. Exit Program")

    while selection > 2 or selection < 0:
        selection = int(input("> "))

    return selection


# Game Function. Starts the Rock-Paper-Scissors Game

def start_game(game_data: dict) -> None:
    system('cls||clear')

    plr_select = -1
    result = ""

    print("STARTING A NEW ROUND...")
    
    print("CHOOSE AN OPTION:")
    print("  ROCK (0)")
    print("  PAPER (1)")
    print("  SCISSORS (2)")

    while plr_select > 2 or plr_select < 0:
        plr_select = int(input("> "))

    comp_select = randint(0, 2)
    result = eval_winner(plr_select, comp_select)

    match (result):
        case 1:
            print("CONGRATULATIONS! YOU WIN!")
            result = "WIN"
        case 0:
            print("OH NO! YOU LOST!")
            result = "LOSS"
        case _:
            print("IT'S A DRAW!")
            result = "DRAW"

    store_results(plr_select, comp_select, result, game_data)
    game_data["matches"] += 1

    print("DO YOU WISH TO KEEP PLAYING? ('YES' OR 'NO')")
    choice = input("> ").lower()
    
    if choice == 'yes': start_game(game_data)
