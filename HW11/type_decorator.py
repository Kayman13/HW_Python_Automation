
from functools import wraps


def typed(type_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = tuple(type_(arg) for arg in args)
            new_kwargs = {k: type_(v) for k, v in kwargs.items()}
            return func(*new_args, **new_kwargs)
        return wrapper
    return decorator


@typed(type_=str)
def add(a, b):
    return a + b


print(add("3", 5))
print(add(5, 5))
print(add('a', 'b'))


@typed(type_=int)
def add_int(a, b, c):
    return a + b + c


print(add_int(5, 6, 7))


@typed(type_=float)
def add_float(a, b, c):
    return a + b + c


print(add_float(0.1, 0.2, 0.4))
