
numbers = [1, 4, 9, 5]

iters = numbers.__iter__()
while True:
    try:
        x = iters.__next__()
        # print(x)
    except StopIteration:
        break


def range_1(start, stop):
    def step():
        nonlocal start
        res = start
        start += 1
        return res

    return iter(step, stop)


z = range_1(0, 10)
z.__next__()
z.__next__()


def range_2(start, stop):
    while start < stop:
        yield start
        start += 1
