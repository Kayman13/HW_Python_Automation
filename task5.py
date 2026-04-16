
def is_palindrome():
    num = input("Enter a number: ")
    if num.startswith('-'):
        return False
    return num == num[::-1]


print("Result:", is_palindrome())
