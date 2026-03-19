import random


def gen_number():
    numbers = "0123456789"
    rand_number = random.sample(numbers, 4)
    secret_num = "".join(rand_number)
    return secret_num


def user_guess():
    guess = input("Enter 4 numbers:")
    return guess


def check_num(secret_num, guess):
    bulls_count = 0
    cows_count = 0
    for i in range(4):
        if guess[i] == secret_num[i]:
            bulls_count += 1
        elif guess[i] in secret_num:
            cows_count += 1
    return bulls_count, cows_count


secret = gen_number()


while True:
    attempt = user_guess()
    bulls, cows = check_num(secret, attempt)
    print(f"Bulls: {bulls},Cows:{cows}")
    if bulls == 4:
        print("Win")
        break
