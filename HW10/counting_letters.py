
def solution(text: str) -> str:
    if not text:
        return ""

    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(text[i - 1] + (str(count) if count > 1 else ""))
            count = 1

    result.append(text[-1] + (str(count) if count > 1 else ""))

    return "".join(result)


assert solution("cccbba") == "c3b2a"
assert solution("abeehhhhhccced") == "abe2h5c3ed"
assert solution("aaabbceedd") == "a3b2ce2d2"
assert solution("abcde") == "abcde"
assert solution("aaabbdefffff") == "a3b2def5"
