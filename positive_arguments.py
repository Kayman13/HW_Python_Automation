
from functools import wraps


def validate_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("Все аргументы должны быть положительными числами")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def add(a, b):
    return a + b


print(add(3, 5))
