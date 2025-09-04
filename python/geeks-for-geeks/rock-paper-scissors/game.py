import random


def store_results(plr_select: int, comp_select: int, result: str, results_list: list, matches: int) -> None:

    match_list = ["ROCK", "PAPER", "SCISSORS"]
    plr_choice = match_list[plr_select]
    comp_choice = match_list[comp_select]

    result_str = (
        f"GAME #{matches + 1} [{result}]\n"
        + f"PLAYER: {plr_choice}"
        + f"COMPUTER: {comp_select}"
    )

    if len(results_list) == 5: results_list.pop()
    results_list.append(result_str)


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
def menu() -> int:

    selection = -1

    print("YOU ARE NOW PLAYING [ROCK PAPER SCISSORS]")
    print("SELECT A MENU OPTION FROM THE CHOICES BELOW:")
    print("1. Start Game")
    print("2. List Previous Matches")
    print("0. Exit Program")

    while selection > 2 or selection < 0:
        selection = int(input("> "))

    return selection

# Game Function. Starts the Rock-Paper-Scissors Game
def game(results_list: list, matches_played: int) -> int:

    plr_select = -1
    result = ""

    print("STARTING A NEW ROUND...")
    
    print("CHOOSE AN OPTION:")
    print("  ROCK (0)")
    print("  PAPER (1)")
    print("  SCISSORS (2)")

    while plr_select > 2 or plr_select < 0:
        plr_select = int(input("> "))

    comp_select = random.randint(0, 2)
    result = eval_winner(plr_select, comp_select)

    match (result):
        case 1:
            print("CONGRATULATIONS! YOU WIN!")
            result = "WIN"
        case 2:
            print("OH NO! YOU LOST!")
            result = "LOSS"
        case _:
            print("IT'S A DRAW!")
            result = "DRAW"

    store_results(plr_select, comp_select, result, results_list, matches_played)

    print("DO YOU WISH TO KEEP PLAYING? ('YES' OR 'NO')")
    choice = input("> ").lower()
    
    game_continue = 1 if choice == 'yes' else 0

    return game_continue
