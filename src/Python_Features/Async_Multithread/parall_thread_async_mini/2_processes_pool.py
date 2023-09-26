import multiprocessing
import os
from time import time


def f(x):
    # print(os.getpid())
    x1 = hash(x + 1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    x1 = hash(x1)
    return x1


if __name__ == "__main__":
    n_proc = 16
    start = time()
    with multiprocessing.Pool(processes=n_proc) as pool:
        # map -  like ordinary map
        n = 100000000
        res = pool.map(f, range(n))
    stop = time()
    print(f"{stop - start:.2f}, processes: {n_proc}")

    n_proc = 2
    start = time()
    with multiprocessing.Pool(processes=n_proc) as pool:
        # map -  like ordinary map
        n = 100000000
        res = pool.map(f, range(n))
        pool.apply_async
    # stop = time()
    print(f"{stop - start:.2f}, processes: {n_proc}")
        # apply - aplly only one function
    