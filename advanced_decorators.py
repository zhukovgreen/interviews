import functools


class counter:
    register = {}

    def __init__(self):
        self.counter = 0

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            self.counter += 1
            counter.register[id(f)] = self.counter
            return f(*args, **kwargs)

        return wrapped


@counter()
def foo(a, b):
    return a, b


@counter()
def bar(a, b):
    return a, b


print(foo(5, 6), foo(5, 6), foo(5, 6), bar(5, 6), bar(5, 6))
print(counter.register)


class CallCounter(type):
    def __new__(cls, *args, **kwargs):
        for name, method in filter(
            lambda method: not method[0].startswith("__")
            and callable(method[1]),
            args[2].items(),
        ):
            args[2][name] = cls.call_counter(method)
        return super().__new__(cls, *args, **kwargs)

    @staticmethod
    def call_counter(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            return f(*args, **kwargs)

        wrapper.calls = 0

        return wrapper


class A(metaclass=CallCounter):
    def __init__(self):
        pass

    def check(self):
        pass


a = A()
a.check()
a.check()
print(a.check.calls)
