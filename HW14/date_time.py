
from datetime import datetime


def days_between(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def check_date(date_str: str) -> str:
    user_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    if user_date > today:
        return "Future date"
    if user_date < today:
        return "Past date"
    return "Today"


if __name__ == "__main__":
    print(days_between("2023-01-01", "2023-01-10"))
    print(check_date("2030-01-01"))
