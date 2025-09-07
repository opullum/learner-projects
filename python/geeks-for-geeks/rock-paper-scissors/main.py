# Entry point of Rock Paper Scissors game

from game import menu, start_game, show_results

game_data = { "results": [], "matches": 0 }
running = True

# Primary program loop. Functions are called from game.py
# menu() -> returns user selection to correspond with options listed

while (running):
    choice = menu()
    match choice:
        case 1: start_game(game_data)
        case 2: show_results(game_data["results"])
        case 0: running = False
    