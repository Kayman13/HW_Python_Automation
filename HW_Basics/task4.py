
def plus_one(digits: list[int]) -> list[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


print(plus_one([9]))
print(plus_one([1, 2, 3]))
print(plus_one([1, 1, 9]))
print(plus_one([9, 9, 9]))
