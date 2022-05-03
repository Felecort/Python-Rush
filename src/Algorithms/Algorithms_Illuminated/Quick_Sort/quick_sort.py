import random


def choose_pivot(l, r):
    return random.randint(l, r)


def partition(arr, l, r):
    p = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]

    return (i - 1)


def quick_sort_(arr, l, r):
    if l >= r:
        return 
    i = choose_pivot(l, r)
    arr[l], arr[i] = arr[i], arr[l]
    j = partition(arr, l, r)
    quick_sort_(arr, l, j - 1)
    quick_sort_(arr, j + 1, r)


def quick_sort(arr):
    quick_sort_(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    for _ in range(1000):
        arr_expr = [random.randint(1, 30) for _ in range(10)]
        arr_etalon = arr_expr[:]
        quick_sort(arr_expr)
        arr_etalon.sort()
        if not arr_etalon == arr_expr:
            print(arr_etalon, arr_expr)
