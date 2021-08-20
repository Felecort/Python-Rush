
from pprint import pprint
import dis
import sys
from tokenize import tokenize
from io import BytesIO
from token import tok_name
import ast


# 1
def foo(x: int, y: int) -> int:
    return x + y


z: int
z = foo(4, 7)
print(z)


# 2
code_string = "print(444 + 444) 4 *8"
tokens = tokenize(BytesIO(code_string.encode("utf-8")).readline)
pprint([(token.string, tok_name[token.type]) for token in tokens])


# 3
str_obj = """
def foo(x: int) -> int:
    x = x * (x + 7)
    return x


z = foo(7)
print(z)
"""

pprint(ast.dump(ast.parse(str_obj)))
print()
print(dis.dis(str_obj))


# 4
def get_frame():
    local_var = 7 + 54
    frame = sys._getframe()
    instruction = frame.f_lasti
    return frame, instruction


frame, instruction = get_frame()
pprint(frame.f_locals)
pprint(len(frame.f_globals))


def fib():
    a, b = 0, 1
    x = 1
    while x < 10:
        x += 1
        yield a
        a, b = b, a + b


print(list(fib()))
