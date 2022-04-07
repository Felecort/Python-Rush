
from multiprocessing import Process


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # Переопределяем функцию run
    def run(self):
        print("hello", self.name)


if __name__ == "__main__":
    p = PrintProcess("Mike")
    p.start()
    # Ждём завершения(завершаем) дочерних процессов
    p.join()
