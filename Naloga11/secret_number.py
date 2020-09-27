import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0

#homework 11.1
guesses = []


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

    #homework 11.3
    new_list = sorted(score_list, key=lambda k: k['attempts'])
    for score_dict in new_list[0:3]:
        print("Attempts made: {0}, Time of game: {1}, Name: {2}".format(score_dict["attempts"], score_dict["timestamp"], score_dict["user_name"]))

while True:
    guess = int(input("Guess the secret number(between 1 and 30): "))
    attempts += 1

    #homework 11.2
    if guess != secret:
        guesses.append(guess)

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        #homework 11.1
        user_name = input("Please enter your name: ") #Naloga11_1
        datum = datetime.datetime.now()

        #homework 11.1, homework 11.2
        score_data = {
             "timestamp": datum.strftime("%d-%m-%Y %H:%M:%S"),
             "attempts": attempts,
             "user_name": user_name,
             "secret_number": secret,
             "wrong_guesses": guesses

        }
        score_list.append(score_data)

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    else:
        print("Your guess is not correct... try something bigger")

