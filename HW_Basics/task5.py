
def is_palindrome(num: str) -> bool:
    if num.startswith('-'):
        return False
    return num == num[::-1]


num1 = input("Enter a number: ")
print("Result:", is_palindrome(num1))
