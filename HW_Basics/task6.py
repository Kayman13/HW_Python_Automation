

def file_stats(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = len(content.split('\n'))
    words = len(content.split())
    letters = sum(1 for char in content if char.isalpha())

    result = f"\nLines: {lines}\nWords: {words}\nLetters: {letters}\n"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(result)

    print(result)
