from game import menu, start_game, show_results

game_data = {
    "results": [],
    "matches": 0
}
matches_played = 0
running = True

while (running):
    choice = menu()
    match choice:
        case 1: start_game(game_data)
        case 2: show_results(game_data["results"])
        case 0: running = False
    