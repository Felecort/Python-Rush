import datetime
import heapq
import types
import time

class Task:

    """Представляет, как долго сопрограмма должна ждать перед возобновлением выполнения.

    Операторы сравнения реализованы для использования в heapq.
    К сожалению, кортеж с двумя элементами не работает, потому что,
    когда экземпляры класса datetime.datetime равны, выполняется 
    сравнение сопрограмм, а поскольку они не имеют методом, реализующих 
    операции сравнения, возникает исключение.

    Считайте класс подобием о asyncio.Task/curio.Task.
    """

    def __init__(self, wait_until, coro):
        self.coro = coro
        self.waiting_until = wait_until

    def __eq__(self, other):
        return self.waiting_until == other.waiting_until

    def __lt__(self, other):
        return self.waiting_until < other.waiting_until

class SleepingLoop:

    """Event loop, сфокусированный на отложенном выполнении сопрограмм.

    Считайте класс подобием asyncio.BaseEventLoop/curio.Kernel.
    """

    def __init__(self, *coros):
        self._new = coros
        self._waiting = []

    def run_until_complete(self):
        # Запустить все сопрограммы.
        for coro in self._new:
            wait_for = coro.send(None)
            heapq.heappush(self._waiting, Task(wait_for, coro))
        # Не прерывать выполнение, пока есть выполняющиеся сопроцедуры.
        while self._waiting:
            now = datetime.datetime.now()
            # Получаем сопрограмму с самым ранним временем возобновления.
            task = heapq.heappop(self._waiting)
            if now < task.waiting_until:
                # Мы оказались здесь раньше, чем нужно, 
                # поэтому подождем, когда придет время возобновить сопрограмму.
                delta = task.waiting_until - now
                time.sleep(delta.total_seconds())
                now = datetime.datetime.now()
            try:
                # Время возобновить выполнение сопрограммы.
                wait_until = task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except StopIteration:
                # Сопрограмма завершена.
                pass

@types.coroutine
def sleep(seconds):
    """Останавливает сопрограмму на указанное количество секунд.

    Считайте класс подобием asyncio.sleep()/curio.sleep().
    """
    now = datetime.datetime.now()
    wait_until = now + datetime.timedelta(seconds=seconds)
    # Останавливаем все сопроцедуры в текущем стэке. Тут необходимо
    # использовать ```yield```, чтобы создать сопрограмму на базе генератора,
    # а не на базе ```async```.
    actual = yield wait_until
    # Возобновляем стэк выполнения, возвращая время, 
    # которое мы провели в ожидании.
    return actual - now

async def countdown(label, length, *, delay=0):
    """Начинает обратный отсчет с секунд ```length``` и с задержкой ```delay```.

    Это обычно то, что реализует пользователь.
    """
    print(label, 'waiting', delay, 'seconds before starting countdown')
    delta = await sleep(delay)
    print(label, 'starting after waiting', delta)
    while length:
        print(label, 'T-minus', length)
        waited = await sleep(1)
        length -= 1
    print(label, 'lift-off!')

def main():
    """Запустить event loop с обратным отсчетом 3 отдельных таймеров.

    Это обычно то, что реализует пользователь.
    """
    loop = SleepingLoop(countdown('A', 5),
                        countdown('B', 3, delay=2),
                        countdown('C', 4, delay=1))
    start = datetime.datetime.now()
    loop.run_until_complete()
    print('Total elapsed time is', (datetime.datetime.now() - start))

if __name__ == '__main__':
    main()