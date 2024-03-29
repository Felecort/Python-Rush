import multiprocessing as mp
import os
from decimal import Decimal

def to_celsius(f):
    c = (f - 32) * (5 / 9)
    pid = os.getpid()
    print(f"{f}F is {c:.0f}C. PID: {pid}")


if __name__ == "__main__":
    print(os.getpid())
    mp.set_start_method("spawn")
    p = mp.Process(target=to_celsius, args=(110, ))
    p.start()
