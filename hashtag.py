
def solution(text: str) -> str:
    stack = []

    for char in text:
        if char == "#":
            if stack:
                stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""
