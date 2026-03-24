
def sequence_solution(sequence):
    violations = 0

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            violations += 1
            if violations > 1:
                return False

            if 0 < i < len(sequence) - 2:
                if sequence[i - 1] >= sequence[i + 1] and sequence[i] >= sequence[i + 2]:
                    return False

    return True


assert sequence_solution([1, 2, 3]) is True
assert sequence_solution([1, 2, 1, 2]) is False
assert sequence_solution([1, 3, 2, 1]) is False
assert sequence_solution([1, 2, 3, 4, 5, 3, 5, 6]) is False
assert sequence_solution([40, 50, 60, 10, 20, 30]) is False
