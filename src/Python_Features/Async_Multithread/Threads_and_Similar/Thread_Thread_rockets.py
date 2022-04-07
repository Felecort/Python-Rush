import time
import random
from threading import Thread
import tracemalloc

tracemalloc.start()


def counter(start=1):
    while True:
        yield start
        start += 1


def random_delay():
    return random.random() * 10


def random_countdown():
    return random.randrange(3)


def launch_rocket(delay, countdown, count):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    next(count)
    print("Rocket Launch")


def rockets():
    n = 20
    return [(random_delay(), random_countdown()) for _ in range(n)]


def run_threading(count):
    threads = [
        Thread(target=launch_rocket, args=(d, c, count))
        for d, c in rockets()
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    count = counter(1)
    run_threading(count)
    print(next(count) - 1)
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
