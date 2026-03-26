
def solution(candle_number: int, make_new: int) -> int:
    total = candle_number
    leftovers = candle_number

    while leftovers >= make_new:
        new_candles = leftovers // make_new
        total += new_candles
        leftovers = leftovers % make_new + new_candles

    return total


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 4) == 19
assert solution(13, 5) == 16
assert solution(2, 3) == 2
