def player_lost() -> bool:
    continue_playing = True
    
    print("OH NO! IT APPEARS YOU HAVE LOST!")
    print("WOULD YOU LIKE TO KEEP PLAYING?")
    print("ENTER 'YES' OR 'NO' AS AN ANSWER!")
    response = input("> ").lower()

    if (response == 'no'): continue_playing = False

    return continue_playing

def player_turn(called_numbers: list) -> tuple[bool, bool]:
    return False, True