
def opposite_number_solution(n, first_number):
    return (first_number + n // 2) % n


assert opposite_number_solution(10, 6) == 1
assert opposite_number_solution(10, 2) == 7
assert opposite_number_solution(10, 4) == 9
