from secret_number_func import play_game, get_top_scores

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection.upper() == "A":
        level = input("Choose your level (easy/hard): ")
        play_game(level=level.lower())
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print("Attempts made: {0}, Time of game: {1}, Name: {2}".format(score_dict["attempts"], score_dict["timestamp"], score_dict["user_name"]))
    else:
        print("Goodbye and thank you for playing!")
        break
