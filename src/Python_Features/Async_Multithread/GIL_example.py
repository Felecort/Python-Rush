from threading import Thread
import time


""" По скорости выполнения оба метода одинаковы,
потому что присутствует GIL, но, если будут
присутствовать системыне вызовы, то они снимут
GIL на время своего выполнения, и распараллеленные
задачи будут выполняться быстрее

GIL - спят 5 милисекунд
"""


def count(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    n = 10
    # Последоватльное выполнение
    t0 = time.time()
    count(100_000_000)
    count(100_000_000)
    print(time.time() - t0)

    # Параллельное выполнение
    t0 = time.time()
    th1 = Thread(target=count, args=(100_000_000, ))
    th2 = Thread(target=count, args=(100_000_000, ))

    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print(time.time() - t0)
