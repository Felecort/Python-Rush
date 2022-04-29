from random import randint


def partition_(arr, l, r):
    p = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    
    return (i - 1)


def partition(arr):
    left = 1
    for right in range(1, len(arr)):
        if arr[0] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    arr[0], arr[left - 1] = arr[left - 1], arr[0]
    return left - 1


if __name__ == "__main__":
    arr = [randint(1, 30) for _ in range(20)]
    i, j = 5, 15
    print(arr[:i], arr[i:])
    left = partition_(arr, 5, 15)
    print(arr)
    
    
    # for _ in range(1_000_000):
    #     arr = [randint(1, 30) for _ in range(10)]
    #     arr_copy = arr[:]
    #     left = partition(arr)

    #     if not all([arr[i] <= (arr[left]) for i in range(0, left)]):
    #         print(arr_copy, arr, left)
