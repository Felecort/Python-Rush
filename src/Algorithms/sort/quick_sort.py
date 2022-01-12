from random import randrange


def partition(arr, i, j):  # O(n^2) -- O(n * log(n)) memory: O(1)
    # pivot = randrange(1, len(arr)) % (j - i) + i
    pivot = randrange(i, j)
    arr[pivot], arr[i] = arr[i], arr[pivot]
    pivot = i
    s1_index = i
    s2_index = i
    for k in range(i + 1, j):
        if arr[k] >= arr[pivot]:
            s2_index += 1
        else:
            s1_index += 1
            arr[s1_index], arr[k] = arr[k], arr[s1_index]
            s2_index += 1
    arr[pivot], arr[s1_index] = arr[s1_index], arr[pivot]
    return s1_index


def quick_sort_(arr, i, j):
    if i == j:
        return
    pivot = partition(arr, i, j)
    # [i, pivot - 1] < pivot, [pivot + 1 , j] >= pivot
    quick_sort_(arr, i, pivot)
    quick_sort_(arr, pivot + 1, j)


def quick_sort(arr):
    quick_sort_(arr, 0, len(arr))


arr = [randrange(0, 30) for _ in range(200)]
sr_arr = sorted(arr)
quick_sort(arr)
print(sr_arr != arr)
