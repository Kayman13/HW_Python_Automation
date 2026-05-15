
def square_number(num):
    return num ** 2


def is_even(num):
    return num % 2 == 0


num1 = int(input("Enter a number: "))

print("Square:", square_number(num1))

if is_even(num1):
    print("Even")
else:
    print("Odd")
