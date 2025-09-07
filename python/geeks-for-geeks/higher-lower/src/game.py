from os import system
from person import Person
from data import Data
from ascii import VS_TEXT, TITLE_TEXT

# Function to initialize a new Person object
#
# Returns: Person (newly created Person obj), bool (success of creation)

def initialize_person(data: dict) -> tuple[type[Person], bool]:
    return Person, False


# Compares the follower counts of the previous Person and current Person
#
# Returns: bool (depending on correct guess)

def verify_guess(guess: int, compared: Person, current: Person) -> bool:
    return False


# Prints the menu to the screen and allows the user to select an option
#
# Returns: int (menu selection)

def menu(data_obj: Data, code: int, status: str) -> int:
    system('cls||clear')

    print(TITLE_TEXT)
    if code == 1:
        data_obj.load_file()
    else:
        if status: print(status)

    print("MAIN MENU OPTIONS:")
    print("1. START GAME")
    print("2. LIST CURRENT STREAK")
    print("3. CHANGE DATA FILE")
    print("0. END PROGRAM")

    while True:
        try:
            selection = int(input("> "))
            if selection < 0 or selection > 3:
                print("Please enter a valid menu option...")
            else:
                break
        except ValueError:
            print("Please enter a valid menu option...")
        
    return selection



        

    





# Starts a new round of higher-lower
# The player will select whether the shown person has a higher/lower
# follower account than the new person (current, compared)
#
# Returns: int (errors, success), str (relevant post-game message)

def start_game(game_data: dict, data_obj: Data) -> tuple[int, str]:
    return 1, ""
