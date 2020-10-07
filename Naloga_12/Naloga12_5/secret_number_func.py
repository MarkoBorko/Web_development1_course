import random
import datetime
import json


def play_game(level="easy"):
    secret_number = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    guesses = []

    while True:
        guess = int(input("Guess the secret number(between 1 and 30): "))
        attempts += 1

        if guess != secret_number:
            guesses.append(guess)

        if guess == secret_number:
            print("You've guessed it - congratulations! It's number " + str(secret_number))
            print("Attempts needed: " + str(attempts))

            user_name = input("Please enter your name: ")
            datum = datetime.datetime.now()

            score_data = {
                "timestamp": datum.strftime("%d-%m-%Y %H:%M:%S"),
                "attempts": attempts,
                "user_name": user_name,
                "secret_number": secret_number,
                "wrong_guesses": guesses
            }

            score_list.append(score_data)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            break

        elif guess > secret_number and level == "easy":
            print("Your guess is not correct... try something smaller")

        elif guess < secret_number and level == "easy":
            print("Your guess is not correct... try something bigger")


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    return score_list


def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

    return top_score_list




