
def mirror_string(text, n):
    left = text[:n]
    right = left[:-1][::-1]
    return left + right


s = "abcdefghijklmnopqrstuvwxyz"
print(mirror_string(s, 1))
print(mirror_string(s, 2))
print(mirror_string(s, 3))
print(mirror_string(s, 4))
