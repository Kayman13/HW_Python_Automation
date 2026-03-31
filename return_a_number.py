
from functools import wraps


def ensure_numeric_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            print("Ошибка: результат не является числом")
        return result
    return wrapper


@ensure_numeric_result
def add(a, b):
    return a + b


@ensure_numeric_result
def concat(a, b):
    return str(a) + str(b)


print(add(2, 3))
print(concat(2, 3))
