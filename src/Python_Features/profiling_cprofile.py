from functools import reduce
import numpy as np
from time import time
import cProfile
from operator import add

def manual_sum(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

def standart_sum(n):
    return sum(list(range(1, n + 1)))


def my_add(x, y):
    return x + y
def func_sum(n):
    return reduce(add, list(range(1, n + 1)))

def np_sum(n):
    return np.arange(1, n + 1).sum()

N = 100_000_000
# func_arr = [manual_sum, standart_sum, func_sum, np_sum]
# func_arr = ["manual_sum", "standart_sum", "func_sum", "np_sum"]
# for func in func_arr:
#     print(f"{func}")
#     cProfile.run(f"{func}({N})")

cProfile.run(f"func_sum({N})")

    