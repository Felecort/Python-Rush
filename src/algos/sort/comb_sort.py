from random import randrange


def comb_sort(arr):
    is_sorted = False
    factor = 1.247
    gap = int(len(arr) / factor)
    while not is_sorted:
        if gap <= 1:
            is_sorted = True
            gap = 1
        for i in range(len(arr) - gap):
            j = i + gap
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
                is_sorted = False
        gap = int(gap / factor)


# for _ in range(20):
#     arr = [randrange(-100_000, 100_000) for _ in range(100_000)]
#     sr_arr = sorted(arr)
#     comb_sort(arr)
#     if arr != sr_arr:
#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i + 1]:
#                 print(i)
#         print(arr)
#         break

x = [randrange(0, 1_000_000) for i in range(10_000_000)]