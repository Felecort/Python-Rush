from random import randint


def partition(arr):
    left = 1
    for right in range(1, len(arr)):
        if arr[0] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    arr[0], arr[left - 1] = arr[left - 1], arr[0]
    return left - 1


if __name__ == "__main__":
    for _ in range(10_000):
        arr = [randint(1, 30) for _ in range(10)]
        left = partition(arr)
        
        if not all([i <= (arr[left]) for i in range(0, left)]):
            print(arr, left)

