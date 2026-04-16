
def file_stats(file_path):
    f = open(file_path, "r", encoding="utf-8")
    content = f.read()
    f.close()
    lines = len(content.split('\n'))
    words = len(content.split())
    letters = 0
    for char in content:
        if char.isalpha():
            letters += 1

    result = f"\nLines: {lines}\nWords: {words}\nLetters: {letters}\n"

    f = open(file_path, "a", encoding="utf-8")
    f.write(result)
    f.close()

    print(result)
