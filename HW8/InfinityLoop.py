
def solution(a, b):
    return a % 2 != b % 2 or a > b


assert solution(5, 100)
assert not solution(5, 101)
