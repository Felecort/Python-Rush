from functools import cache, lru_cache
import time


def fib(i):
    if i <= 1:
        return i
    return fib(i - 1) + fib(i - 2)


@cache
def fib_cache(i):
    if i <= 1:
        return i
    return fib_cache(i - 1) + fib_cache(i - 2)


@lru_cache(maxsize=5)
def fib_lru_cache(i):
    if i <= 1:
        return i
    return fib_lru_cache(i - 1) + fib_lru_cache(i - 2)


def main():
    n = 37

    for i in range(n):
        start = time.perf_counter()
        fib(i)
        print(f"fib, {i = }, time = {time.perf_counter() - start}")

    print()

    for i in range(n):
        start = time.perf_counter()
        fib_cache(i)
        print(f"fib_cache, {i = }, time = {time.perf_counter() - start}")

    print()

    for i in range(n):
        start = time.perf_counter()
        fib_lru_cache(i)
        print(f"fib_lru_cache, {i = }, time = {time.perf_counter() - start}")

if __name__ == "__main__":
    main()
