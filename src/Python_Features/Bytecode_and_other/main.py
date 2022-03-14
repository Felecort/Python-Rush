import dis
import opcode


def multiply(a, b):
    return a * b


print(dir(multiply), "\n")
print(multiply.__code__, "\n")

# Bytecode
print(multiply.__code__.co_code, "\n")
dis.dis(multiply)

# Список инструкций байткода
print("\n", opcode.opmap)