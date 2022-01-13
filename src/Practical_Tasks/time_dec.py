import time


def time_it(func):
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f'args: {args}, time = {time.time() - start}')
        return res
    return inner
