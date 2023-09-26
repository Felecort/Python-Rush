from time import time



def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        stop = time()
        print(f"time: {stop - start}")
        return res
    return wrapper


def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            start = time()
            for _ in range(n):
                res = f(*args, **kwargs)
            stop = time()
            print(stop - start)
            return res
        return wrapper
    return inner


@ntimes(10000000)
def add(x, y=10):
    return x + y


print(add(1, 2))


