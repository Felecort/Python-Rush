from random import randrange


# Подходит для маленького количества элементов
# Особенно для почти отсортированных массивов
def insertion_sort(arr):  # O(n^2), memory: O(1)
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur


arr = [randrange(0, 30) for _ in range(1_000)]
sr_arr = sorted(arr)
insertion_sort(arr)
print(sr_arr == arr)
