from matplotlib import pyplot as plt


def func1(i):
    return i / decompose_range


def func2(i):
    return 2 ** (i / decompose_range)


def func3(i):
    return 1 / (decompose_range + 1 - i)


def func4(i):
    return i / (2 ** decompose_range)


def func5(i):
    return 2 ** (i - decompose_range)


def draw(x, y, i):
    plt.scatter(x, y, )
    plt.title(str(i))
    plt.show()


def run():
    y = [0 for i in range(decompose_range)]
    set_of_func = [func1, func2, func3, func4, func5]
    i = 1
    for func in set_of_func:
        x = [func(i) for i in range(decompose_range)]
        draw(x, y, i)
        i += 1


if __name__ == "__main__":
    decompose_range = 50
    run()
