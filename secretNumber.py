secret_number = 9

guess_number = input("Please take a guess of a secret number: ")

if secret_number == int(guess_number):
    print("Bravo, you are a genius, you found the secret number.")

else:
    print("Sorry, but your guess is wrong. The secret number that we are looking for is: " + str(secret_number))