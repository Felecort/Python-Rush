import timeit

time = timeit.timeit("sum(range(10**8))", number=1)
print(time)
