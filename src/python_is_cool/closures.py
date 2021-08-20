from pprint import pprint


def whisper(text):
    return text.lower() + '...'


def yell(text):
    return text.upper() + '!'


def greet(func):
    greeting = func('hello')
    print(greeting)


bark = yell
del yell
greet(bark)
greet(whisper)


def get_speak_func_2(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper


c = get_speak_func_2("hello world", 0.4)()
print(c)


def make_adder(n):
    def add(x):
        return x + n

    return add


plus_7 = make_adder(7)
plus_3 = make_adder(3)

print(plus_7(4))
print(plus_3(10))
# pprint(globals())
