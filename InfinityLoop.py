
def loop(a, b):
    steps = 0

    while a != b:
        a += 1
        b -= 1
        steps += 1

        if steps > 10:
            return True

    return False


print(loop(2, 6))
print(loop(2, 3))
