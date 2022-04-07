
from multiprocessing import Process


def f(name):
    print("Hello", name)


if __name__ == "__main__":
    # Передаём функцию и её аргументы.
    p = Process(target=f, args=("Bob",))

    # Создание процесса. Исполнение функции в отдельном процессе
    p.start()
    # Ждём завершения(завершаем) дочерних процессов
    p.join()
