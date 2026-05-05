
def luhn_validate(number):
    if not isinstance(number, int) or number < 0:
        return False

    digits = [int(d) for d in str(number)][::-1]

    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d

    return total % 10 == 0


assert luhn_validate(4561261212345464) is False
assert luhn_validate(4561261212345467) is True
