def verify_input(called_nums: list) -> bool:

    if not called_nums: print("HOW DID YOU GET HERE??")

    latest_num = called_nums[-1]

    if latest_num < 0 or latest_num >= 21: return False
    if len(called_nums) == 1: return True

    previous_num = called_nums[-2]
    return (latest_num - previous_num == 1)

def player_lost() -> bool:
    continue_playing = True
    
    print("OH NO! IT APPEARS YOU HAVE LOST!")
    print("WOULD YOU LIKE TO KEEP PLAYING?")
    print("ENTER 'YES' OR 'NO' AS AN ANSWER!")
    response = input("> ").lower()

    if (response == 'no'): continue_playing = False

    return continue_playing

def player_turn(called_numbers: list) -> tuple[bool, bool]:

    game_ended = False

    print("HOW MANY NUMBERS WOULD YOU LIKE TO CALL?")
    print("YOU MAY CALL UP TO 3 NUMBERS!")
    added_amount = int(input("> "))

    if added_amount > 3 or added_amount <= 0: game_ended = True


    if called_numbers and not game_ended: 
        print("EXCELLENT. PLEASE ENTER THE NUMBERS YOU WOULD LIKE TO CALL:")
        print(f"CURRENT NUMBERS: {called_numbers}")
    else:
        print("EXCELLENT. PLEASE ENTER THE NUMBERS YOU WOULD LIKE TO CALL:")
        print("NO NUMBERS HAVE BEEN CALLED. PLEASE CALL CONSECUTIVE NUMBERS STARTING FROM 1!")

    added_count = 0

    while not game_ended and (added_count < added_amount): 
        added_num = int(input("> "))

        called_numbers.append(added_num)
        game_ended = not verify_input(called_numbers)
        added_count += 1

    if (game_ended): return game_ended, player_lost()
    return game_ended, True

