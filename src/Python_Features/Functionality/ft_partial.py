from functools import partial


def greeter(person, greeting):
    return f"{greeting}, {person}!"


hier = partial(greeter, greeting="Hi")
helloor = partial(greeter, greeting="Hello")

print(hier("brother"))
print(helloor("sir")) 