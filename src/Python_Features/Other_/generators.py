from time import time


def gen_file_name():
    while True:
        pattern = 'file-{}.jpg'
        t = int(time() * 1000)
        yield pattern.format(str(t))
        print(456)


def gen():
    while True:
        yield 1
        yield 2


g = gen_file_name()


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1("hello")
g2 = gen2(7)
tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
