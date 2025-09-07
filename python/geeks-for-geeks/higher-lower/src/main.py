# HIGHER LOWER GAME
# Python assignment based on the GeeksForGeeks listing of the project.
# Guess whether a shown figure has a higher/lower follower account than the
# compared person
#
# Entry point for the program. Contains handling of the game loop
# and primary variables

from game import start_game, menu
from data import Data

game_data = {}
status = ""
code = 0
running = True
data_obj = Data()

while running:
    selection = menu(data_obj, code, status)
    match(selection):
        case 1: start_game(game_data, data_obj)
        case 2: 
            status = f"Your current streak is {game_data["streak"]}"
            menu(data_obj, code, status)
        case 3: data_obj.load_file()
        case 0: running = False







