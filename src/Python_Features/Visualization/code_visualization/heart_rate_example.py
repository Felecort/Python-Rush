from random import randint
import heartrate
heartrate.trace(browser=True)


def selection_sort(arr):  # O(n^2) memory: O(1)
    for j in range(len(arr)):
        min_ind = j
        for i in range(j, len(arr)):
            if arr[min_ind] > arr[i]:
                min_ind = i
        arr[j], arr[min_ind] = arr[min_ind], arr[j]


arr = [randint(0, 5_000) for _ in range(5_000)]
sr_arr = sorted(arr)

selection_sort(arr)

print(sr_arr == arr)
