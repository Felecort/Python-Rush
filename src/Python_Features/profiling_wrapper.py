from functools import reduce
import numpy as np
from time import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        stop = time()
        print(f"func: {f.__name__}:.20\ttime: {stop - start:.2f}, res: {res}")
        return res
    return wrapper


@timeit
def manual_sum(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

@timeit
def standart_sum(n):
    return sum((range(1, n + 1)))

@timeit
def func_sum(n):
    return reduce(lambda x, y: x + y, (range(1, n + 1)))

@timeit
def np_sum(n):
    return np.arange(1, n + 1).sum()

N = 100_000_000
func_arr = [manual_sum, standart_sum, func_sum, np_sum]
for func in func_arr:
    func(N)