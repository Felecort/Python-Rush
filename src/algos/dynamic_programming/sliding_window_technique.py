from random import randrange


def sliding_window(arr, k): # O(n)
    sum = 0
    for i in range(k):
        sum += arr[i]
    for i in range(1, len(arr) - k):
        sum = sum - arr[i - 1] + arr[i + k - 1]
    return sum


arr = [randrange(2, 10) for _ in range(10)]
k = 4
x = sliding_window(arr, k)
