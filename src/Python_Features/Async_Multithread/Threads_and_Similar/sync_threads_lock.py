import threading


# Лушче использовать очереди, а не блокировки
# Первый вариант
class poinr(object):
    def __init__(self) -> None:
        self._mutex = threading.RLock()
        self._x = 0
        self._y = 0

    def get(self):
        with self._mutex:
            return (self._x, self._y)

    def set(self, x, y):
        with self._mutex:
            self._x = x
            self._y = y


# Второй вариант
# Если будет много процессов, то случится deadlock, 
# потому что освобождение процессов в неправильнойц
# последовательности
def foo():
    try:
        # Захват блокировки
        a.acquire()
        b.acquire()
    finally:
        # Высвобождени блокировки
        a.release()
        b.release()


if __name__ == "__main__":
    a = threading.RLock()
    b = threading.RLock()
