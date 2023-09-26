import multiprocessing as mp
import os


def to_celsius(f):
    c = (f - 32) * (5 / 9)
    pid = os.getpid()
    print(f"{f}F is {c:.0f}C. PID: {pid}")


if __name__ == "__main__":
    mp.set_start_method("spawn")
    with mp.Pool(4) as pool:
        pool.map(to_celsius, range(110, 150, 10))
    print("=" * 23)
    with mp.Pool(4, maxtasksperchild=1) as pool:
        pool.map(to_celsius, range(110, 150, 10))