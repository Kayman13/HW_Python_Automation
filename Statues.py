
def statues(num):
    num.sort()
    missing = 0

    for n in range(len(num) - 1):
        step = num[n + 1] - num[n]
        if step > 1:
            missing += step - 1

    return missing


print(statues([6, 2, 3, 8]))
