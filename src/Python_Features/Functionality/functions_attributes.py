
def foo():
    pass


def func(x):
    func.power2 = x ** 2
    func.power4 = func.power2 ** 2
    return x * 10


res = func(20)
print(res, func.power2, func.power4)

print(10)
