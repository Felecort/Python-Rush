from memory_profiler import profile
from copy import deepcopy

@profile()
def foo():
    x = list(range(1_000_000))
    y = x.copy()
    z = deepcopy(x)
    return z
foo();