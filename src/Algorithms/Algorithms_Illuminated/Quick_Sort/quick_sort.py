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
    i = choose_pivot(arr, l, r)
    arr[l], arr[i] = arr[i], arr[l]
    j = partition(arr, l, r)
    quick_sort_(arr, l, j - 1)
    quick_sort_(arr, j + 1, r)


def quick_sort(arr):
    quick_sort_(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [random.randint(1, 30) for _ in range(20)]
    print(arr)
    quick_sort(arr)
    print(arr)
