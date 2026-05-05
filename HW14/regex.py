
import re


def find_dates(input_text: str):
    return re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", input_text)


def is_valid_password(password: str) -> bool:
    return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$", password))


def fix_repeated_words(input_text: str) -> str:
    return re.sub(r"\b(\w+)(\s+\1\b)+", r"\1", input_text, flags=re.IGNORECASE)


if __name__ == "__main__":
    sample_text = "Dates: 12.05.2020 and 01.01.2022"
    print(find_dates(sample_text))

    print(is_valid_password("Test1234"))

    bad_text = "Ошибка ошибка слова слова"
    print(fix_repeated_words(bad_text))
