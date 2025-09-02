from player import player_lost

def computer_lost() -> bool:

    continue_playing = True

    print("OH NO! IT APPEARS THE COMPUTER HAS LOST!")
    print("CONGRATULATIONS ON WINNING!")
    print("WOULD YOU LIKE TO KEEP PLAYING?")
    print("ENTER 'YES' or 'NO' AS AN ANSWER!")
    response = input("> ").lower()

    if (response == 'no'): continue_playing = False

    return continue_playing


def computer_turn(called_numbers: list) -> tuple[bool, bool]:

    recent_number = 0
    target_distance = 3
    game_ended = False
    continue_playing = True

    # Calculate target value for the computer to attempt to call towards
    if called_numbers:
        recent_number = called_numbers[-1]
        target_distance = 4 - (recent_number % 4) 

        if recent_number == 20: 
            continue_playing = computer_lost()
            game_ended = True

    if (not game_ended):
        print("THE COMPUTER WILL NOW PLAY...")

        if target_distance > 3: target_distance = 3

        added_num = recent_number + 1

        while added_num <= recent_number + target_distance:        
            called_numbers.append(added_num)
            added_num += 1   

        recent_number = called_numbers[-1]
        print("THE COMPUTER TURN IS NOW OVER!")

        if recent_number == 20: 
            continue_playing = player_lost()
            game_ended = True


    return game_ended, continue_playing