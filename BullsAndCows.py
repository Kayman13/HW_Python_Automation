import random
import string


def gen_number():
    numbers = string.digits
    return "".join(random.sample(numbers, 4))


def user_guess():
    while True:
        guess = input("Enter 4 digits: ")

        if not guess.isdigit():
            continue
        if len(guess) != 4:
            continue
        if len(set(guess)) != 4:
            continue

        return guess


def check_num(secret_num, guess):
    bulls_count = 0
    cows_count = 0

    for i, digit in enumerate(secret_num):
        if guess[i] == digit:
            bulls_count += 1
        elif guess[i] in secret_num:
            cows_count += 1

    return bulls_count, cows_count


secret = gen_number()

while True:
    attempt = user_guess()
    bulls, cows = check_num(secret, attempt)

    print(f"Bulls: {bulls}, Cows: {cows}")

    if bulls == 4:
        print("Win")
        break
