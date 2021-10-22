from random import randrange
from math import log10


# Работает только если все сиволы одинавковой длины: 1000, abcd, 0093
def radix_sort(arr): # O(n * d), d - digits (1000 - 4 d), memory: O(n)
    power_of_ten = 1
    max_pow = int(log10(arr[0])) + 1
    bucket = [[] for _ in range(10)]
    for pow in range(max_pow):
        for elem in arr:
            bucket[int(elem / power_of_ten) % 10].append(elem)
        arr.clear()
        for i in range(len(bucket)):
            for j in range(len(bucket[i])):
                arr.append(bucket[i][j])
            bucket[i].clear()
        power_of_ten *= 10


arr = [randrange(1000, 10000) for _ in range(100)]
# arr = [1445, 7944, 2584, 4569, 7777]
print(arr)
sr_arr = sorted(arr)
radix_sort(arr)
print(arr)
print(sorted(arr))
print(sr_arr == arr)
