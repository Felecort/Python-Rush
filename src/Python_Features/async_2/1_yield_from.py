import asyncio

arr = [1, 2, 3]

def foo():
    yield from arr

c = foo()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
