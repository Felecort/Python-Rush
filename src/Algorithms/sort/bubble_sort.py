from random import randrange


# Without optimization
def bubble_sort(arr):  # O(n^2) memory: O(1)
    for j in range(len(arr)):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]


# With optimization
def bubble_sort_opt(arr):  # O(n^2) memory: O(1)
    for j in range(len(arr)):
        is_sorted = True
        for i in range(1, len(arr) - j):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                is_sorted = False
        if is_sorted:
            return



arr = [randrange(0, 30) for _ in range(500)]
sr_arr = sorted(arr)

bubble_sort_opt(arr)

print(sr_arr == arr)
