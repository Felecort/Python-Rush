from random import randrange


def shell_sort(arr):
    step = len(arr) // 2
    while step > 0:
        for i in range(step, len(arr)):
            j = i
            delta = j - step
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step
        step //= 2


for _ in range(200):
    arr = [randrange(-1_000, 1_000) for _ in range(1_000)]
    sr_arr = sorted(arr)
    shell_sort(arr)
    if arr != sr_arr:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                print(i)
        print(arr)
        break
