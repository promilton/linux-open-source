from .csv_ import CSV
from .json_ import JSON

CLASS = [CSV, JSON]


def get_file_class(extension):
    for cls in CLASS:
        if extension in cls.EXTENSION:
            return cls
    return None


def report(function):
    def wrapper(*args, **kwargs):
        print("log started")
        print(f"From {function.__qualname__} function with the argument(s)", *args[1:], **kwargs)
        rv = function(*args, **kwargs)
        return rv
    return wrapper


class Meta(type):
    def __new__(mcs, name, bases, attrs):
        print("Meta class initiated")
        for name, value in attrs.items():
            if name.startswith("__"):
                pass
            else:
                print(name.upper())
        return type(name, bases, attrs)
